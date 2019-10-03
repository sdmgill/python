import csv

with open('C:\\Users\\seangi\\OneDrive - Ports America\\_Projects\\EDW\\AWS\\DMSTesting\\sg_test1\\LOAD00000001.csv','r') as inf, \
    open('C:\\Users\\seangi\\OneDrive - Ports America\\_Projects\\EDW\\AWS\\DMSTesting\\sg_test1\\LOAD00000001.csv','a') as outf:
    csvreader = csv.DictReader(inf)
    fieldnames = ['PNCT'] + ['L'] + csvreader.fieldnames  # add column name to beginning
    csvwriter = csv.DictWriter(outf, fieldnames)
    csvwriter.writeheader()
    for systemname, row in enumerate(csvreader, 1):
        csvwriter.writerow(dict(row, PNCT='PNCT', L='L'))

try:
    file_object = open('C:\\Users\\seangi\\OneDrive - Ports America\\_Projects\\EDW\\AWS\\DMSTesting\\sg_test1\\LOAD00000001.csv', 'r')
    lines = csv.reader(file_object, delimiter=',', quotechar='"')
    flag = 0
    data=[]
    for line in lines:
        if line == []:
            flag =1
            continue
        else:
            data.append(line)
    file_object.close()
    if flag ==1: #if blank line is present in file
        file_object = open('C:\\Users\\seangi\\OneDrive - Ports America\\_Projects\\EDW\\AWS\\DMSTesting\\sg_test1\\LOAD00000001.csv', 'w')
        for line in data:
            str1 = ','.join(line)
            file_object.write(str1+"\n")
        file_object.close()
except e:
    print(e)