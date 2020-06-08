file = open("Hashtable.txt")
string= "lst = "
string +=file.read()
exec(string)

k=[]
for i in lst:
    if i != 0:
        k.append(len(i))
print("Total number of words in hash table: ",len(lst))
print("Max collisions : ",max(k))
frequency=[]
for i in  k:
    frequency.append((i,k.count(i)))
frequency= set(frequency)
print("Frequency of collisions: ",frequency)
count=0
frequency= list(frequency)
for i in range(len(frequency)):
    count += frequency[i][1]
print("Number of words after removal",count)
