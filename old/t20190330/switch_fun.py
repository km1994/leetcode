#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: switch_fun.py
@time: 2019/3/30 22:40
@desc:
'''
def success(msg):
    print(msg)

def debug(msg):
    print(msg)

def error(msg):
    print(msg)

def warning(msg):
    print(msg)

def other(msg):
    print(msg)

def notify_result(num, msg):
    numbers = {
        0 : success,
        1 : debug,
        2 : warning,
        3 : error
    }

    method = numbers.get(num, other)
    if method:
        method(msg)

if __name__ == "__main__":
    notify_result(0, "success")
    # notify_result(1, "debug")
    # notify_result(2, "warning")
    # notify_result(3, "error")
    # notify_result(4, "other")