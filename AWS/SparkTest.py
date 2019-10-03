import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf,current_timestamp, expr
from pyspark.sql.types import StringType
from pyspark.sql.functions import lit
import time
import boto3

sc = SparkContext()
spark=SparkSession(SparkContext)

spark.sql("select from_utc_timestamp('2018-04-15 23:23:15.097','America/New_York')").show()