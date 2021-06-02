#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


if __name__ == '__main__':
    f = open("good.txt", "r")
    fc = f.read()
    f.close()
    split_regex = re.compile(r'[.|!|?|…]')
    sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(fc)])
    print(sorted(sentences, key = lambda x: x[1]))