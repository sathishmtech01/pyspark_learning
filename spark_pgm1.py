from random import random
import os
from pyspark.sql import SparkSession
os.environ['SPARK_HOME'] = "/home/csk/sparkscala/spark-2.4.0-bin-hadoop2.6/"

def create_spark_session(app_name="SparkApplication"):
    spark_session = SparkSession.builder.master("local").\
        appName("sparkapp").\
        config("spark.driver.bindAddress","localhost").\
        config("spark.ui.port","4041").\
        getOrCreate()

    spark_session.sparkContext.setLogLevel("WARN")

    return spark_session


def main():
    session = create_spark_session()
    sc = session.sparkContext

    total_points = 1000000
    numbers = sc.range(0, total_points)
    points = numbers.map(lambda n: (random(), random()))
    circle = points.filter(lambda p: (p[0] * p[0] + p[1] * p[1]))
    num_inside = circle.count()
    print("Pi = ", 4 * num_inside / total_points)
    input()


if __name__ == '__main__':
    main()
