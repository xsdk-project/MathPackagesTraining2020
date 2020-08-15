from __future__ import print_function
import csv, re
from datetime import datetime
  
#
# Read the exported csv file named 'sme_choices.csv' from the Google
# form submission data
#
requests = []
with open('sme_choices.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        if line[0] == 'Timestamp': # skip header line
           header = [re.sub('Select Priorities \[(.*) \((.*)\)\]',r'\1',x) for x in line]
           header_counts = [0] * len(header)
           continue
        line_time = datetime.strptime(line[0], '%m/%d/%Y %H:%M:%S')
        # time stamp ensures first-come, first served ordering
        time_id = abs((line_time - datetime(2020,8,4)).total_seconds())
        student_id = line[1]
        request = [time_id, student_id]
        for i in range(2,len(line)-2):
            if line[i]:
                request += [header[i]]
                header_counts[i] += 1
        requests += [request]

#
# Setup empty assignments
#
maxSlots = 4
assignments = {}
for req in requests:
    assignments[req[1]] = [True] * maxSlots

print('### Errors')


#
# Any SME's not at all selected?
#
schedule = {}
for i in range(2,len(header)-2):
    if header_counts[i] == 0:
        print('* ', header[i], 'has no selections')
    else:
        schedule[header[i]] = [''] * maxSlots

#
# Ensure requests are sorted by time of arrival
#
def requestTime(e):
    return e[0]
requests.sort(key=requestTime)

#
# Iterate over requests assigning first, then second
# and finally third priorities
#
for i in range(1,4):
    for req in requests:
        if len(req)-2 < i:
            continue
        student = req[1]
        sme = req[2+i-1]
        slot = 0
        while slot < maxSlots and \
            (assignments[student][slot] == False or \
            schedule[sme][slot] != ''):
            slot += 1
        if slot == maxSlots:
            print('* Unable to schedule student "%s" %d choice of "%s"'%(student,i,sme))
            continue
        if assignments[student][slot]:
            schedule[sme][slot] = student
            assignments[student][slot] = False
        else:
            print('* Slot not available for student "%s" %d choice of "%s"'%(student,i,sme))

#
# Output markdown for the schedule
#
print('\n\n### Schedule')
mdhdr = '|**SME**|' + ''.join(['**Slot %d**|'%i for i in range(maxSlots)])
mdhdr1 = '|:---|' + ''.join([':---:|' for i in range(maxSlots)])
print(mdhdr)
print(mdhdr1)
for item in schedule:
    print('|%s|'%item, end=' ')
    for student in schedule[item]:
       print('%s|'%student, end='')
    print('\n', end='')
