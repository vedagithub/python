import sys
import os
fl = open("E:\Bayer\SampleFile.txt",'w')
strRow = 'red,aspirin,tablet'
#print strRow
rowcount = 0
price = 100
nrecords = 1000000000
while rowcount<nrecords:
    rowcount += 1
    price += 12
    fl.write(str(rowcount) + ',' + strRow + ',' + str(price) + '\n')
'''for i in range(1, nrecords):
    # print i
    rowcount += 1
    price += 12
    fl.write(str(rowcount)+','+strRow+','+str(price)+'\n')
'''
fl.close()
print 'file created with {} records'.format(nrecords)
