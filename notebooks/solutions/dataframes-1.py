df = dd.read_csv('../data/minute/aig/2012-*.csv', parse_dates=['timestamp'])

# what was the max value?
max_value = df.high.max().compute()

# when did this happen?
max_value_date = df[df.high == max_value].timestamp.dt.date.compute()

# all the dates
df_all = dd.read_csv('../data/minute/aig/*.csv', parse_dates=['timestamp'])
df_all[df_all.high == max_value].timestamp.dt.date.compute()

# reindex
df = df.set_index('timestamp', sorted=True)

# resample by hour:
df.close.resample('1h').mean().compute()
