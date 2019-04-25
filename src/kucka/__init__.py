# Copyright (c) 2019 Heizelnut (Emanuele Lillo)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from .log import Logger
from .git import GitBindings
from .config import Configuration
from .parsing import Parser

class KuckaApp(Logger, GitBindings, Configuration, Parser):
    """Kucka - Simple config manager."""
    def __init__(self):
        self._check_config_folder()
        self.version = "0.1.0"