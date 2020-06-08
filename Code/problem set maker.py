import random
n = int(input ("enter number of rows: "))
string=""
file = open("commonwords.txt","r")
data = file.read()
data= data.split("\n")
file.close()
file = open("nouns.txt","r")
data2 = file.read()
data2= data2.split("\n")
file.close()
puntuation= [".",",","?",":",";"]
for i in range(n):
    
    k = random.randint(7,20)
    for j in range(k):
        if j%2 ==0:
            index= random.randint(0,len(data2)-1)
            string+= data2[index]+ " "
            continue
        if j%5 ==0:
            index= random.randint(0,len(puntuation)-1)
            string+=puntuation[index]
            continue
        index= random.randint(0,len(data)-1)
        string+= data[index]+" "
    string+="\n"

file = open("SampleSet.txt" , "w")
file.write(string)
file.close()



        
