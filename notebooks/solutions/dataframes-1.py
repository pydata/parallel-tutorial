# what was the max value?
max_value = df.high.max().compute()

# when did this happen?
max_value_date = df[df.high == max_value].timestamp.dt.date.compute()

# all the dates
df_all = dd.read_csv('../data/minute/aa/*.csv', parse_dates=['timestamp'])
df_all[df_all.high == max_value].timestamp.dt.date.compute()

# reindex
df = df.set_index('timestamp', sorted=True)

# resample by hour:
df.close.resample(pd.Timedelta(hours=1)).mean().compute()

# resample by week (this will fail):
df.close.resample(pd.Timedelta(weeks=1)).mean().compute()
