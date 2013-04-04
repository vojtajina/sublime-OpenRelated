import unittest
from .converter import *


class ConverterTest(unittest.TestCase):

    def test_none_if_not_match(self):
        # should return empty list if given path does not match from pattern
        c = Converter(["^abc", "{1}"])
        self.assertEqual(c.convert("aaa"), [])

    def test_pattern_to_formatter(self):
        # should convert pattern (i.e. */test/*.js) to formatter
        c = Converter([])
        self.assertEqual(c._pattern_to_formatter("*/test.js"), "{0}/test.js")
        self.assertEqual(c._pattern_to_formatter("*/test/*.js"), "{0}/test/{1}.js")

    def test_basic_pattern(self):
        # should allow double patterns
        c = Converter(["*/test/unit/*.spec.coffee", "*/lib/*.js"])
        self.assertEqual(c.convert("/some/test/unit/aaa/b.spec.coffee"), ["/some/lib/aaa/b.js"])
        self.assertEqual(c.convert("/other/lib/abc.js"), ["/other/test/unit/abc.spec.coffee"])

    def test_multiple_patterns(self):
        # should match all patterns
        c = Converter(["*/some/*.js", "*/css/*.css", "*/more/deep/*.yml"])
        self.assertEqual(c.convert("/fake/some/one.js"), \
            ["/fake/css/one.css", "/fake/more/deep/one.yml"])
        self.assertEqual(c.convert("/fake/more/deep/two.yml"), \
            ["/fake/some/two.js", "/fake/css/two.css"])

    def test_right_order_with_multiple(self):
        # should always start on current file, so that you can keep switching between multiple files
        c = Converter(["*/some/*.js", "*/css/*.css", "*/more/deep/*.yml"])
        self.assertEqual(c.convert("/project/css/my.css"), \
            ["/project/more/deep/my.yml", "/project/some/my.js"])

class WindowsConverterTest(unittest.TestCase):

    def test_windows_path(self):
        # should handle backslash
        c = WindowsConverter(["*/functions/*.pm", "*/standard/css/*.css"])
        self.assertEquals(c.convert("C:\\Users\\functions\\admin_open.pm"), \
            ["C:\\Users\\standard\\css\\admin_open.css"])


if __name__ == '__main__':
    unittest.main()
