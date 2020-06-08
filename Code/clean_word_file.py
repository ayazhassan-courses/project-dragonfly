file = open("nouns.txt","r")
string = file.read()
file.close()
string= string.split("\n")
lst = [i.split() for i in string]
lst1=[]
for i in lst:
    try:
        
        lst1.append(i[1])
    except Exception:
        continue
del lst
string= "\n".join( lst1)
file = open("nouns.txt","w")
file.write(string)
file.close()

