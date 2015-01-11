#!/bin/sh
#export GRAPH_DB_PATH=/Users/twer/Documents/projects/sfexpress/graph.db
rm -rf tmp && mkdir tmp && (cd tmp && jar xvf ../vishnu-2.0.0.war > structure.log) && exec java -jar vishnu-2.0.0.war > run.log &
