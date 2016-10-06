from pyspark import SparkContext
sc = SparkContext('local[4]')

cv_rdd = sc.parallelize(cv_splits)
param_rdd = sc.parallelize(list(param_samples))

rdd = param_rdd.cartesian(cv_rdd)
results = rdd.map(lambda tup: evaluate_one(SVC, tup[0], tup[1]))

results = results.collect()
