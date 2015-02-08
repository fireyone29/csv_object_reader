csv_object_reader
=================

.. image:: https://travis-ci.org/fireyone29/csv_object_reader.svg?branch=develop
    :target: https://travis-ci.org/fireyone29/csv_object_reader


.. image:: https://coveralls.io/repos/fireyone29/csv_object_reader/badge.svg?branch=develop
  :target: https://coveralls.io/r/fireyone29/csv_object_reader?branch=develop


A simple module which mimics the `reader` classes from python's csv
module but returns an object whose attributes are the members of the
header instead of a list or dict.

The ObjectReader also provides a way to make fields required to be
present and required to be not empty.

TODO
----

1) Add support for headers specified multiple times
2) Add more filtering support
