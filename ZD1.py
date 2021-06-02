#!/usr/bin/env python3
# -*- coding: utf-8 -*

if __name__ == '__main__':
    with open('good.txt', 'r') as f:
        text = f.read()

    word = input("Введите слово:")

    sentences = text.split(".")

    for sentence in sentences:
        if word in sentence:
            print(sentence)