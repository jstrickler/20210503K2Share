#!/usr/bin/env python
# (c) 2017 CJ Associates
#
import csv
import os
from django.conf import settings

airports_file_path = os.path.join(str(settings.ROOT_DIR), 'airport_boardings.csv')

with open(airports_file_path) as airports_in:
    rdr = csv.reader(airports_in)
    next(rdr)  # skip header row
    AIRPORTS = sorted((r[1], r[0]) for r in rdr)

