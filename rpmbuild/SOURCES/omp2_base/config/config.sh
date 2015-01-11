#!/bin/sh
cp /etc/init_d_bak/jexec /etc/init.d/
/etc/init.d/jexec start
source /etc/profile.d/init_java_home.sh
source /etc/profile.d/init_zookeeper.sh
source /etc/profile.d/storm-init.sh
#/usr/share/neo4j-community-1.9.5/bin/neo4j install
test -e "/omp2" && (test -e "/omp2/flag/drpcs/pid" || rm -rf /service/e_drpc)
#test -e "/omp2" && (test -e "/omp2/flag/neo4j/pid" || rm -rf /service/d_neo4j)
rm -rf /service/d_neo4j
test -e "/omp2" && (test -e "/omp2/flag/nimbus/pid" || rm -rf /service/c_nimbus)
test -e "/omp2" && (test -e "/omp2/flag/supervisors/pid" || rm -rf /service/b_supervisor)
test -e "/omp2" && (test -e "/omp2/flag/zookeepers/pid" || rm -rf /service/a_zookeepr)
test -e "/omp2" && (test -e "/omp2/flag/storm-ui/pid" || rm -rf /service/f_storm-ui)
test -e "/omp2/config/storm/storm.yaml" && cp /omp2/config/storm/storm.yaml /usr/local/storm/conf
test -e "/omp2/config/zookeeper/zoo.cfg" && cp /omp2/config/zookeeper/zoo.cfg /usr/share/zookeeper-3.4.5/conf
test -e "/omp2/config/zookeeper/myid" && cp /omp2/config/zookeeper/myid /usr/share/zookeeper-3.4.5/data
test -e "/omp2/config/client" && cp -rf /omp2/config/client/* /usr/omp2/config
test -e "/omp2/route_data" && mv /omp2/route_data /usr/omp2/
cd /package/admin/daemontools-0.76 && sh package/upgrade
cd /package/admin/daemontools-0.76 && sh package/run
