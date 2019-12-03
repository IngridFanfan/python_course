#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File -> save with encoding -> UTF-8 without BOM
print('这是中文')
#formatting, placeholder: %d->int, %f->float, %s->string,%x->hex, %%->%
print('Hi, %s, you have $%d.'%('David',10000))

#übung
s1 = 71
s2 = 85
r = (s2 - s1)*100/s1
print(r)
print('Hi, your scores have been imporved in: %s %%' %r)
