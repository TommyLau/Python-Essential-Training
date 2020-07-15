#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Tommy http://tommy.net.cn/


class Mouse:
    def squeak(self):
        print('Squeak.')

    def run(self):
        print('Runs like a rat.')


def main():
    mickey = Mouse()
    mickey.squeak()
    mickey.run()


if __name__ == '__main__':
    main()
