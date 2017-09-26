(df.filter(df.fare_amount > 0)
   .withColumn('tip_fraction', df.tip_amount / df.fare_amount)
   .groupby('passenger_count').agg({'tip_fraction': 'avg'})).collect()
