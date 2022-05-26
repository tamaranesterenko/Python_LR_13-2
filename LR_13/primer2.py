#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process


def func():
    print("Hello from main Process")
    proc = Process(target=func)
    proc.start()
    print("Goodbye")

