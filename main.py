import random

rand_list = []  #create list of random items
n = 100
for i in range(n):
    rand_list.append(random.randint(0, 1000))
print("Random List", rand_list)

for i in range(0, len(rand_list)): #use sort
    for j in range(i + 1, len(rand_list)):
        if rand_list[i] >= rand_list[j]:
            rand_list[i], rand_list[j] = rand_list[j], rand_list[i]
# sorted list
print("Sorted List", rand_list)

se = 0 #sum even
so = 0 #count even
ce = 0 #sum odd
co = 0 #count odd
for i in rand_list:
    if i % 2 == 0:
        se += i #sum even
        ce += 1 #count even
    else:
        so += i #sum odd
        co += 1 #count even
print('average for even', se/ce)
print('average for odd', so/co)
