"""WordWrapper class"""

class WordWrapper(object):

    def wrap(self, words, column_number):
        if len(words) > column_number:
            try:
                index_of_breaking_space = words.rindex(" ", 0, column_number + 1)
            except ValueError:
                i = 0
                length = len(words)
                composition = ""
                while length > 0:
                    i += column_number
                    composition = composition + words[i-column_number:i] + '\n'
                    length -= column_number

                return composition[:len(composition)-len('\n')]

            return words[:index_of_breaking_space] + '\n' + words[index_of_breaking_space + 1:]
        return words