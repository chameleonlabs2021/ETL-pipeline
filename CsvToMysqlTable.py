
import mysql.connector
import pandas as pd
from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .config("spark.jars", "/home/ubuntu/mysql-connector-java-8.0.22.jar")\
    .master("local[*]")\
    .appName("pivot and unpivot")\
    .getOrCreate()


df = spark.read.option("header",True) \
     .csv("/home/ubuntu/source/src.csv")


df.write.jdbc(url="jdbc:mysql://localhost:3306/staging"
                  "?user=etl-user&password=password",
              table="src",
              mode="append",
              properties={"driver": 'com.mysql.jdbc.Driver'})