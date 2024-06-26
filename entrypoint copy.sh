#!/bin/bash

#set -ex


# /opt/spark/bin/spark-submit app.py & jupyter notebook --ip=0.0.0.0 --port=4041 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''

# Start Spark master
# $SPARK_HOME/sbin/start-master.sh -h localhost

# Start Spark worker
# 
#$SPARK_HOME/sbin/start-worker.sh spark://localhost:7077 -h localhost


# Wait for Spark services to start
# sleep 10

# jupyter notebook --ip=0.0.0.0 --port=4041 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''
jupyter notebook --ip=0.0.0.0 --port=4041 --allow-root --NotebookApp.token='' --NotebookApp.password=''

# Execute PySpark job from Python script
# /opt/spark/bin/spark-submit app.py


# Execute PySpark job from Jupyter notebook
# jupyter nbconvert --to notebook --execute your_notebook.ipynb
