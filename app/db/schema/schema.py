from pyspark.sql.types import StructType, StructField, StringType, TimestampType , LongType

def create_schema():
    schema = StructType([
        StructField("traceId", StringType(), True),
        # StructField("createdTime", TimestampType(), True),
        StructField("logData", StringType(), True),
        # StructField("traceData", TimestampType(), True),
        # StructField("serviceName", StringType(), True),
        # StructField("startUnixNanoTime", LongType, True),
        # StructField("endUnixNanoTime", LongType, True),
        # StructField("duration", LongType, True),
        # StructField("requestURI", StringType(), True),
        # StructField("requestMethod", StringType(), True),
        # StructField("responseStatusCode", StringType(), True),
        # StructField("language", StringType(), True)

    ])
    return schema