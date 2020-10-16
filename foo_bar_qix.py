class FooBarQix(object):

    def __init__(self):
        self.map = {3: "Foo", 5: "Bar", 7: "Qix"}

    def generate(self, number):

        for k, v in self.map.items():
            if number % k == 0:
                return v
        return str(number)