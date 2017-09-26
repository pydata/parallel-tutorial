df = df[df.fare_amount > 0]
df['tip_fraction'] = df.tip_amount / df.fare_amount
df.tip_fraction.groupby(df.passenger_count).mean()
