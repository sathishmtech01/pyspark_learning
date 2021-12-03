from pyspark import SparkContext

sc = SparkContext()

rdd = sc.textFile("hadoop-tutorials-data/UN_Pop_Stats.csv")

rdd.take(5)


headless_rdd = rdd.filter(lambda line: 'LocID' not in line)

headless_rdd.take(5)

from collections import namedtuple
from pprint import pprint

pData = namedtuple('pData',['LocID','Location','VarID','Variant','Time','MidPeriod','SexID','Sex','AgeGrp','AgeGrpStart','AgeGrpSpan','Value'])

def map_record(record):
  columns = record.split(",")[:12]
  return pData(*columns)

ntuple_rdd = headless_rdd.map(map_record)

ntuple_rdd.take(5)

plot_rdd = ntuple_rdd.filter(lambda record: record.Location =='"Switzerland"' and record.Time == '"2015"' and record.Sex in ['"Male"','"Female"']) \
    .map(lambda record: (int(record.AgeGrpStart),int(float(record.Value)*1000))) \
    .reduceByKey(lambda x,y: x+y) \
    .sortByKey() \
    .collect()


import matplotlib.pyplot as plt

plt.figure(figsize=(14,6))
x_val = [x[0] for x in sorted(plot_rdd)]
y_val = [x[1] for x in sorted(plot_rdd)]
print(plot_rdd)
plt.bar(range(len(y_val)), y_val)
plt.xticks(range(len(x_val)), x_val, size='small')
plt.show()

# %load key/solution1.py

from operator import add

m_rdd = ntuple_rdd.filter(lambda record: record.Sex == '"Male"') \
    .map(lambda record: ((record.Location,record.Time,record.Sex),float(record.Value))) \
    .reduceByKey(add) \
    .map(lambda record: ((record[0][0],record[0][1]),(record[0][2],record[1])))

m_rdd.take(5)

f_rdd = ntuple_rdd.filter(lambda record: record.Sex == '"Female"') \
    .map(lambda record: ((record.Location,record.Time,record.Sex),float(record.Value))) \
    .reduceByKey(add) \
    .map(lambda record: ((record[0][0],record[0][1]),(record[0][2],record[1])))

f_rdd.take(5)

join_rdd = m_rdd.join(f_rdd)

join_rdd.take(5)

fn_rdd = join_rdd.map(lambda record: (record[1][0][1]/record[1][1][1],(record[0][0],record[0][1])))

ratio_rdd = fn_rdd.filter(lambda record: record[1][0] == '"Estonia"').map(lambda x,y: (y,x)).sortByKey().collect()

plt.figure(figsize=(14,6))
x_val = [x[0][1] for x in sorted(ratio_rdd)]
y_val = [x[1] for x in sorted(ratio_rdd)]
print(plot_rdd)
plt.plot(range(len(y_val)), y_val)
plt.xticks(range(len(x_val)), x_val, size='small')
plt.show()

fn_rdd.filter(lambda record: record[0] > 2.5 or record[0] < 0.8).sortByKey().collect()

# %load key/solution2.py
#
# %load key/solution3.py
#
# %load key/solution4.py

broadcastWorkingAge = sc.broadcast([25,30,35,40,45,50,55,60])


def map_agegrp(record):
    if int(record.AgeGrpStart) in broadcastWorkingAge.value:
         AgeGroup = 'WORKING'
    else:
         AgeGroup = 'RETIRED'
    return ((record.Location,record.Time,AgeGroup),float(record.Value))

def cal_ratio(record):
    if record[1][0] == 'WORKING':
         ratio = record[1][3] / record[1][1]
    else:
         ratio = record[1][1] / record[1][3]
    return (ratio,(record[0][0],record[0][1]))

ntuple_rdd.filter(lambda record: record.Sex == '"Both"' and int(record.AgeGrpStart) not in [0,5,10,15,20]) \
    .map(map_agegrp) \
    .reduceByKey(add) \
    .map(lambda record: ((record[0][0],record[0][1]),(record[0][2],record[1]))) \
    .reduceByKey(lambda a, b: a + b) \
    .map(cal_ratio) \
    .take(10)

ntuple_rdd.getNumPartitions()

rep_rdd = ntuple_rdd.repartition(5)

rep_rdd.getNumPartitions()

ntuple_rdd.cache()

rdd.id()

rdd.name()

ntuple_rdd.map(lambda record: record.Location).distinct().collect()

