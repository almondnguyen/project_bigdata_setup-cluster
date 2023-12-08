from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import col, when, mean



spark = SparkSession.builder \
    .appName("MyApp") \
    .master("spark://34.142.194.212:7077") \
    .config("spark.cores.max", "4")\
    .config("spark.jars", "/opt/spark/jars/gcs-connector-latest-hadoop2.jar") \
    .getOrCreate()
spark.conf.set("google.cloud.auth.service.account.json.keyfile","/opt/spark/lucky-wall-393304-2a6a3df38253.json")
# spark.conf.set("spark.executor.cores", "2")

spark._jsc.hadoopConfiguration().set('fs.gs.impl', 'com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem')
spark._jsc.hadoopConfiguration().set('fs.gs.auth.service.account.enable', 'true')
def data_cleansing(i):
    path=f"gs://it4043e-it5384/it4043e/it4043e_group8_problem3/raw/R_{i}/kols_table.csv"
    df = spark.read.csv(path, header=True, inferSchema=True)
    non_empty_columns = [c for c in df.columns if df.filter(df[c].isNotNull()).count() > 0]
    df = df.select(*non_empty_columns)
    selected_columns = df.columns[6:13]  
    for column in selected_columns:
        mean_value = df.select(mean(col(column))).collect()[0][0]
        df = df.withColumn(column, when(col(column).isNull(), mean_value).otherwise(col(column)))
        df = df.withColumn(column, col(column).cast(IntegerType()))
    df.show()

data_cleansing(1)

spark.stop()