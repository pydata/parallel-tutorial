### Parallel code

rdd = sc.parallelize(filenames)
series = rdd.map(lambda fn: pd.read_hdf(fn)['close'])

corr = (series.cartesian(series)
              .filter(lambda ab: not (ab[0] == ab[1]).all())
              .map(lambda ab: ab[0].corr(ab[1]))
              .max())

result = corr
