#!/usr/bin/env python3

import pytest
from count_sentences import MyString

class TestMyString:
    def test_value_string(self):
        '''Raises ValueError if the value is not a string.'''
        try:
            string = MyString()
            string.value = 123  # This should raise ValueError
        except ValueError as e:
            print(f"Caught expected ValueError: {e}")
            assert str(e) == "Value must be a string"

    def test_is_sentence(self):
        '''Returns True if value ends with a period and False otherwise.'''
        s1 = MyString("It's me.")
        s2 = MyString("It's me!")
        print(f"'{s1.value}' ends with a period: {s1.is_sentence()}")
        print(f"'{s2.value}' ends with a period: {s2.is_sentence()}")
        assert s1.is_sentence() == True
        assert s2.is_sentence() == False

    def test_is_question(self):
        '''Returns True if value ends with a question mark and False otherwise.'''
        s1 = MyString("Is this a question?")
        s2 = MyString("No question here.")
        print(f"'{s1.value}' ends with a question mark: {s1.is_question()}")
        print(f"'{s2.value}' ends with a question mark: {s2.is_question()}")
        assert s1.is_question() == True
        assert s2.is_question() == False

    def test_is_exclamation(self):
        '''Returns True if value ends with an exclamation mark and False otherwise.'''
        s1 = MyString("Wow!")
        s2 = MyString("Not exciting.")
        print(f"'{s1.value}' ends with an exclamation mark: {s1.is_exclamation()}")
        print(f"'{s2.value}' ends with an exclamation mark: {s2.is_exclamation()}")
        assert s1.is_exclamation() == True
        assert s2.is_exclamation() == False

    def test_count_sentences(self):
        '''Returns the number of sentences in the value.'''
        s1 = MyString("one. two. three?")
        s2 = MyString("This is a sentence. This is another sentence! And a question?")
        s3 = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
        print(f"Sentence count for '{s1.value}': {s1.count_sentences()}")
        print(f"Sentence count for '{s2.value}': {s2.count_sentences()}")
        print(f"Sentence count for '{s3.value}': {s3.count_sentences()}")
        assert s1.count_sentences() == 3
        assert s2.count_sentences() == 3
        assert s3.count_sentences() == 4
