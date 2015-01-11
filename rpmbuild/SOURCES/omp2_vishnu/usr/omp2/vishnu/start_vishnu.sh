#!/bin/sh
VISHNU_HOME=`pwd`
export JAVA_HOME=$VISHNU_HOME/jdk1.7.0_45
export PATH=$JAVA_HOME/bin:$PATH
export GRAPH_DB_PATH=$VISHNU_HOME/data/graph.db
sh run.sh &
echo "started"
