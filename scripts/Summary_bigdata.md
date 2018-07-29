Summary of Big data Course:

1. Messaging layer
2. Data Injection Layer
3. ETL Layer
4. Scheduling Layer
5. Front End Layer

1. Messaging layer

(Web sockets)
(TCP)
a. Kafka
    - Producer (produces data which is in bytes)
        -  each data is tracked through the topics   
    - Consumer (consumes the streaming byte data)
b. Flume (Same like kafka) but outdated


2. Data Injection Layer
a. Sqoop
    - Data injection from rdbms to hadoop
    - Vice versa
    - incremental import
    - all tables import
    
3. ETL Layer
a. Spark
    - lazy loading means till the action is performed the transform is on hold.
    - RDD
        - transform (map, flatmap, groupby)
        - action (collect, count, write)
    - Dataframe
        - Sql kind of table row, column approach
        - Sql kind queries
        - Pandas dataframe kind opeartion (filter,groupby,aggregate)
    - Stream Capture
        - ssc (spark streaming context)
        - receiving streaming data
        - source to the receiver may come from messaging devices
            - kafka
            - flume
            - socket
    - Other Operations
        - storing in HDFS
        - storing is MySQL

b. Pig (out dated)
    - Big data Scripting tool (Yahoo tool)
    - Map, Aggregation  

c. Hive
    - Big data warehouse
    - SQL kind querying service
    - In backend the tables are stored in hdfs file system
                 
4. Scheduling Layer
    - Oozie
        - workflow.xml (process of the task, what to do before running script, after script execution what to do)
        - coordinator.xml (scheduling oriented, starttime (1-1-2017), endtime(1-1-2117), frequency(5min, 10 min, 24 hrs))
        - job.properties (all properties of the job like,namenode,jobTracker,script,workflow,cooridnator)
        nameNode=hdfs://localhost:9000
        jobTracker=localhost:8032
        - jobs that can be run in oozie: 
           shell script | jar | hive | pig

5. Front End Layer
    - Java Appication (D3 charts- dashbord)
    - ETL Application
    - CRM Application

6. Load Balancer
    - Zookeeper is a big data tool for balancing the load

7. Bigdata platform
    - Cloudera
    - Hortonworks
    
8. Programming Languages:
    - Python
    - Scala
    - Java
    - R    
      
Architecture Level:
1. Lambda Architecture

 
References:
 
https://www.datamation.com/big-data/big-data-architecture.html
https://medium.com/makemytrip-engineering
