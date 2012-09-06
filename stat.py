# ECE 2524 Homework 2 Problem 3 Randall Ferrance

from sys import argv

filename = argv[1]

maxOwed = minOwed = totalOwed = numPeople = 0;
maxOwedBy = minOwedBy = " "

print "ACCOUNT SUMMARY"
with open(filename, 'r') as f:
    for line in f:
        newline = ' '.join(line.split())
        numPeople=numPeople+1
        owed = float(newline.split(' ',3)[2])
        if owed>maxOwed:
            maxOwed=owed
            maxOwedBy = newline.split(' ',2)[1]
        if owed<minOwed or numPeople==1:
            minOwed=owed
            minOwedBy = newline.split(' ',2)[1]
        totalOwed+=owed
        
    print "Total amount owed = ",totalOwed
    print "Average amount owed = ", (totalOwed/numPeople)
    print "Maximum amount owed = ", maxOwed, " by ", maxOwedBy
    print "Minimum amount owed = ", minOwed, " by ", minOwedBy
        
        
        
