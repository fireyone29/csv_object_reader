csv_object_reader
=================

A simple module which mimics the `reader` classes from python's csv
module but returns an object whose attributes are the members of the
header instead of a list or dict.

The ObjectReader also provides a way to make fields required to be
present and required to be not empty.
