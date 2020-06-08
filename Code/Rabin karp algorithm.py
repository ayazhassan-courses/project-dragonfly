  
def search(pat, txt, q): 
    M = len(pat) 
    N = len(txt) 
    i = 0
    j = 0
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

  
def extract (txt):
    temp=""
    dic=[]
    string=""
    for i in  txt:
        if i == "," or i ==".":
            continue
        if i == " "  and temp != "":
            
            if temp in dic:
                temp=""
                continue
            temp = fuzzy_word(temp)
            string += temp
            temp=""
        temp+=i
    return string

d = 256
txt = "hello everyone how are you guys. we have descided to build this algorithim  to test out what it can do . Rabin karp uses naive approach to traverse through a given string. we will be using hash tables"
pat = "to" 
q = 201
search(pat, txt, q) 
print(extract (txt))  
