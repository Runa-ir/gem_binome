import unittest


class CLIParser(object):

    def __init__(self, schema):
        self.flags = {}
        self.schema = schema

    def set_cli(self, cli):
        parsed_cli = []
        i = 0
        block = ""
        for char in cli:
            if char == "-" and not cli[i+1].isnumeric():
                parsed_cli.append(block)
                i += 1
                block = ""
                continue
            block += char
            i += 1
        parsed_cli.append(block)

        for item in parsed_cli:
            split_flag = item.split(" ")
            flag = split_flag[0]
            value = True
            if len(split_flag) > 1:
                if split_flag[1]:
                    value = split_flag[1]

            self.flags[flag] = value

    def evaluate_flag(self, flag):
        flag_type = self.schema[flag]

        if type(flag_type) == list:
            flag_type = flag_type[0]

            collection = []
            for val in self.flags[flag].split(","):
                collection.append(self.cast(val, flag_type))
            return collection

        if flag not in self.flags.keys():
            return False

        return self.cast(self.flags[flag], flag_type)

    def cast(self, value, new_type):

        return new_type(value)


class TestCLIParser(unittest.TestCase):

    def test_should_return_true_when_single_boolean_flag(self):
        cli_parser = CLIParser({"l": bool})
        cli_parser.set_cli("-l")
        self.assertEqual(True, cli_parser.evaluate_flag("l"))

    def test_should_return_false_when_no_single_boolean(self):
        cli_parser = CLIParser({"l": bool})
        cli_parser.set_cli("")
        self.assertEqual(False, cli_parser.evaluate_flag("l"))

    def test_should_return_integer_when_single_integer_flag(self):
        cli_parser = CLIParser({"p": int})
        cli_parser.set_cli("-p 8080")
        self.assertEqual(8080, cli_parser.evaluate_flag("p"))

    def test_should_return_string_when_single_string_flag(self):
        cli_parser = CLIParser({"d": str})
        cli_parser.set_cli("-d /usr/logs")
        self.assertEqual("/usr/logs", cli_parser.evaluate_flag("d"))

    def test_should_parse_several_different_flags_type_at_once(self):
        cli_parser = CLIParser({"l": bool, "p": int, "d": str})
        cli_parser.set_cli("-l -p 8080 -d /usr/logs")
        self.assertEqual(True, cli_parser.evaluate_flag("l"))
        self.assertEqual(8080, cli_parser.evaluate_flag("p"))
        self.assertEqual("/usr/logs", cli_parser.evaluate_flag("d"))

    def test_should_return_collection_when_single_collection_flag(self):
        cli_parser = CLIParser({"g": [str]})
        cli_parser.set_cli("-g this,is,a,list")
        self.assertEqual(["this", "is", "a", "list"], cli_parser.evaluate_flag("g"))

    def test_cli_is_split_correctly_with_minus_in_values(self):
        cli_parser = CLIParser({"d": int})
        cli_parser.set_cli("-d -3")
        self.assertEqual(-3, cli_parser.evaluate_flag("d"))


    def test_should_return_multiple_collections_when_multiple_collection_flag(self):
        cli_parser = CLIParser({"g": [str], "d": [int]})
        cli_parser.set_cli("-g this,is,a,list -d 1,2,-3,5")
        self.assertEqual(["this", "is", "a", "list"], cli_parser.evaluate_flag("g"))
        self.assertEqual([1, 2, -3, 5], cli_parser.evaluate_flag("d"))


if __name__ == '__main__':
    unittest.main()
