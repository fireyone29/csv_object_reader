"""
Utility for parsing csv files.

This module offers more options for restricting and filtering the file
contents than python's built in cvs module.
"""


import csv
from collections import namedtuple
import logging
LOG = logging.getLogger(__name__)
LOG.addHandler(logging.NullHandler())


class ObjectReader(object):
    """Returns an objects for each record in a csv file"""
    def __init__(self, raw_file, required_items=None, required_groups=None,
                 required_not_empty=True):
        self.__stream = csv.reader(raw_file)
        header = next(self.__stream, None)
        if not header:
            raise ValueError("Empty header")
        self.line_type = namedtuple("line_type", header)
        fields = set(self.line_type._fields)
        if required_items:
            missing = set(required_items) - fields
            if missing:
                raise AttributeError(
                    "Required field(s) %r missing in header." %
                    (missing))
        if required_groups:
            for group in required_groups:
                if not set(group) & fields:
                    raise AttributeError(
                        "Header must contain at least one of %r" %
                        (group))
        self.__not_empty = required_not_empty
        self.__required_items = required_items
        self.__required_gruops = required_groups

    def __iter__(self):
        for line in self.__stream:
            try:
                item = self.line_type(*line)
            except TypeError:
                LOG.warning("Ignoring entry not matching header: %r", line)
            else:
                if self.__not_empty:
                    missing = []
                    if self.__required_items:
                        missing = [field for field in self.__required_items
                                   if not getattr(item, field)]
                    if self.__required_gruops:
                        for group in self.__required_gruops:
                            empty = True
                            for member in group:
                                if getattr(item, member, None):
                                    empty = False
                                    break
                            if empty:
                                missing.append(group)
                    if missing:
                        LOG.debug("Ignoring entry with empty field(s) %r: %r",
                                  missing, item)
                        continue
                yield item
