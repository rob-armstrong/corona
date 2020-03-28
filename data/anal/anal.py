#!/usr/bin/env python

import datetime
import csv
data_dir = "../nytimes/covid-19-data"

f1 = open(data_dir+"/"+"us-counties.csv","r")
counties = csv.DictReader(f1)

f2 = open(data_dir+"/"+"us-states.csv")
states = csv.DictReader(f2)


alameda = 1
california = 06
def state_fips(state,county):
    return state*1000+county
ac = alameda_california = state_fips(california,alameda)

for r in counties:
    if (r["state"] != "California") or (r["county"] != "Alameda"):
        continue
    print r["date"]
