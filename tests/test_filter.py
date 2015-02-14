import unittest
from collections import namedtuple
from csv_object_reader import Filter, RegexFilter


class TestFilterValueNone(unittest.TestCase):
    def setUp(self):
        super(TestFilterValueNone, self).setUp()
        self.field = "field1"
        self.filter1 = Filter(self.field)

    def test_field_present(self):
        Entry = namedtuple("Entry", [self.field])
        entry = Entry("a")
        self.assertTrue(self.filter1.test(entry))

    def test_field_missing(self):
        Entry = namedtuple("Entry", [self.field + "a"])
        entry = Entry("a")
        self.assertFalse(self.filter1.test(entry))


class TestFilterValueNoneInvert(TestFilterValueNone):
    def setUp(self):
        super(TestFilterValueNoneInvert, self).setUp()
        self.filter1 = Filter(self.field, invert=True)


class TestFilterValueNoneMissingPass(TestFilterValueNone):
    def setUp(self):
        super(TestFilterValueNoneMissingPass, self).setUp()
        self.filter1 = Filter(self.field, missing_is_pass=True)


class TestRegexFilterValueNone(TestFilterValueNone):
    def setUp(self):
        super(TestRegexFilterValueNone, self).setUp()
        self.filter1 = RegexFilter(self.field)


class TestRegexFilterValueNonePassMissing(TestFilterValueNone):
    def setUp(self):
        super(TestRegexFilterValueNonePassMissing, self).setUp()
        self.filter1 = RegexFilter(self.field, missing_is_pass=True)


class TestRegexFilterValueNoneInvert(TestFilterValueNone):
    def setUp(self):
        super(TestRegexFilterValueNoneInvert, self).setUp()
        self.filter1 = RegexFilter(self.field, invert=True)


class TestFilter(unittest.TestCase):
    def setUp(self):
        super(TestFilter, self).setUp()
        self.field = "field1"
        self.pass_value = 2
        self.fail_value = "2"
        self.filter1 = Filter(self.field, self.pass_value)

    def test_pass(self):
        Entry = namedtuple("Entry", [self.field])
        entry = Entry(self.pass_value)
        self.assertTrue(self.filter1.test(entry))

    def test_fail(self):
        Entry = namedtuple("Entry", [self.field])
        entry = Entry(self.fail_value)
        self.assertFalse(self.filter1.test(entry))

    def test_field_missing(self):
        Entry = namedtuple("Entry", [self.field + "a"])
        entry = Entry(self.pass_value)
        self.assertFalse(self.filter1.test(entry))


class TestFilterInvert(TestFilter):
    def setUp(self):
        super(TestFilterInvert, self).setUp()
        self.pass_value = "2"
        self.fail_value = 2
        self.filter1 = Filter(self.field, self.fail_value, invert=True)


class TestFilterMissingPass(TestFilter):
    def setUp(self):
        super(TestFilterMissingPass, self).setUp()
        self.filter1 = Filter(self.field, self.pass_value,
                              missing_is_pass=True)

    def test_field_missing(self):
        Entry = namedtuple("Entry", [self.field + "a"])
        entry = Entry(self.pass_value)
        self.assertTrue(self.filter1.test(entry))


class TestRegexFilterInvalidPattern(unittest.TestCase):
    def test_invalid_regex_pattern(self):
        with self.assertRaises(TypeError):
            RegexFilter("x", 2)

    def test_invalid_field(self):
        with self.assertRaises(TypeError):
            RegexFilter(2, "2")


class TestRegexFilter(TestFilter):
    def setUp(self):
        super(TestRegexFilter, self).setUp()
        self.pass_value = "val1"
        self.fail_value = "1val"
        self.pattern = "val[0-9]"
        self.filter1 = RegexFilter(self.field, self.pattern)


class TestRegexFilterInvert(TestRegexFilter):
    def setUp(self):
        super(TestRegexFilterInvert, self).setUp()
        self.pattern = "[0-9]val"
        self.filter1 = RegexFilter(self.field, self.pattern, invert=True)


class TestRegexFilterMissingPass(TestRegexFilter):
    def setUp(self):
        super(TestRegexFilterMissingPass, self).setUp()
        self.filter1 = RegexFilter(self.field, self.pattern,
                                   missing_is_pass=True)

    def test_field_missing(self):
        Entry = namedtuple("Entry", [self.field + "a"])
        entry = Entry(self.pass_value)
        self.assertTrue(self.filter1.test(entry))
