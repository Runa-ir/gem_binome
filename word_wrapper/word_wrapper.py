"""WordWrapper class"""
import textwrap

class WordWrapper(object):

    def wrap_w_standard_lib(self, words, column_number):
        return textwrap.fill(words, column_number)

    def wrap(self, words, column_number):
        if len(words) > column_number:
            i = 0
            length = len(words)
            composition = ""
            while length > 0:
                index_of_breaking_space, offset = self.my_rindex(words, column_number, i)

                i += index_of_breaking_space
                composition = composition + words[i - index_of_breaking_space + offset:i+offset] + '\n'
                length -= index_of_breaking_space

            return composition[:len(composition)-len('\n')]

        return words


    def my_rindex(self, words, column_number, index):
        try:
            return words.rindex(" ", index+1, column_number + 1), 0
        except ValueError:
            return column_number, 1
