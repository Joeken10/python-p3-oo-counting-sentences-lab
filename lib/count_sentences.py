#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self._value = value
        print(f"Initialized MyString with value: '{self._value}'")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            raise ValueError("Value must be a string")
        self._value = val
        print(f"Value set to: '{self._value}'")

    def is_sentence(self):
        '''Returns True if value ends with a period and False otherwise.'''
        result = self._value.endswith('.')
        print(f"Checking if value ends with a period: {result}")
        return result

    def is_question(self):
        '''Returns True if value ends with a question mark and False otherwise.'''
        result = self._value.endswith('?')
        print(f"Checking if value ends with a question mark: {result}")
        return result

    def is_exclamation(self):
        '''Returns True if value ends with an exclamation mark and False otherwise.'''
        result = self._value.endswith('!')
        print(f"Checking if value ends with an exclamation mark: {result}")
        return result

    def count_sentences(self):
        '''Returns the number of sentences in the value.'''
        sentences = re.split(r'[.!?]+', self._value)
       
        sentence_count = len([s for s in sentences if s.strip()])
        print(f"Counted sentences: {sentence_count}")
        return sentence_count


