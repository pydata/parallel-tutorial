import os
from glob import glob
import pandas as pd
try:
    import ujson as json
except ImportError:
    import json

import dask
import dask.dataframe as dd
import dask.multiprocessing
import os
import sys

WINDOWS = sys.platform.startswith('win')

if WINDOWS:
    dask.set_options(get=dask.threaded.get)
else:
    dask.set_options(get=dask.multiprocessing.get)

here = os.path.dirname(__file__)
os.makedirs(os.path.join(here, 'data', 'minute'), exist_ok=True)

stocks = ['aet', 'afl', 'aig', 'al', 'amgn', 'avy', 'b', 'bwa', 'ge',
          'hal', 'hp', 'hpq', 'ibm', 'jbl', 'jpm', 'luv', 'met', 'pcg',
          'tgt', 'usb', 'xom']

def write_stock(symbol):
    dirname = os.path.join(here, 'data', 'minute', symbol)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        df = dd.demo.daily_stock(symbol, '2010', '2015', freq='120s',
                                 data_source='google')
        names = [str(ts.date()) for ts in df.divisions]
        df.to_csv(os.path.join(here, 'data', 'minute', symbol, '*.csv'),
                  name_function=names.__getitem__)
        print("Finished CSV: %s" % symbol)

for symbol in stocks:
    write_stock(symbol)


def convert_to_json(d):
    filenames = sorted(glob(os.path.join(d, '*')))[-365:]
    outfn = d.replace('minute', 'json') + '.json'
    if os.path.exists(outfn):
        return
    with open(outfn, 'w') as f:
        for fn in filenames:
            df = pd.read_csv(fn)
            for rec in df.to_dict(orient='records'):
                json.dump(rec, f)
                f.write(os.linesep)
    print("Finished JSON: %s" % d.split(os.path.sep)[-1])


js = os.path.join(here, 'data', 'json')
if not os.path.exists(js):
    os.mkdir(js)

directories = sorted(glob(os.path.join(here, 'data', 'minute', '*')))
values = [dask.delayed(convert_to_json)(d) for d in directories]
dask.compute(values)
