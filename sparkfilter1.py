import findspark
findspark.init()
from pyspark import SparkContext
sc = SparkContext("local", "test App")
data = sc.textFile("/home/ec2-user/lab/sample.txt")
print(data.count())
delivered_data=data.filter(lambda x: 'delivered' in x)
print("delivered are {}".format(delivered_data.count()))
print(delivered_data.collect())
delivered_data.saveAsTextFile("/home/ec2-user/lab/sample_delivered")