"""Filter Objects"""

import re


class Filter(object):
    """Basic Filter, uses == to compare values."""
    def __init__(self, field, value=None, invert=False, missing_is_pass=False):
        """
        :param field: name of field to filter on
        :param value: required value of the specified field, if None
            checks that the field exists
        :param invert: invert the results of the filter. Ignored if
            value is None.
        :param missing_is_pass: if True and field is not present,
            pass this entry instead of failing it (the default).
            Ignored if value is None.
        """
        if not isinstance(field, str):
            raise TypeError
        self._field = field
        self._value = value
        self._invert = invert
        self._missing_is_pass = missing_is_pass

    def _compare(self, value):
        """Compare the expected value to the present value with ==."""
        return self._value == value

    def test(self, entry):
        """
        Test the provided entry against this filer.

        :param entry: entry to test against the filter.
        :returns: True if the entry passes the filter, otherwise False.
        """
        value = None
        missing = False
        try:
            value = getattr(entry, self._field)
        except AttributeError:
            missing = True
        if missing:
            if self._value is None:
                return False
            else:
                return self._missing_is_pass
        elif self._value is None:
            return True
        else:
            return self._compare(value) ^ self._invert


class RegexFilter(Filter):
    """Filter which uses regex match to compare values."""
    def __init__(self, field, value=None, invert=False, missing_is_pass=False):
        super(RegexFilter, self).__init__(field, value, invert,
                                          missing_is_pass)
        if self._value is not None:
            self._regex = re.compile(self._value)

    def _compare(self, value):
        """Treat the expected value as a regex expression to match."""
        return bool(self._regex.match(str(value)))
