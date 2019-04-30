# Copyright (c) 2019 Heizelnut (Emanuele Lillo)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from . import Kucka
import sys

def main():
    if len(sys.argv) == 2:
        kucka = Kucka(sys.argv[1])
    else:
        kucka = Kucka()

if __name__ == "__main__":
    main()