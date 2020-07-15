#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Tommy http://tommy.net.cn/

import platform


def main():
    message()


def message():
    print('The python version is {}'.format(platform.python_version()))


if __name__ == '__main__':
    main()
