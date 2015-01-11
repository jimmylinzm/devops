#!/bin/sh -e

umask 022

initctl stop svscan
sudo rm -rf /etc/init/svscan.conf
initctl reload-configuration
rm -rf /service
#/usr/share/neo4j-community-1.9.5/bin/neo4j remove
#pkill -f neo4j
pkill -f storm
pkill -f zookeeper
rm -rf /usr/local/storm
rm -rf /usr/share/neo4j-community-1.9.5
rm -rf /usr/share/zookeeper-3.4.5
rm -rf /usr/omp2
rm -rf /package 
rm -rf /etc/alternatives/java
rm -rf /etc/alternatives/javac
rm -rf /etc/alternatives/javaws
rm -rf /etc/alternatives/jar
rm -rf /usr/bin/java
rm -rf /usr/bin/javac
rm -rf /usr/bin/javaws
rm -rf /usr/bin/jar
