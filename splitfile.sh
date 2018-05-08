#!/bin/sh
echo "About to split"
#split -b 10m /home/ec2-user/iriscripts/test2/sampleaspirin1m.txt /home/ec2-user/iriscripts/test2/chunkfiles/sampleaspirin
#$1: size (e.g. 10m); $2: large file location; $3: chuck files' location; $4: chuck files' path; $5: S3 path
split -b $1 $2 $3
echo "**Splitting file into chucks is done**"
echo "**Move files to S3**"
aws s3 cp /home/ec2-user/iriscripts/test2/chunkfiles/sampleaspirinaa s3://bayer-cdh-poc/iri/
echo "**Moved files to S3**"

#for file in sample/*; do
#echo $(basename "$file")
#done