# ECE 2524 Homework 2 Problem 1 Randall Ferrance

with open('/etc/passwd', 'r') as f:
    for line in f:
        print line.split(':',1)[0] + '\t' + line.rsplit(':',1)[1]
        
