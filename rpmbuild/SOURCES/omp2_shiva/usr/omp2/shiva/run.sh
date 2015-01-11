#!/bin/sh
#export REDIS_IP=127.0.0.1
rm -rf tmp && mkdir tmp && (cd tmp && jar xvf ../shiva-2.0.0.war > structure.log) && exec java -jar shiva-2.0.0.war > run.log &
