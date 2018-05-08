#!/bin/sh
echo "** About to split **"
#split -b 10m /home/ec2-user/iriscripts/test2/sampleaspirin1m.txt /home/ec2-user/iriscripts/test2/chunkfiles/sampleaspirin
#$1: size (e.g. 10m); $2: large file location; $3: chuck files' location; $4: S3 path
#command: sh splitfile.sh 1m /home/ec2-user/lab/largefiles/sampleaspirin.txt /home/ec2-user/lab/chunkfiles/sampleaspirinchunk/ s3://vedas3bucket1/lab/sourcedata/sampleaspirin/
split -b $1 $2 $3
echo "**Splitting file into chuncks is done**"
echo "**Moving files to S3**"
#for filename in "/home/ec2-user/lab/chunkfiles/sampleaspirinchunk"/*
for filename in "$3"/*
do
#echo "$filename"
#echo $(basename "$filename")
#aws s3 cp $filename s3://vedas3bucket1/lab/sourcedata/sampleaspirin/
aws s3 cp $filename $4
done
#aws s3 cp /home/ec2-user/lab/chunkfiles/sampleaspirinchunk/ s3://vedas3bucket1/lab/sourcedata/sampleaspirin/
echo "**Moved files to S3**"
#for file in sample/*; do
#echo $(basename "$file")
#done