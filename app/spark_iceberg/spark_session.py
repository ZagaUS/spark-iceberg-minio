from pyspark import SparkConf
from pyspark.sql import SparkSession

def setup_spark_session(config):
    spark_config = config['spark']
    conf = SparkConf() \
        .setAppName(spark_config['app_name']) \
        .setMaster(spark_config['master']) \
        .set('spark.jars.packages', 'org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.5.1,org.apache.iceberg:iceberg-aws-bundle:1.5.1')\
        .set("spark.driver.memory", spark_config['spark_properties']['spark.driver.memory']) \
        .set("spark.executor.memory", spark_config['spark_properties']['spark.executor.memory']) \
        .set("spark.driver.host", spark_config['spark_properties']['spark.driver.host']) \
        .set("spark.sql.shuffle.partitions", spark_config['spark_properties']['spark.sql.shuffle.partitions']) \
        .set("spark.sql.catalog.apm", spark_config['iceberg_properties']['spark.sql.catalog.apm']) \
        .set("iceberg.engine.hive.enabled", spark_config['iceberg_properties']['iceberg.engine.hive.enabled']) \
        .set("spark.sql.defaultCatalog", spark_config['iceberg_properties']['spark.sql.defaultCatalog'])\
        .set("spark.sql.catalog.apm.type", spark_config['iceberg_properties']['spark.sql.catalog.apm.type']) \
        .set("spark.sql.catalog.apm.uri", spark_config['iceberg_properties']['spark.sql.catalog.apm.uri'])\
        .set("spark.sql.catalog.apm.cache-enabled", spark_config['iceberg_properties']['spark.sql.catalog.apm.cache-enabled'])\
        .set("spark.hadoop.hive.metastore.schema.verification", spark_config['iceberg_properties']['spark.hadoop.hive.metastore.schema.verification'])\
        .set("spark.hadoop.hive.metastore.schema.verification.record.version", spark_config['iceberg_properties']['spark.hadoop.hive.metastore.schema.verification.record.version'])\
        .set("spark.sql.catalog.apm.warehouse", spark_config['iceberg_properties']['spark.sql.catalog.apm.warehouse'])\
        .set("spark.sql.catalog.apm.io-impl", spark_config['iceberg_properties']['spark.sql.catalog.apm.io-impl'])\
        .set("spark.sql.catalog.apm.s3.endpoint", spark_config['iceberg_properties']['spark.sql.catalog.apm.s3.endpoint'])\
        .set("spark.sql.extensions", spark_config['iceberg_properties']['spark.sql.extensions'])\
        .set("spark.eventLog.enabled", spark_config['iceberg_properties']['spark.eventLog.enabled'])\
        .set("spark.sql.catalog.apm.s3.path-style-access", spark_config['iceberg_properties']['spark.sql.catalog.apm.s3.path-style-access'])\
        .set("spark.sql.storeAssignmentPolicy", spark_config['iceberg_properties']['spark.sql.storeAssignmentPolicy'])

    spark = SparkSession.builder.config(conf=conf).enableHiveSupport().getOrCreate()
    return spark