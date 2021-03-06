# Python CLI Game Engine
<p align="center">
    <img src="https://img.shields.io/github/license/SantaSpeen/Python-CLI-Game-Engine?style=for-the-badge" alt="license" title="license: MIT">
    <img src="https://img.shields.io/github/issues/SantaSpeen/Python-CLI-Game-Engine?style=for-the-badge" alt="issues">
    <img src="./assets/magic_logo.svg" alt="magic" loading="lazy">
    <br/>
    <img src="./assets/preview.png" alt="preview" loading="lazy">
</p>

## Localizations

* English: [here](./README.md)
* Russian: You are here.

## О проекте

* ### Пока что проект не готов

* В качестве примера будет игра "змейка".

## TODO:

- [x] Ядро (Основа)
- [ ] Получение пикселей вокруг определённой точки 
- [ ] Динамическая система подстройки FPS
- [ ] Игра "Змейка"

## Системные требования

1. Система UNIX: MacOS, Linux, и тому подобное :trollface:
2. Python3.10 и выше
3. Библиотеки: `pynput`, `click`

## Как запустить:

* #### Debian based:
```shell
# Shell:

$ sudo apt install git
    # * Installing git VSC... *
$ python3.10 -m pip install -U pip
    # * Update pip... *
$ git clone https://github.com/SantaSpeen/CLI-Snake-on-Python.git
    # * Dowloading... *
$ cd CLI-Snake-on-Python/src/
    # Change dir
$ python3.10 -m pip install -r requirements.txt
    # * Installing requirements... *
$ python3.10 main.py start
    # * Play now! *
```

* #### MacOS:

```shell
# Shell:

$ brew install git
    # * Installing git VSC... *
$ python3.10 -m pip install -U pip
    # * Update pip... *
$ git clone https://github.com/SantaSpeen/CLI-Snake-on-Python.git
    # * Dowloading... *
$ cd CLI-Snake-on-Python/src/
    # Change dir
$ python3.10 -m pip install -r requirements.txt
    # * Installing requirements... *
$ python3.10 main.py start
    # * Нужно разрешить считывание клавиш отовсюду в настройках! *
    # * Разрешаем и запускаем вновь * 
```

## Ссылки

* [Мой Telegram](https://t.me/SantaSpeen "SantaSpeen"): https://t.me/SantaSpeen

Используемые библиотеки: 

* [pynput](https://github.com/moses-palmer/pynput "pynput")
* [click](https://click.palletsprojects.com/ "click")
