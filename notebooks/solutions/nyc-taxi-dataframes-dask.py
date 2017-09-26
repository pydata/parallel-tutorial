df = df[df.fare_amount > 0]
df['tip_fraction'] = df.tip_amount / df.fare_amount
df.groupby(df.passenger_count).tip_fraction.mean().compute()
