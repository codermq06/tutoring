f = open("input.txt")
file_data = f.read()
f.close()
print(file_data)
list1 = []
list2 = []
lines = file_data.strip().split('\n')
for line in lines:
    a, b = map(int, line.split())
    list1.append(a)
    list2.append(b)
#Good so far!
'''for j in range(len(list1)-1):
    for i in range((len(list1)-1)-j):
        if list1[j] > list1[j+i]:
            x = list1[i]
            list1[i] = list1[i+1]
            list1[i+1]= x
        else:
            break'''
for x in range(len(list1)):
    for i in range((len(list1)-1)):
        if list1[i] > list1[i+1]:
            x = list1[i]
            list1[i] = list1[i+1]
            list1[i+1]= x
for x in range(len(list2)):
    for i in range((len(list2)-1)):
        if list2[i] > list2[i+1]:
            x = list2[i]
            list2[i] = list2[i+1]
            list2[i+1]= x
number = 0
for i in range(len(list1)):
    number += abs(list1[i]-list2[i])

print((number))




