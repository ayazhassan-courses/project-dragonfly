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
    lst = strings.split("\n")
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
        strings+= "("+str(i+1)+")"+" ".join(sentences[result[i]])+"\n"
    return strings


file = open("SampleSet.txt","r")
st= file.read()
sentences = make_lst(st)
lst =make_hashtable(sentences)
pat= "father today"
print(get_keywords(pat,lst,sentences))

import cProfile
cProfile.run('get_keywords(pat,lst,sentences)')


'''
root2 = tk.Tk()
root2.withdraw()
path =filedialog.askopenfilename()
count =0
root = tk.Tk()
root.title('Search bar')
root.configure(background="#1d8fdb")
root.geometry("850x550")
root.resizable(0, 0)
label_search= tk.Label(root,text = "Enter keywords",background="#1d8fdb")
label_search.grid(row = 0, column = 1, pady = 2)
entry = tk.Entry(root,width = 40, )
entry.grid(row = 2, column = 2, pady = 2)
text = tk.Text(root,)
text.grid(row = 5, column = 2, pady = 2)
file = open(path,"r")
strings_set= file.read()
file.close()
sentences= make_lst(strings_set)
lst= make_hashtable(sentences)
def get_vals(event):
    text.delete('1.0', tk.END)
    string=""
    string = entry.get()
    if string != "":
        s= get_keywords(string,lst,sentences)
    else:
        s= "Enter keyword"
    
    text.insert(tk.END, s)
    
    return
def get_val():
    text.delete('1.0', tk.END)
    string=""
    string = entry.get()
    if string != "":
        s= get_keywords(string,lst,sentences)
    else:
        s= "Enter keyword"
    
    text.insert(tk.END, s)
    
    return

root.bind('<Return>', get_vals)

label_search= tk.Label(root,text = "Results:",background="#1d8fdb")
label_search.grid(row = 4, column = 1, pady = 2)

button= tk.Button(root, text ="search", command = get_val,height=2, width=15 )
button.grid(row = 3, column = 3, pady = 2)


root.mainloop()

'''
