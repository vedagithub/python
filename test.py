import sys
sys.path.append('/home/ec2-user/iriscripts/test/')
from pyspark import StorageLevel

def initializeSparkHiveContext(application_name):
	from pyspark.sql import HiveContext
	from pyspark.sql import SparkSession
	from pyspark.sql import SQLContext	
	#spark = SparkSession.builder.master("yarn").appName(application_name).getOrCreate()
	#spark = SparkSession.builder.master("local").appName(application_name).getOrCreate()
	spark = SparkSession.builder.master("local").appName(application_name).enableHiveSupport().getOrCreate()	
	sc = spark.sparkContext
	hive_context = HiveContext(sc)
	print 'spark/hive context'
	return hive_context
	
def main():
	#Create Hive context
	hive_context = initializeSparkHiveContext('iri_bi_data_brand')
	hive_context.sql("SET mapred.input.dir.recursive=true")	
	print 'create df dataframe'	
	df = hive_context.sql('select * from consumer.iri_bi_data_brand_cleansed limit 10')	
	#df = hive_context.sql("select 100")
	print 'showing df dataframe..'
	df.show()
	print 'end of showing df dataframe..'
	print 'start of creating processed table..'		
	df.registerTempTable("IRI_BI_DATA_BRAND_INT")
	df2=hive_context.sql('insert overwrite table consumer.iri_bi_data_brand_proc select * from IRI_BI_DATA_BRAND_INT')
	print 'end of creating processed table'

if __name__ == "__main__":
	try:
		main()
	except BaseException as error: 
		print("exception in main")
		raise