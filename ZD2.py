#!/usr/bin/env python3
# -*- coding: utf-8 -*

import json


if __name__ == '__main__':
    with open('he4', 'r', encoding='utf-8') as f:
        text = json.load(f)

    word = input("Введите слово:")

    sentences = text.split(".")

    for sentence in sentences:
        if word in sentence:
            print(sentence)
            with open('he5', 'w', encoding='utf-8') as f:
                json.dump(sentence, f, ensure_ascii=False)