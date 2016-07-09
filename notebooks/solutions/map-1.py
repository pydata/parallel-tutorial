# Parallel code

from concurrent.futures import ProcessPoolExecutor
e = ProcessPoolExecutor()

def load_parse_store(fn):
    with open(fn) as f:
        data = [json.loads(line) for line in f]

    df = pd.DataFrame(data)

    out_filename = fn[:-5] + '.h5'
    df.to_hdf(out_filename, '/data')

list(e.map(load_parse_store, filenames))
