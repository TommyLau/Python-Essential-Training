#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020 Tommy http://tommy.net.cn/


def is_prime(n):
    if n <= 1:
        return False

    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


n = 7

if is_prime(n):
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')
