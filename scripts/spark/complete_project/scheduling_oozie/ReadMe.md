https://blog.surajnayak.com/introd-oozie/
http://crazyadmins.com/tag/how-to-execute-shell-script-in-oozie/

(BOL) sathish@sathish-Latitude-3480:~/Sathish/BOL/scripts/spark/complete_project/scheduling_oozie/wordcount_example$ hadoop version
Hadoop 2.8.4
Subversion https://git-wip-us.apache.org/repos/asf/hadoop.git -r 17e75c2a11685af3e043aa5e604dc831e5b14674
Compiled by jdu on 2018-05-08T02:50Z
Compiled with protoc 2.5.0
From source with checksum b02a59bb17646783210e979bea443b0
This command was run using /home/sathish/hadoop-2.8.4/share/hadoop/common/hadoop-common-2.8.4.jar

(BOL) sathish@sathish-Latitude-3480:~/Sathish/BOL/scripts/spark/complete_project/scheduling_oozie/wordcount_example$ java -version
java version "1.8.0_161"
Java(TM) SE Runtime Environment (build 1.8.0_161-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.161-b12, mixed mode)

Issue:
2018-07-27 23:37:42,488 [main] INFO  org.apache.hadoop.ipc.Client - Retrying connect to server: localhost/127.0.0.1:10020. Already tried 9 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)

turn off ipv6 in /etc/sysconfig/network or /etc/sysconfif/network-manager/ifcfg-eth0

parameter

NETWORKING_IPV6=no

IPV6INIT=no

Please check selniux is disable or not if not then disable it and reboot.

vi /etc/sysconfig/selinux

selinux=disabled

Also check ntp and iptable and firewall.
