from db.schema.schema import create_schema
from pyspark.errors import PySparkException

def create_iceberg_table(spark):
    try:
        # Create Iceberg table using the specified schema and catalog
        print("Iceberg databae created  1------ ")

        spark.sql(""" CREATE DATABASE IF NOT EXISTS observability  """)
        
        # spark.sql("create database observability location '/user/data_transform/iceberg_test'")
       
        print("Iceberg databae created  ------ ")
       
        
        spark.sql("""
            CREATE TABLE IF NOT EXISTS observability.trace  (
                traceId string,
                logData string                
            )  USING iceberg  """)
        
       
        print("Iceberg table trace created ------ ")
       
        print("Iceberg table 'apm.trace' created successfully.")
    except Exception as e:
        print("Error creating Iceberg table:", str(e))

def write_to_iceberg_table(trace, spark):
    # schema creation will part of image initailiation , it needs to be commneted out 
    create_iceberg_table(spark)
    

    trace_df = spark.createDataFrame(trace, schema=create_schema())

    try:
       
        # trace_df.writeTo("iceberg.observability.trace").create()
        trace_df.show()
        trace_df.printSchema()
        spark.catalog.currentDatabase()
        spark.catalog.listDatabases()
        # trace_df.writeTo("observability.trace").createOrReplace()
        trace_df.writeTo("observability.trace").append()
        
        print("Data written to Iceberg table trace successfully." )
    except Exception as e:
        print("Error writing data to Iceberg trace table:", str(e))