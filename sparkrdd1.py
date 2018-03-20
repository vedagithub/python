import findspark
findspark.init()
from pyspark import SparkContext
sc = SparkContext("local", "test App")
data = sc.textFile("/home/ec2-user/lab/output/Employee.txt")
print(data.take(1))

data.saveAsTextFile("/home/ec2-user/lab/output/Employee3/")
print("file saved")