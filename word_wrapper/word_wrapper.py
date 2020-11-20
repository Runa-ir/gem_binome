"""WordWrapper class"""
import textwrap

class WordWrapper(object):

    def wrap_w_standard_lib(self, words, column_number):
        return textwrap.fill(words, column_number)

    def wrap(self, words, column_number):
        if len(words) > column_number:
            i = 0
            offset = 0
            length = len(words)
            composition = ""
            while length > 0:
                index_of_breaking_space, offset = self.my_rindex(words, 0, column_number)

                string_to_add = words[0:index_of_breaking_space + offset]
                if offset:
                    string_to_add = string_to_add.rstrip()
                composition = composition + string_to_add + '\n'
                length -= index_of_breaking_space
                words = words[index_of_breaking_space + offset:]

            return composition[:len(composition)-len('\n')]

        return words


    def my_rindex(self, words, index, column_number):
        try:
            return words.rindex(" ", index + 1, column_number + 1), 1
        except ValueError:
            return column_number, 0
