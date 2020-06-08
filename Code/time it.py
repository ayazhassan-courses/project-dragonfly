# importing the required module 
import timeit 
import hashlib
import math
import tkinter as tk
from tkinter import filedialog

def get_index(string,prime):   # n = number of index
    string = string.lower()
    m = hashlib.sha256(str.encode(string))
    hash_result = m.hexdigest()
    index_number= int(hash_result,16) % prime
    return (index_number,string)
def find_prime(n):
    if n > 1:  
        for i in range(2, n): 
            if (n % i) == 0: 
                return False
         
        return True 
    else: 
        return False 
    
def nearest_prime(n):
    
    bool_a = find_prime(n)
    
    if bool_a == True:
        return n
    return nearest_prime(n+1)
        
def make_lst(strings):
    lst = strings.split('\n')
    lst= [i.split() for i in lst]
    return lst
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
        return 0


def make_hashtable(sentences):      # sentence(format) = [[group1 words], [group2 words]]
    n= sum([len(i) for i in sentences])
    prime =  nearest_prime (n)
    lst= [0 for i in range(prime)]  # initialize array
    for i in range(len(sentences)):
        group_no = i
        for j in range(len(sentences[i])):
            word= fuzzy_word(sentences[i][j])
            index, word = get_index(word,prime)
            bool_list=False
            if lst[index] == 0:
                lst[index]= [[word,[group_no]]]
                continue
            for h in range(len(lst[index])):
                if lst[index][h][0] == word:
                    if group_no not in  lst[index][h][1]:
                        
                        lst[index][h][1].append(group_no)
                        bool_list= True
                if len(lst[index][h][1]) >= math.ceil(2*len(sentences)/3):
                    lst[index][h].append("Too common")
            if bool_list== False:
                lst[index].append([word,[group_no]])
            
    
    for i in range(len(lst)):   # removing common words
        if isinstance(lst[i],int):
            continue
        for j in range(len(lst[i])):
            if len(lst[i][j]) >= 3:
                del lst[i][j]
                break
    return lst

def search(word,lst):
    prime= len(lst)
    fuzzy= fuzzy_word(word)
    index,word1 = get_index(fuzzy,prime)
    g= lst[index]
    num = None
    if g != 0 :
        for i in range(len(g)):
            if fuzzy == g[i][0]:
                num = g[i][1]
    return num




def get_keywords(string,lst,sentences):
    string= string.split()
    strings= "Keyword not found"
    b= set()
    c= set()
    d = set()
    temp= search(string[0],lst)
    if temp == None :
        a= set()
    else:
        a= set(temp)
    if len(string) > 1:
        temp= search(string[1],lst)
        if temp == None :
            b= set()
        else:
            
            b= set(temp)
    if len(string) > 2:
        temp= search(string[2],lst)
        if temp == None :
            c= set()
        else:
            c= set(temp)
    if len(string) > 3:
        temp= search(string[3],lst)
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
    
    for i in range(len(result)):
        strings+= "("+str(i+1)+")"+" ".join(sentences[result[i]])+'\n'
    return "" 
file = open("SampleSet.txt","r")
st= file.read()
sentences = make_lst(st)
lst =make_hashtable(sentences)
pat= "father today"

#########################################################################Rabin Krap altered################################################################################
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

############################################################orignal algorithim################################################################
# Following program is the python implementation of 
# Rabin Karp Algorithm given in CLRS book 
  
# d is the number of characters in the input alphabet 
d = 256
  
# pat  -> pattern 
# txt  -> text 
# q    -> A prime number 
  
def searchR(pat, txt):  # slightly modified
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
    temp= searchR(string[0], lst)
    if temp == None :
        a= set()
    else:
        a= set(temp)
    if len(string) > 1:
        temp= searchR(string[1], lst)
        if temp == None :
            b= set()
        else:
            
            b= set(temp)
    if len(string) > 2:
        temp= searchR(string[2], lst)
        if temp == None :
            c= set()
        else:
            c= set(temp)
    if len(string) > 3:
        temp= searchR(string[3], lst)
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

d = 256
file = open("SampleSet.txt","r")
string=file.read()
file.close()
pat = "father"



################### timeit statement ##############

#print (timeit.timeit( stmt = '''get_keywords(pat,lst,sentences)''',globals = globals(), number = 10000)/10000) 
#print (timeit.timeit( stmt = '''search_rabin(string, lst,sentences)''',globals = globals(), number = 10000)/10000)
#print (timeit.timeit( stmt = '''saerching_orignal_algorithim(pat, string)''',globals = globals(), number = 10000)/10000)

