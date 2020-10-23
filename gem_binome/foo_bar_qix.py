class FooBarQix(object):

    def __init__(self):
        self.map = {3: "Foo", 5: "Bar", 7: "Qix"}

    def generate(self, number):

        res = ''
        for k, v in self.map.items():
            if number % k == 0:
                res += v

        for char in str(number):
            for k, v in self.map.items():
                if char == str(k):
                    res += v

        if res != '':
            return res

        return str(number)

