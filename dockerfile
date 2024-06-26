FROM python:3.9-bullseye

#############################################
# install pipenv
############################################
ENV PIPENV_VENV_IN_PROJECT=1

# ENV PIPENV_VENV_IN_PROJECT=1 is important: it causes the resuling virtual environment to be created as /app/.venv. Without this the environment gets created somewhere surprising, such as /root/.local/share/virtualenvs/app-4PlAip0Q - which makes it much harder to write automation scripts later on.

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir pipenv

RUN pip install --no-cache-dir jupyter

RUN pip install --no-cache-dir py4j

RUN pip install --no-cache-dir findspark

#spark
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      sudo \
      curl \
      vim \
      unzip \
      openjdk-11-jdk \
      build-essential \
      software-properties-common \
      ssh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Jupyter and other python deps
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Add scala kernel via spylon-kernel
RUN python3 -m pip install spylon-kernel


# Optional env variables
ENV SPARK_HOME=${SPARK_HOME:-"/opt/spark"}
ENV PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9.7-src.zip:$PYTHONPATH

WORKDIR ${SPARK_HOME}

ENV SPARK_VERSION=3.5.1
ENV SPARK_MAJOR_VERSION=3.5
ENV ICEBERG_VERSION=1.5.1

# jupitor note
ENV PYSPARK_PYTHON=/usr/bin/python3
ENV PYSPARK_DRIVER_PYTHON='jupyter'
ENV PYSPARK_DRIVER_PYTHON_OPTS='notebook --no-browser --port=4041'

# Download spark
RUN mkdir -p ${SPARK_HOME} \
 && curl https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz -o spark-${SPARK_VERSION}-bin-hadoop3.tgz \
 && tar xvzf spark-${SPARK_VERSION}-bin-hadoop3.tgz --directory /opt/spark --strip-components 1 \
 && rm -rf spark-${SPARK_VERSION}-bin-hadoop3.tgz

# Download iceberg spark runtime
RUN curl https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-${SPARK_MAJOR_VERSION}_2.12/${ICEBERG_VERSION}/iceberg-spark-runtime-${SPARK_MAJOR_VERSION}_2.12-${ICEBERG_VERSION}.jar -Lo /opt/spark/jars/iceberg-spark-runtime-${SPARK_MAJOR_VERSION}_2.12-${ICEBERG_VERSION}.jar

# Download AWS bundle
RUN curl -s https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-aws-bundle/${ICEBERG_VERSION}/iceberg-aws-bundle-${ICEBERG_VERSION}.jar -Lo /opt/spark/jars/iceberg-aws-bundle-${ICEBERG_VERSION}.jar

# Download PostgreSQL JDBC driver
RUN curl -s https://jdbc.postgresql.org/download/postgresql-42.2.23.jar -o /opt/spark/jars/postgresql-jdbc.jar

# Add iceberg spark runtime jar to IJava classpath
ENV IJAVA_CLASSPATH=/opt/spark/jars/*

RUN mkdir -p /home/iceberg/localwarehouse  /home/iceberg/warehouse /home/iceberg/spark-events /home/iceberg /opt/spark/spark-events

RUN mkdir -p /notebook
RUN chmod +x /notebook
COPY spark-defaults.conf /opt/spark/conf
ENV PATH="/opt/spark/sbin:/opt/spark/bin:${PATH}"

RUN chmod u+x /opt/spark/sbin/* && \
    chmod u+x /opt/spark/bin/*


# Set the working directory to /app
WORKDIR /app

COPY ./app .

COPY ./entrypoint.sh .

# Copy the current directory contents into the container at /app
RUN chmod +x /app/entrypoint.sh

#EXPOSE 4040
EXPOSE 4040 4041


ENTRYPOINT ["./entrypoint.sh"  ]
# CMD [ "jupyter notebook --ip=0.0.0.0 --port=4041 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''"]