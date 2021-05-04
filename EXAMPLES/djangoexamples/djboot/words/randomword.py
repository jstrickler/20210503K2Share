#!/usr/bin/env python
# (c) 2017 CJ Associates
#
import random
import os
from django.conf import settings

class RandomWord():

    def __init__(self):
        words_file_path = os.path.join(str(settings.ROOT_DIR), 'words.txt')
        with open(words_file_path) as words_in:
            self._words = [w.rstrip() for w in words_in]


    def __call__(self):
        return random.choice(self._words)


    def get_random_word_list(self, count):
        return random.sample(self._words, count)
