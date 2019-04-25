# Copyright (c) 2019 Heizelnut (Emanuele Lillo)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os.path as path
from os import mkdir

class Configuration:
    def _check_config_folder(self):
        self.config_path = path.expanduser("~/.kucka")

        if not path.exists(self.config_path):
            self.log("Creating Kucka folder (~/.kucka)...")
            mkdir(self.config_path)