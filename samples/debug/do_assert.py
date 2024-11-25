#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def foo(s):
    n = int(s)
    # 条件必须为真，否则异常
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')


main()
