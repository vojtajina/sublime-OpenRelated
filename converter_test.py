import unittest
from converter import Converter


class ConverterTest(unittest.TestCase):

    def test_none_if_not_match(self):
        # should return None if given path does not match from pattern
        c = Converter("^abc", "{1}")
        self.assertEqual(c.convert("aaa"), None)

    def test_convert_basic(self):
        # should convert basic expression
        c = Converter("*/test/*Spec.js", "{0}/src/{1}.js")
        self.assertEqual(c.convert("some/path/test/oneSpec.js"), "some/path/src/one.js")

    def test_pattern_to_formatter(self):
        # should convert pattern (i.e. */test/*.js) to formatter
        c = Converter("", "")
        self.assertEqual(c._pattern_to_formatter("*/test.js"), "{0}/test.js")
        self.assertEqual(c._pattern_to_formatter("*/test/*.js"), "{0}/test/{1}.js")

    def test_double_pattern(self):
        # should allow double patterns
        c = Converter("*/test/unit/*.spec.coffee", "*/lib/*.js")
        self.assertEqual(c.convert("/some/test/unit/aaa/b.spec.coffee"), "/some/lib/aaa/b.js")
        self.assertEqual(c.convert("/other/lib/abc.js"), "/other/test/unit/abc.spec.coffee")

if __name__ == '__main__':
    unittest.main()
