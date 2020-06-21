  

# Following program is the python implementation of 
# Rabin Karp Algorithm given in CLRS book 
  
# d is the number of characters in the input alphabet 
d = 256
  
# pat  -> pattern 
# txt  -> text 
# q    -> A prime number 
  
def search(pat, txt):  # slightly modified
    q = 201
    M = len(pat) 
    N = len(txt) 
    i = 0
    j = 0

    p = 0    # hash value for pattern 
    t = 0    # hash value for txt 
    h = 1
    index = []
    # The value of h would be "pow(d, M-1)%q" 
    for i in range(M-1): 
        h = (h*d)%q 
  
    # Calculate the hash value of pattern and first window 
    # of text 
    for i in range(M): 
        p = (d*p + ord(pat[i]))%q 
        t = (d*t + ord(txt[i]))%q 
  
    # Slide the pattern over text one by one 
    for i in range(N-M+1): 
        # Check the hash values of current window of text and 
        # pattern if the hash values match then only check 
        # for characters on by one 
        if p==t: 
            # Check for characters one by one 
            for j in range(M): 
                if txt[i+j] != pat[j]: 
                    break
  
            j+=1
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1] 
            if j==M: 
                index.append(i)
  
        # Calculate hash value for next window of text: Remove 
        # leading digit, add trailing digit 
        if i < N-M: 
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q 
  
            # We might get negative values of t, converting it to 
            # positive 
            if t < 0: 
                t = t+q 
    return index
     
def saerching_orignal_algorithim(string, lst):
    strings= "Keyword not found"
    string = string.split()
    b= set()
    c= set()
    d = set()
    temp= search(string[0], lst)
    if temp == None :
        a= set()
    else:
        a= set(temp)
    if len(string) > 1:
        temp= search(string[1], lst)
        if temp == None :
            b= set()
        else:
            
            b= set(temp)
    if len(string) > 2:
        temp= search(string[2], lst)
        if temp == None :
            c= set()
        else:
            c= set(temp)
    if len(string) > 3:
        temp= search(string[3], lst)
        if temp == None :
            d= set()
        else:
            d= set(temp)
    
    if a == set() and b == set()and c == set() and d== set():
        result = []
    if a != set() and b == set()and c == set() and d== set():
        result = a
    if a != set() and b != set()and c == set() and d== set():
        result = list(a.intersection(b))
    if a != set() and b != set() and c != set() and d== set():

        result = list(a.intersection(b,c,d))
    result= list(result)
    if result == []:
        result = list(a)+list(b)
    if result != []:
        strings=""
    
    return (result , strings)
    

    p = 0     
    t = 0     
    h = 1
  
    for i in range(M-1): 
        h = (h * d)% q
    
  
    for i in range(M): 
        p = (d * p + ord(pat[i]))% q 
        t = (d * t + ord(txt[i]))% q
        print("pattern",p)
        print("text",t)
    for i in range(N-M + 1): 
        
        if p == t: 
             
            for j in range(M): 
                if txt[i + j] != pat[j]: 
                    break
  
            j+= 1 
            if j == M: 
                print ("Pattern found at index " + str(i)) 
  
        
        if i < N-M: 
            t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q  
            if t < 0: 
                t = t + q 


def fuzzy_word(word):
    
    if  type(word) == str:
        word= word.lower()
        string=word[0]
        lst= ["h","w","y","a","e","i","o","u"]
        dic= {"b":1, "f":1 ,"p":1, "v":1,"c":2 ,"g":2 , "j":2 , "k":2, "q":2, "s":2, "x":2, "z":2,"d":3, "t":3, "l":4,"m":5, "n":5, "r":6}
        for i in range(1,len(word)):
            if not (ord(word[i]) >= 97 and ord(word[i]) <= 122):
                continue
            if word[i] in lst:
                continue
            string+= str(dic[word[i]])
        final = string[0]
        for i in range(1,len(string)):
            if string[i] != final[-1]:
                final+= string[i]
        if len(final)> 4:
            final = final[:4]
        while len(final) < 4:
            final+= "0"
        
        return final
    else:
        return word


def extract(stop_words,lst ):
    string= []
    lst1=[]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] not in stop_words:
                string.append(fuzzy_word(lst[i][j]))
        lst1.append(string)
        string=[]
    return lst1
def Rabin(lst , pat):
    index =[]
    pat = fuzzy_word(pat)
    
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == pat:
                index.append(i)
    return index
def search_rabin(string, lst,sentences):
    string = string.split()
    strings= "Keyword not found"
    b= set()
    c= set()
    d = set()
    temp= Rabin(lst , string[0])
    result= []
    if temp == None :
        a= set()
    else:
        a= set(temp)
    if len(string) > 1:
        temp= Rabin(lst , string[1])
        if temp == None :
            b= set()
        else:
            
            b= set(temp)
    if len(string) > 2:
        temp= Rabin(lst , string[2])
        if temp == None :
            c= set()
        else:
            c= set(temp)
    if len(string) > 3:
        temp= Rabin(lst , string[3])
        if temp == None :
            d= set()
        else:
            d= set(temp)
   
    if a != set() and b == set()and c == set() and d== set():
        result = a
    if a != set() and b != set()and c == set() and d== set():
        result = list(a.intersection(b))
    if a != set() and b != set() and c != set() and d== set():

        result = list(a.intersection(b,c,d))
    result= list(result)
    if result == []:
        result = list(a)+list(b)
    if result != []:
        strings=""
    for i in range(len(result)):
        strings+= "("+str(i+1)+")"+" ".join(sentences[result[i]])+"\n"
    return strings
    
d = 256
file = open("SampleSet.txt","r")
string=file.read()
file.close()
file = open("stop words.txt","r")
stop_words=file.read()
stop_words= stop_words.split("\n")
file.close()
lst_sent = string.split("\n")
lst = [i.split() for i in lst_sent]
lst = extract(stop_words,lst )
pat ="father"
search_rabin(pat, lst,lst_sent)
#pat = "father"
#print(saerching_orignal_algorithim(pat, string))



import cProfile
#cProfile.run('saerching_orignal_algorithim(pat, string)')
#cProfile.run("search_rabin(pat, lst,lst_sent)")
