=====
Usage
=====

To use csv_object_reader in a project::

    import csv_object_reader
    with open("somefile.csv") as f:
        reader = csv_object_reader.ObjectReader(f)
        for line in reader:
            print(line)
