<!--
 Copyright (c) 2019 Heizenut
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

![logo]

![code-size] ![fork-me]

**Kucka** (`/'kutska/`) is a minimalistic **automation tool** to build, run, install programs and much more.

Not [him](https://en.wikipedia.org/wiki/Juraj_Kucka),
 neither [her](https://open.spotify.com/artist/6JcD2YKEhgimweLpUI0NEw).

## Install
Kucka is made up of a **Python Package**, which you can install by doing
```bash
git clone https://github.com/heizelnut/kucka # Clone the repository
cd kucka/src # Change working directory
python3 setup.py install # Install the package
```

## Usage
Go ahead and create a `Kuckafile.yml` file inside a directory.
Then, write as so:
```yaml
$config:
    greet: "Hello"

default:
    - echo "$K(greet); World!"
```
And after that, run `kucka` into the terminal. Play with the 
"greet" parameter.

You can also organize the file as sections, as you would imagine:
```yaml
$config:
    compiler: "gcc"

compile:
    - $K(compiler); main.c -o main

run:
    - ./main
```
Now create a simple C program inside `main.c`
```c
#include <stdio.h>

int main(void) {
    printf("Hello World!\n");
    return(0);
}
```
And run it by doing `kucka compile` and then `kucka run`.
> If there's nothing after the command, it picks the _default_ **directive**.

## Contributing
If you'd like to contribute, you're free to do so! Fork my project and then pull request me.

<!-- Shields & Logo-->
[code-size]: https://img.shields.io/github/languages/code-size/heizelnut/kucka.svg?color=success&label=size
[fork-me]: https://img.shields.io/github/forks/heizelnut/kucka.svg?label=forks
[logo]: https://i.imgur.com/EvqGisdl.png
