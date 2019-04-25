# Copyright (c) 2019 Heizelnut (Emanuele Lillo)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pygit2 import clone_repository
import os.path as path
from shutil import rmtree

class GitBindings:
    def clone(self, url, name):
        self.log("Cloning repository...")
        try:
            clone_repository(url, self._get_path(name))
        except ValueError:
            self.log("Recloning...")
            self.delete(name)
            clone_repository(url, self._get_path(name))
        self.log("Checking if Kuckafile is present...")
        self.is_valid_repo(name)

    def is_valid_repo(self, name):
        if not path.isfile("{}/Kuckafile".format(self._get_path(name))):
            self.delete(name)
            
            self.log("Kuckafile not found, repository deleted.")
            return

        self.log("Repository saved succesfully as '{}'.".format(name))
    
    def _get_path(self, name):
        return "{}/{}".format(self.config_path, name)

    def delete(self, name):
        if not path.isdir(self._get_path(name)):
            return "No repo named '{}' found.".format(name)
        
        rmtree(self._get_path(name))
        return "Succesfuly deleted '{}'.".format(name)