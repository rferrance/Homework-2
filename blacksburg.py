# ECE 2524 Homework 2 Pro Randall Ferrance

from sys import argv

filename = argv[1]

print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
with open(filename, 'r') as f:
    for line in f:
        newline = ' '.join(line.split())
        if (newline.rsplit(' ',2)[1])=="Blacksburg":
            print newline.rsplit(' ',1)[1]+', '+newline.split(' ',2)[1]+', '+newline.split(' ',1)[0]+', '+newline.split(' ',3)[2]
             
