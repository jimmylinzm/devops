#!/bin/sh
source /etc/profile.d/init_java_home.sh
cd /usr/omp2/bin && sh submit_omp2.sh $1 $2
