http://spark.apache.org/docs/latest/api/python/pyspark.html

data sets:
https://snap.stanford.edu/data/web-Amazon.html


Error: spark_df_pd2
Traceback (most recent call last):
  File "/home/csk/PycharmProjects/git/pyspark_learning/scripts/spark/dataframe/spark_df_pd2.py", line 50, in <module>
    def pandas_plus_one(series: pd.Series) -> pd.Series:
  File "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/python/lib/pyspark.zip/pyspark/sql/udf.py", line 47, in _create_udf
  File "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/python/lib/pyspark.zip/pyspark/sql/utils.py", line 149, in require_minimum_pyarrow_version
ImportError: PyArrow >= 0.8.0 must be installed; however, it was not found.

csk@csk-ai-revolution:~/PycharmProjects/git/pyspark_learning$ /home/csk/anaconda/envs/face/bin/pip3 install PyArrow
Collecting PyArrow
  Using cached https://files.pythonhosted.org/packages/38/c6/97a4133eea642155e7a73cb946d889cadc461a1e6b93f5627af9fdd7b3f3/pyarrow-6.0.1.tar.gz
  Could not find a version that satisfies the requirement numpy==1.21.3 (from versions: 1.11.3, 1.12.0, 1.12.1, 1.13.0rc1, 1.13.0rc2, 1.13.0, 1.13.1, 1.13.3, 1.14.0rc1, 1.14.0, 1.14.1, 1.14.2, 1.14.3, 1.14.4, 1.14.5, 1.14.6, 1.15.0rc1, 1.15.0rc2, 1.15.0, 1.15.1, 1.15.2, 1.15.3, 1.15.4, 1.16.0rc1, 1.16.0rc2, 1.16.0, 1.16.1, 1.16.2, 1.16.3, 1.16.4, 1.16.5, 1.16.6, 1.17.0rc1, 1.17.0rc2, 1.17.0, 1.17.1, 1.17.2, 1.17.3, 1.17.4, 1.17.5, 1.18.0rc1, 1.18.0, 1.18.1, 1.18.2, 1.18.3, 1.18.4, 1.18.5, 1.19.0rc1, 1.19.0rc2, 1.19.0, 1.19.1, 1.19.2, 1.19.3, 1.19.4, 1.19.5)
No matching distribution found for numpy==1.21.3

/home/csk/anaconda/envs/face/bin/pip install --upgrade pip
/home/csk/anaconda/envs/face/bin/pip install pyarrow


Degraded because - Caused by: java.lang.IllegalArgumentException pandas_udf

https://stackoverflow.com/questions/60306633/pyspark-pandas-udfs-java-lang-illegalargumentexception-error

 /home/csk/anaconda/envs/face/bin/pip install pyarrow==0.14