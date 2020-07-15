#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Tommy http://tommy.net.cn/

# Fibonacci number
# https://en.wikipedia.org/wiki/Fibonacci_number

a, b = 0, 1

while b < 1000:
    print(b, end=' ', flush=True)
    a, b = b, a + b

# New line for ending
print()
