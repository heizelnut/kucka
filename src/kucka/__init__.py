# Copyright (c) 2019 Heizelnut (Emanuele Lillo)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
import sys
import yaml

class Kucka:
    VERSION = "0.1.0"
    AUTHOR = "Heizelnut (https://github.com/heizelnut)"
    DESCRIPTION = ("Minimalistic automation tool to build, run, install "
        "programs and much more.")

    def __init__(self, directive="default"):
        # Show splash screen only if asked
        if directive in ("--about", "-a", "--help", "-h", 
            "--version", "-v"):
            self.splash()
            sys.exit(0)
        
        # Define a tuple of valid filenames to analyze
        self.valid_files = ("Kuckafile", "Kuckafile.yml", "Kuckafile.yaml")
        
        # Set the directive
        self.directive = directive

        # Check for Kuckafiles in the current directory
        self.target = self.check_for_kuckafile()

        # Parse the file
        self.parse()

    def splash(self):
        # Write a header
        sys.stdout.write("Kucka by {} - version {}\n".format(
            self.AUTHOR, self.VERSION)
        )

        # Write an infobox
        sys.stdout.write(self.DESCRIPTION + "\n\n")
        sys.stdout.write("Github Repo: https://github.com/heizelnut/kucka\n")

        # Write a splitter
        sys.stdout.write("-" * 40 + "\n")
        
        # Flush the stdout buffer - write everything 
        #  in the buffer to the terminal
        sys.stdout.flush()

    def log(self, message):
        # Format the message with a " - " before and 
        #  a character return at the end
        log = " - {}\n".format(message)

        # Write the message
        sys.stdout.write(log)

        # Flush the stdout buffer
        sys.stdout.flush()

    def warn(self, message):
        # Format the message with a "[!] " before and 
        #  a character return at the end
        warn = "[!] {}\n".format(message)

        # Write the warning message
        sys.stderr.write(warn)

        # Flush the stderr buffer
        sys.stderr.flush()

    def fail(self, message):
        # Format the message with a "[!] " before and 
        #  a character return at the end
        error = "[x] {}\n".format(message)

        # Write the error message
        sys.stderr.write(error)

        # Flush the stderr buffer
        sys.stderr.flush()

        # Exit the process
        sys.exit(1)

    def check_for_kuckafile(self):
        # For every filename whitelisted
        for filename in self.valid_files:
            # Check if it exists in the current directory
            if os.path.isfile(filename):
                # Return it if it exists
                return filename
        # Fail otherwise
        self.fail("Kuckafile not present in this directory.")

    def parse(self):
        # Open the file and read the contents
        with open(self.target, "r") as f:
            contents = f.read()
        
        # Try to parse it with YAML - fail if there's an exception
        try:
            yaml_content = yaml.load(contents, Loader=yaml.SafeLoader)
        except:
            self.fail("Not valid YAML content.")
        
        # Process the parsed content 
        self.execute(yaml_content)
    
    def execute(self, content):
        # Fail if the directive starts with a dollar sign ("$")
        # (it's a special character used for internal variables)
        if self.directive.startswith("$"):
            self.fail("Cannot call a special directive.")

        # Fail if the directive doesn't exist
        if self.directive not in content:
            message = ("Directive '{}' not "
                "present in Kuckafile.").format(self.directive)
            self.fail(message)
        
        # Initialize the config
        config = {}

        # Get the directive's content
        directive = content[self.directive]

        # If there's a "$config" variable,
        #  check if it's a dict and store it temporarily.
        # Fail if it's not a dict.
        if "$config" not in content:
            self.warn("Config directive not found.")
        else:
            config = content["$config"]
            if type(config) is not dict:
                self.fail("Config directive is malformed.")

        # Check if directive's content is a list - otherwise fail.
        if type(directive) is list:

            # For every instruction in the directive
            for instruction in directive:
                # Check if instruction is a string, ignore otherwise
                if not isinstance(instruction, str):
                    continue

                # Format variables - take a cup of coffee while reading this.

                # Example instruction: `echo "$K(greet);"`
                # Replace every "$K(" and ");" with "{" and "}",
                #  this way the result will be `echo "{greet}"`.

                # Then, using the classic str method "format", replace
                #  every occurency with the corresponding value of the
                #  "config" dict.

                # So, if before we defined:
                # ```
                # $config:
                #   greet: "hello world"
                # ```
                # the result will be `echo "hello world"`.
                
                # You can swear to me now.

                instruction = instruction.replace("$K(", "{") \
                    .replace(");", "}")
                try:
                    instruction = instruction.format(**config)
                except KeyError as e:
                    self.fail(("{} is undefined, you should define"
                        " it inside $config.").format(e))

                # Execute the formatted instruction
                os.system(instruction)
        else:
            self.fail("Directive '{}' is not a list.".format(self.directive))
        
        # All's fine - end the program.
        self.log("Done.")
