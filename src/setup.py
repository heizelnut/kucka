# Copyright (c) 2019 Heizelnut (Emanuele Lillo)
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from setuptools import setup

def get_file_conts(file):
    with open(file, "r") as f:
        contents = f.read()
    
    return contents

setup(
    name="kucka",
    version="0.1.0",
    description="Simple configuration sharing tool through Git repositories.",
    long_description=get_file_conts("../README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/heizelnut/kucka",
    author="Heizelnut",
    author_email="emalillo270304@gmail.com",
    license="MIT",
    packages=["kucka"],
    install_requires=get_file_conts("./requirements.txt").split("\n")
    zip_safe=False
)