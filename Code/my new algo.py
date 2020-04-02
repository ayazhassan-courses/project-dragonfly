import hashlib
import math

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
    lst = strings.split(".")
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
        return word


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
                lst[index]= [[sentences[i][j],[group_no]]]
                continue
            for h in range(len(lst[index])):
                if lst[index][h][0] == word:
                    if group_no not in  lst[index][0][1]:
                        lst[index][h][1].append(group_no)
                        bool_list= True
                if len(lst[index][h][1]) >= math.ceil(len(sentences)/2):
                    lst[index][h].append("Too common")
            if bool_list== False:
                lst[index].append([sentences[i][j],[group_no]])
            
    
    for i in range(len(lst)):   # removing common words
        if isinstance(lst[i],int):
            continue
        for j in range(len(lst[i])):
            if len(lst[i][j]) >= 3:
                del lst[i][j]
                break
    return lst


def search(word,lst,sentences):
    prime= len(lst)
    index,word1 = get_index(word,prime)
    print(lst[index])
    return

strings="hello everyone how are u today. we have descided to build this machine to test out what can we do. we will be changing how u will think"
sentences= make_lst(strings)

'''
lst= make_hashtable(sentences)

print(lst)
word= "machine"
search(word,lst,sentences)
'''
    







