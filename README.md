### Data Ingestion from kafka to Mino S3 with Pyspark & Iceberg.


## Introuction about demo.

How to stream data from Kafka brocker and ingest streaming data to S3 object storage using iceberg .

![images/arch.png.png](images/arch.png)


The followoing components involved for this demo and deployed as docker compose 
    Spark - pyspark
    Hive metastore 
    Postrgres DB
    Iceberg
    Minio
    Minio client
    Kafka 

### running the demo locally

```bash
   docker compose build
   docker compose up
    ```
run kafka producer to pus data to kafka topic 

    ```bash
    ./pyhthon3 /spark-iceberk-minio/app/kafka_consumer/kafka_producer.py

    ```