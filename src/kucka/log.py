# Copyright (c) 2019 Heizelnut (Emanuele Lillo)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from sys import stdout

class Logger:
    def log(self, msg):
        message = " * {}\n".format(msg)
        stdout.write(message)
        stdout.flush()