import os
import pyspark
from pyspark.sql import SparkSession
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
from pyspark.sql.functions import upper,pandas_udf,PandasUDFType,udf
from pyspark.sql.types import *
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"

# initialization of spark
# master is machine | server allooting
spark_session = SparkSession.builder.master("local").\
        appName("SparkApplication").\
        config("spark.driver.bindAddress","localhost").\
        config("spark.ui.port","4041").\
        getOrCreate()

df = spark_session.createDataFrame(
          [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)],
        ("id", "v"))  # doctest: +SKIP
@pandas_udf("id long, v double", PandasUDFType.GROUPED_MAP)  # doctest: +SKIP
def normalize(pdf):
    v = pdf.v
    return pdf.assign(v=(v - v.mean()) / v.std())
df.groupby("id").apply(normalize).show()  # doctest: +SKIP

# df.groupby("color").apply(g1).show()
# df.show()