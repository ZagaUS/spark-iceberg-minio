from kafka import KafkaConsumer
import logging
import time
from dotenv import load_dotenv
load_dotenv(verbose=True)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import json
from spark_iceberg.persist_data import write_to_iceberg_table
from spark_iceberg.data_preprocess import process_kafka_message


def connect_to_kafka(config):
    
    kafka_config = config['Kafka']
    print("kafak connection--" ,kafka_config )
    while True:
        try:
            consumer = KafkaConsumer(
                bootstrap_servers=kafka_config['bootstrap_servers'],
                security_protocol=kafka_config['security_protocol'],
                value_deserializer=lambda v: json.loads(v.decode('ascii')),
                auto_offset_reset=kafka_config['auto_offset_reset'],
                group_id=kafka_config['group_id'], 
                session_timeout_ms=kafka_config['session_timeout_ms'],  
                request_timeout_ms=kafka_config['request_timeout_ms'],
                ssl_cafile=kafka_config['ssl_cafile'],
                ssl_certfile=kafka_config['ssl_certfile']
            )
            consumer.subscribe([kafka_config['topic']])
            return consumer
        except Exception as e:
            print("Failed to connect to Kafka: begin", e)

            logger.error(e)
            
            print("Failed to connect to Kafka: end", e)
            time.sleep(10)

def consume_kafka_message(config,spark):
    consumer = connect_to_kafka(config)
    for message in consumer:
        trace=process_kafka_message(message)
        print(trace)
        print('\n')
        print("=======started writing into the spark=========")
        # print(type(message))
        write_to_iceberg_table(trace,spark)
        print("=======ended writing into the spark=========")
