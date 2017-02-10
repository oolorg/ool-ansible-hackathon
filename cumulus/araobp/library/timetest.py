#!/usr/bin/python

import datetime
import json

date = str(datetime.datetime.now())
print json.dumps({
    "changed": False,
    "time": date
})
