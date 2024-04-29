from spark_iceberg.spark_session import setup_spark_session
from kafka_consumer.kafka_consume import connect_to_kafka,consume_kafka_message
from conf import load_config


def main():
    config = load_config()
    print(config)
    spark = setup_spark_session(config)
    print("Spark Running")

    connect_to_kafka(config)

    consume_kafka_message(config,spark)
if __name__ == "__main__":
    main()