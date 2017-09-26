
# Use map or submit with the `read_row_group` function
# on each of the row groups to get a list of futures of Pandas dataframes

futures = client.map(read_row_group, pf.row_groups)

# How many passengers rode in cab rides in 2016 total?
# (answer provided for this question)

def f(df):
    return df.passenger_count.sum()

counts = client.map(f, futures)
total = client.submit(sum, counts)
total_count = total.result()
print("Number of total passengers:", total_count)


# What was the average number of passengers over all rides?

def f(df):
    return df.passenger_count.sum(), len(df)

intermediates = client.map(f, futures)

def accumulate(results):
    counts = 0
    lengths = 0
    for count, len in results:
        counts += count
        lengths += len
    return counts / lengths

total = client.submit(accumulate, intermediates)
avg = total.result()
print("Average passenger count:", total_count)


# How many rides were there for each passenger count?

def f(df):
    return df.passenger_count.value_counts()

counts = client.map(f, futures)

import pandas as pd

def accumulate(results):
    result = pd.concat(results)
    return result.groupby(result.index).sum()

total = client.submit(accumulate, counts)
value_counts = total.result()

print("Number of rides per passenger count:", value_counts)
