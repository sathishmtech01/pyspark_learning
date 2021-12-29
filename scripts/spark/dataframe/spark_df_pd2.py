import os
import pyspark
from pyspark.sql import SparkSession
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
from pyspark.sql.functions import upper,pandas_udf
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"

# initialization of spark
# master is machine | server allooting
spark_session = SparkSession.builder.master("local").\
        appName("SparkApplication").\
        config("spark.driver.bindAddress","localhost").\
        config("spark.ui.port","4041").\
        getOrCreate()


# creating df on top of pandas dataframe
pandas_df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [2., 3., 4.],
    'c': ['string1', 'string2', 'string3'],
    'd': [date(2000, 1, 1), date(2000, 2, 1), date(2000, 3, 1)],
    'e': [datetime(2000, 1, 1, 12, 0), datetime(2000, 1, 2, 12, 0), datetime(2000, 1, 3, 12, 0)]
})
df = spark_session.createDataFrame(pandas_df)



print(df)
df.show()
df.show(1)
df.show(1, vertical=True)

# view a selected column
df.select(df.c).show()

# create new column instance
df = df.withColumn('upper_c', upper(df.c))
df.show()

# subset of data/ filter
df.filter(df.a == 1).show()


