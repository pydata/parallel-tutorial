import os
import shutil
from glob import glob
import pandas as pd
import json
from fakestockdata import generate_stocks
from concurrent.futures import ProcessPoolExecutor

here = os.path.dirname(__file__)

data = os.path.join(here, 'data')
if not os.path.exists(data):
    os.mkdir(data)


minute = os.path.join(data, 'minute')
if not os.path.exists(minute):
    os.mkdir(minute)
    generate_stocks(freq=pd.Timedelta(seconds=60),
                    start=pd.Timestamp('2010-01-01'),
                    directory=minute)


def convert_to_json(d):
    filenames = sorted(glob(os.path.join(d, '*')))[-365:]
    with open(d.replace('minute', 'json') + '.json', 'w') as f:
        for fn in filenames:
            df = pd.read_csv(fn)
            for rec in df.to_dict(orient='records'):
                json.dump(rec, f)
                f.write(os.linesep)
    print("Finished JSON: %s" % d)


js = os.path.join(data, 'json')
if not os.path.exists(js):
    os.mkdir(js)
    directories = sorted(glob(os.path.join(minute, '*')))

    e = ProcessPoolExecutor()
    list(e.map(convert_to_json, directories))
