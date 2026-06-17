#1Find the length of a string. S = "programming" 11
"""
s=input("enter your str : ")
l=len(s)
print(l)
"""



#2Copy one string to another. S1 = "source" S2 becomes "source"
"""
s=input("enter str : ")
s2=s
print("s2 become " ,s2)

"""



#3Concatenate two strings. S1 = "Hello", S2 = "World" "HelloWorld"
"""
s=input("enter your str: ")
s1=input("enter str")
print(s+s1)
"""

#4Compare two strings (case-sensitive). S1 = "Test", S2 = "test" Not Equal (or non-zero value)
"""
s1=input("enter str")
s2=input("enter str :")
if s1==s2:
    print("equal")
else:
    print("not equal")
    """
"""
s=input("enter str : ")
s1=input("enter str : ")
i=0
x=0
while i<len(s):
    ch=s[i]
    
    j=0
    while j<len(s1):
        chh=s1[j]
        if ch!=chh:
            x=1
            break
        
        j=j+1
    i=i+1
if x==0:
    print("eqa")
else:
    print("not eqaul")
"""





#5Compare two strings ignoring case. S1 = "Test", S2 = "test" Equal (or 0)
"""
s1=input("enter str: ").lower()
s2=input("enter str : ").lower()
if s1==s2:
    print("equal")
else:
    print("0")
"""

#6Convert a string to uppercase. S = "hello" "HELLO"
"""
s=input("enter str : ")
s1=s.upper()
print(s1)
"""
"""
s=input("enter str :")
re=""
for ch in s:
    
    if ch>="a" and ch<="z":
        upper=ord(ch)-32
        re=re+chr(upper)

    else:
        pass
print(re)
"""

#7Convert a string to lowercase. S = "HELLO" "hello"
"""
s=input("enter str : ")
s1=s.lower()
print(s1)
"""
"""
s=input("enter str :")
re=""
for ch in s:
    if ch>="A" and ch<="Z":
        upper=ord(ch)+32
        re=re+chr(upper)
    else:
        pass
print(re)
"""



#8Toggle the case of each character. S = "MiXED" "mIxeD"
"""
s=input("enter str :")
re=""
for ch in s:
    if ch>="A" and ch<="Z":
        upper=ord(ch)+32
        re=re+chr(upper)
    elif ch>="a" and ch<="z":
        upper=ord(ch)-32
        re=re+chr(upper)
    else:
        pass
print(re)

"""
#9Check whether a string is empty. S1 = "", S2 = "A" S1: True, S2: False
"""
s1=input("enter str : ")
s2=input("enter str : ")
if len(s1)==0:
    print(True)
else:
    print("FAlse")
if len(s2)!=0:
    print("False")
else:
    print("True ")

"""


#10Trim leading, trailing, or extra spaces. S = "  hello  world  " "hello world"
"""
s=input("enter str :")
s1=s.split()
print(" ".join(s1))
"""
"""
s=input("enter str ")
r=""
for i in s:
    if i==" ":
        if r=="":
            pass
        else:
            if r[len(r)-1]!=" ":
                r=r+i
    else:
        r=r+i
    
print(r)
    """    
 
#11Get the character at a given index. S = "Python", Index = 2 t'
"""
n=input("enter str : ")
i=int(input("enter index"))
print("index == ",i,n[i])
"""


#12Get the Unicode code point of a character at index. S = "A", Index = 0 65
"""
s=input("enter str : ")
ch=input("enter character : ")
i=int(input("enter index : "))

print( "ch",ch,"index =",i,s[i],ord(ch))


"""

#13Get the Unicode code point before index. S = "Hello", Index = 1 72 (Unicode for 'H')
"""
s=input("enter str : ")
i=int(input("enter index : "))
o=ord(s[i])
print("str",s,"index",i,"=",o)

"""

#14Find the first occurrence of a character. S = "banana", Char = 'a' 1 (index)
"""
s=input("enter str : ")
chr=input("enter character")
print("index",s.index(chr))
"""






#15Find the last occurrence of a character. S = "banana", Char = 'a' 5 (index)
"""
s=input("enter str : ")
chr=input("enter character")
i=len(s)-1
while i>=0:
    if s[i]==chr:
        print(i)
        break
    else:
        pass
    i=i-1

"""

#16Count total occurrences of a character. S = "programming", Char = 'g' 2
"""
s=input("enter str : ")
ch=input("enter str  :")
i=0
c=0
while i<len(s):
    if s[i]==ch:
        c=c+1
    else:
        pass
    i=i+1
print("count",c)
"""


#17Remove occurrences of a character. S = "banana", Char = 'a', Remove All "bnn"
"""
s=input("enter str : ")
ch=input("enter character : ")
i=0
r=""
while i<len(s):
    if s[i]==ch:
        pass
    else:
        r=r+s[i]
    i=i+1
print(r)
"""

#18Replace occurrences of a character. S = "apple", Old='p', New='x' "axxle"
"""
s=input("enter str : ")
s1=s.replace("p","x")
print(s1)


"""
"""
s=input("enter str ")
o="p"
n="x"
r=""
for i in s:
    if i==o:
        r=r+n
    else:
        r=r+i
print(r)
"""
#19Find the highest frequency character. S = "abracadabra" a'
"""
s=input("enter str :")

c=0
hc=0
for i in s:
    j=0
    c=0
    for j in s:
        if i==j:
            c=c+1
    else:
        if hc<c:
            hc=c
            ch=i
print(ch)
print(hc)

"""







#20Find the lowest frequency character. S = "aabbcde" c', 'd', 'e' (any one or all)
"""
s=input("enter str : ")
l=len(s)
lc=l
ch=""
for i in s:
    c=0
    for j in s:
        if i==j:
            c=c+1
    else:
        if lc>c:
            lc=c
            ch=i
        elif lc==c:
             ch=ch+" "+i
print(ch)
print(lc)
"""


#21Find the first non-repeating character. S = "aabbcde" c'
"""
s=input("enter str : ")
lc=len(s)
ch=""
for i in s:
    c=0
    for j in s:
        if i==j:
            c=c+1
    else:
        if lc>c:
            lc=c
            ch=i
print(ch)
print(lc)

"""
#22Find the last repeating character. S = "abracadabra" r'
"""
s=input("Enter the String: ")
s1=""

for i in s:
    c=0
    for j in s:
       if i==j:
          c=c+1
    else:
        if c>=2:
           s1=i
print(s1)


"""

#23Print all characters that occur exactly twice. S = "aabbcdee" b', 'e'
"""
s=input("enter str : ")
s1=""
for i in s:
    if not i in s1:
        s1=s1+i
        c=0
        for j in s:
            if i==j:
                c=c+1
        else:
            if c==2:
                print(i,end="")


"""

#24Check if all characters in a string are unique. S1 = "abc", S2 = "abca" S1: True, S2: False
"""
s=input("enter str : ")
s1=input("enter str :")
a=""
b=""
for i in s:
    if i not  in a:
        a=a+i
    else:
        print("s","False")
        break
else:
    print("s","True")
for j in s1:
    if j not in b:
        b=b+j
    else:
        print("s1","False")
        break
else:
    print("s1","True")

"""




#25Count total words in a string. S = "This is a test" 4
"""
s=input("enter str :")
s1=s.split()
l=len(s1)
print(l)

"""
"""
s=input("enter str :")
s1=s.split()
c=0
for i in s1:
    c=c+1
print(c)
"""

#26Find the first occurrence of a word. S = "Test this test", Word = "test" 10 (index)
"""
s=input("enter")
sub=input("enter word")
index=s.index(sub)
print(index)
"""
"""
s=input("enter str : ")
sub=input("enter wor")
flag=False
i=0
while i<=len(s)-len(sub):
    ch=s[i]
    if ch==sub[0]:
        j=0
        k=i
        while j<len(sub):
            if s[k]==sub[j]:
              
                j=j+1
                k=k+1
            else:
                break
            
        else:
            print(i)
            flag=True
            break
    i=i+1
if flag==False:
    print("substring not found")
"""



#27Find the last occurrence of a word. S = "Test this test", Word = "test" 15 (index)

"""
s=input("enter str : ")
sub=input("enter substring  ")
x=0
c=0
i=0

while i<len(s)-len(sub):
    ch=s[i]
    if ch==sub[0]:
        j=0
        k=i
        while j<len(sub):
            if s[k]==s[j]:
                k=k+1
                j=j+1
            else:
                break
        else:
            m=i
            c=c+1
            x=1
    i=i+1
if x==0:
    print("not fount")
else:
    print(c)
    print(m)

"""

#28Count occurrences of a word. S = "word word other word", Word = "word" 3
"""
s=input("enter str : ")
w=input("word")
s1=s.split()
c=0
for i in s1:
    if i==w:
        c=c+1
    else:
        pass
print(c)

"""

#29Remove occurrences of a word. S = "a test b test c", Word = "test", Remove All "a b c"
"""
s=input("enter str : ")
w=input("word : ")
s1=s.split()
c=""
for i in s1:
    if i==w:
        pass
    else:
        c=c+" "+i
print(c)
"""

#30Replace a word with another word. S = "old data", Old="old", New="new" "new data"
"""
s=input("enter str  : ")
print(s.replace("old","new"))

"""
"""
s=input("enter str : ")
s1=s.split()
o="old"
n="new"
r=""
for i in s1:
    if i==o:
        r=r+n
    else:
        r=r+" "+i
print(r)
"""

#31Remove duplicate words. S = "the cat and the dog" "the cat and dog"
"""
s=input("enter str : ")
s1=s.split()
r=""
for i in s1:
    if i not in r:
        r=r+" "+i
    else:
        pass
print(r)
"""

#32Count frequency of each word. S = "apple banana apple" apple: 2, banana: 1
"""
s=input("enter str : ")
s1=s.split()
r=""
c=0
for i in s1:
    if i not in r:
        r=r+i
        c=0
        for j in s1:
            if i==j:
                c=c+1
        else:
            print(i,":",c,end="")
"""
#33Find the longest word. S = "find the longest word" "longest"
"""
s=input("enter str : ")
s1=s.split()
l=0

for i in s1:
    j=0
    c=0
    while j<len(i):
        c=c+1
        j=j+1
    else:
        if l<c:
            l=c
            ch=i

print(ch)
"""


#34Find the shortest word. S = "find the shortest word" "the"
"""
s=input("enter str : ")
s1=s.split()
l=len(s)

for i in s1:
    c=0
    j=0
    while j<len(i):
        c=c+1
        j=j+1
    else:
        if l>c:
            l=c
            ch=i

print(ch)
"""

#35Find the first palindrome word. S = "this madam is here" "madam"
"""
s=input("enter str : ")
s1=s.split()
x=0
for i in s1:
    if i==i[::-1]:
        print(i,"palindrome")
    else:
        pass
"""

#36Reverse order of words. S = "one two three" "three two one"
"""
s=input("enter str  : ")
s1=s.split()
i=0
r=""
while i<len(s1):
    ch=s1[i]
    r=ch+" "+r
    i=i+1
print(r)

"""

#37Reverse each word. S = "cat dog" "tac god"
"""
s=input("enter str  :")
s1=s.split()

for i in s1:
    r=""
    for j in i:
        r=j+r
    else:
        print(r,end=" ")

"""


#38Reverse words without split(). S = "a b c" "c b a"
"""
s=input("enter str : ")
r=""
for i in s:
   
    if i==" ":
        pass
    else:
        r=i+" "+r
print(r)
"""




#39Search all occurrences of a character. S = "banana", Char='a' 1, 3, 5 (indices)
"""
s=input("enter str : ")
ch=input("charcter : ")

for i in range(len(s)):
    if s[i]==ch:
        print(i,end=" ")
   
"""


#40Search all occurrences of a word. S = "a b a b", Word='b' 2, 6 (start indices)
"""
s=input("enter str : ")
ch=input("enter character")
for i in range(len(s)):
    if s[i]==ch:
        print(i,end=" ")

"""
"""
s=input("enter str : ")
ch=input("enter character")
i=0
while i<len(s):
    if s[i]==ch:
        print(i,end=" ")
    i=i+1
"""
#41Check if a string contains a substring (without using built-in method). S1 = "Hello", Sub="ell" TRUE

    









#42Check if two strings are equal without equals(). S1 = "abc", S2 = "abc" TRUE
"""
s1=input("enter str  :")
s2=input("enter str2: ")
r=""
for i in s1:
    r=r+i

r1=""
for j in s2:
    r1=r1+j
if r==r1:
    print("True")
else:
    print("False")

"""


#43Check if two strings are rotations of each other. S1 = "abcde", S2 = "cdeab" TRUE
"""
s1=input("enter str : ")
s2=input("enter str2 : ")

if len(s1)==len(s2):
    for i in s1:
        if i.count(s1)!=i.count(s2):
            print("not qual")
            break
        else:
            pass
    else:
        print("TRUE")
else:
    print("False")

"""





#44Check if two strings are anagrams. S1 = "listen", S2 = "silent" TRUE
"""
s1=input("enter str1")
s2=input("enter str2")
if sorted(s1)==sorted(s2):
    print("TRUE")
else:
    print("FALSE")
"""
"""
s1=input("enter str1")
s2=input("enter str2")
if len(s1)==len(s2):
    for i in s1:
        if s1.count(i)==s2.count(i):
            print("not anagram")
            break
        else:
            pass
    else:
        print("anagram")
else:
    print("not anagram")

 """           


#45Check whether a string starts/ends with another string. S = "apple pie", Prefix = "apple", Suffix = "pie" Start: True, End: True
"""
s=input("enter str : ")
s1=s.split()
pre=input("enter prefix ")
suf=input("enter suffix ")
start=s1[0]
end=s1[-1]
if pre==start:
    print("prefix=",pre)
    print("TRUE")
else:
    print("FALSE")
if suf==end:
    print("suffix=",suf)
    print("TRUE")
else:
    print("FALSE")

"""
#46 Check if a substring appears at both the start and end. S = "abcabca", Sub = "abca" TRUE

    




#47 Check if one string is a substring of another using only concatenation. S1 = "CDAB", S2 = "ABCD" S1 is substring of S2S2 (ABCDABCD) → True
#48 Remove all vowels. S = "aeiou XYZ" " XYZ"
"""
s=input("enter str : ")
i=0
r=""
while i<len(s):
    ch=s[i]
    if (ch!="a" and ch!="e" and ch!="i" and ch!="o" and ch!="u") and (ch!="A" and ch!="E" and ch!="I" and ch!="O" and ch!="U"):
        r=r+ch
    else:
        pass
    i=i+1
print(r)
"""

#49 Replace all consonants with ''. S = "apple" "ae"
"""
s=input("enter str ")
i=0
r=""
while i<len(s):
    ch=s[i]
    
    
    if (ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" )or (ch=="A" or ch=="E" or ch=="O" or ch=="I" or ch=="U"):
        r=r+ch
    else:
        pass
    i=i+1
print(r)

"""






#50 Remove all digits. S = "a1b2c3" "abc"
"""
s=input("enter str ")
i=0
r=""
while i<len(s):
    ch=s[i]
    if ch>="a" and ch<="z":
        r=r+ch
    else:
        pass
    i=i+1
print(r)

"""




#51 Extract only digits. S = "a1b2c3" "123"
"""
s=input("enter str ")
i=0
r=""
while i<len(s):
    ch=s[i]
    if ch>="0" and ch<="9":
        r=r+ch
    else:
        pass
    i=i+1
print(r)
"""





#52 Remove all special characters. S = "a!@b#c" "abc"
"""
s=input("enter str ")
i=0
r=""
while i<len(s):
    ch=s[i]
    if ch>="a" and ch<="z":
        r=r+ch
    else:
        pass
    i=i+1
print(r)

"""
#53 Remove all punctuation characters. S = "Hello, world!" "Hello world
"""
s=input("enter str ")
i=0
r=""
while i<len(s):
    ch=s[i]
    if ch>="a" and ch<="z" or ch==" ":
        r=r+ch
    else:
        pass
    i=i+1
print(r)

"""
#54 Replace all duplicate characters with '$'. S = "hello" "he$lo"
#55 Reverse only vowels. S = "hello" "holle"
#56 Reverse only consonants. S = "apple" "eplpa"
#57 Merge two strings alternatively (char by char). S1 = "ABC", S2 = "def" "AdBeCf"
#58 Rotate characters by 2 positions to the left. S = "abcde" "cdeab"
#59 Rotate characters by 3 positions to the right. S = "abcde" "cdeab"
#60 Append two strings but remove duplicate adjacent characters. S1 = "miss", S2 = "issippi" "misisipi"

  





#61 Count total alphabets, digits, and special characters. S = "a1b!c2" Alphabets: 3, Digits: 2, Special: 1
"""
s=input("enter str ")
i=0
l=len(s)
a=0
d=0
sp=0
while i<l:
    ch=s[i]
    if ch>="a" and ch<="z":
        a=a+1
    elif ch>="0" and ch<="9":
        d=d+1
    else:
        sp=sp+1
    i=i+1
print("alphabets",a,"digit=",d,"special=",sp)

"""

#62 Count vowels and consonants. S = "apple" Vowels: 2, Consonants: 3
"""
s=input("enter str ").lower()
v=0
c=0
i=0
while i<len(s):
    ch=s[i]
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        v=v+1
    else:
        c=c+1
    i=i+1
print("vowel =",v)
print("consonent=",c)
"""




##63 Count frequency of each character. S = "aabcc" a: 2, b: 1, c: 2
"""
s=input("enter str")
r=""
i=0
c=0
while i<len(s):
    ch=s[i]
    if ch in r:
        r=r+ch
        c=c+1
    else:
        r=r+ch
        
    i=i+1
print(r)
print(c)

    

"""



#64 Count frequency of each vowel. S = "programming" o: 1, a: 1 (e, i, u: 0)
#65 Count palindromic substrings. S = "aaa" 6 (a, a, a, aa, aa, aaa)
#66 Count number of sentences in a paragraph.
"""
s=input("enter str ")
s1=s.split()
c=0
for i in s1:
    c=c+1
print(c)

"""
#67Count how many times a substring appears. S = "abab", Sub = "ab" 2
"""
s=input("enter str ")
ss=input("enter substr")
print(s.count(ss))

"""







#68Count the sum of digits present in a string. S = "a1b2c3" 6 (1+2+3)
"""
s=input("enter str ")
c=0
for i in s:
    if i>="0" and i<="9":
        c=c+int(i)
        
    else:
        pass
print(c)

"""

#69Count how many times 'life' appears in a string. S = "life is life" 2
"""
s=input("enter str")
c=0
s1=s.split()
for i in s1:
    if i=="life":
        c=c+1
print(c)

"""
#51Extract only digits. S = "a1b2c3" "123"
""" n=input("Enter the n:")
d=""
for i in n:
    if "a"<=i<="z":
        continue
    else:
        d+=i 
print(d) """
#52Remove all special characters. S = "a!@b#c" "abc"
""" n=input("Enter the string:").lower()
alpha="qwertyuiopasdfghjklzxcvbnm"
rev=""
for i in n:
    if i  in alpha:
            rev=rev+i 
print(rev)  """

#53Remove all punctuation characters. S = "Hello, world!" "Hello world"
""" n=input("Enter the string:")
alpha="qwertyuiopasdfghjklzxcvbnmQWERTYUIOKJHGFDSAZXCVBNM "
rev=""
for i in n:
    if i  in alpha:
            rev=rev+i 
print(rev)  """
#54Replace all duplicate characters with '$'. S = "hello" "he$lo"
""" n=input("Enter the string:")
rev=""
i=1
while i<=len(n):
    n[i]==n[i+1]
    rev=rev+n[i]+"$"
print(rev)
 """



#55Reverse only vowels. S = "hello" "holle"




#56Reverse only consonants. S = "apple" "eplpa"

#57Merge two strings alternatively (char by char). S1 = "ABC", S2 = "def" "AdBeCf"
""" s1=input("Enter the n:")
s2=input("Enter the s2:")
d=""
for i in range(len(s1)):
    d+=s1[i]
    d+=s2[i] 
print(d)    
 """


#58Rotate characters by 2 positions to the left. S = "abcde" "cdeab"
""" s1=input("Enter the n:")
n=2
s2=s1[n:]+s1[:n]
print(s2) """
#59Rotate characters by 3 positions to the right. S = "abcde" "cdeab"
""" s1=input("Enter the n:")
n=3
s2=s1[n:]+s1[:n]
print(s2) """
#60Append two strings but remove duplicate adjacent characters. S1 = "miss", S2 = "issippi" "misisipi" 
""" s1 = input("Enter the s1:")
s2 = input("Enter the s2:")
combined = s1 + s2
result = "" 

for char in combined:
    if not result or result[-1] != char:
        result += char

print(result)  
 """
#61Count total alphabets, digits, and special characters. S = "a1b!c2" Alphabets: 3, Digits: 2, Special: 1

#62Count vowels and consonants. S = "apple" Vowels: 2, Consonants: 3

#63Count frequency of each character. S = "aabcc" a: 2, b: 1, c: 2
""" n=input("Enter the n:")
rev=""
for i in n:
    if i not in rev:
        print(i,":",n.count(i)) 
        rev=i+rev """

#64Count frequency of each vowel. S = "programming" o: 1, a: 1 (e, i, u: 0)
""" n=input("Enter the n:")
vowel="aeiou"
for i in n:
    if i in vowel:
        print(i,":",n.count(i)) """

#65Count palindromic substrings. S = "aaa" 6 (a, a, a, aa, aa, aaa)
""" string=input("Enter the string:")
for i in  range(len(string)):
    for j in range(i+1,len(string)+1):
        sub=string[i:j]
        print(sub) 
 """
#66Count number of sentences in a paragraph. P = "This. Is. Test." 3


#67Count how many times a substring appears. S = "abab", Sub = "ab" 2
""" string=input("Enter the string:")
sub=input("Enter the substring:")
rev=[]
count=0
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        s1=string[i:j]
        rev.append(s1)

for i in rev:
    if sub==i:
        count+=1
print(sub,":",count)
 """
#68Count the sum of digits present in a string. S = "a1b2c3" 6 (1+2+3)
""" n=input("Enter the string:")
digit="0123456789"
rev=""
sum=0
for i in n:
    for j in digit:
            if i==j:
                sum+=int(i)
print(sum) """
#69Count how many times 'life' appears in a string. S = "life is life" 2

#70Compare the number of times 'the' and 'is' appear. S = "the cat is on the mat" the: 2, is: 1 (theis)
""" string=input("Enter the sttring:")
s1=input("Enter the sttring:")
s2=input("Enter the sttring:")
rev=[]
for i in range(len(string)):
    for j in range(i+1,len(string)):
        s=string[i:j]
        rev.append(s)
if s1 in rev:
    print(s1,":",rev.count(s1))
if s2 in rev: 
    print(s2,":",rev.count(s2))  

"""
#71Print all substrings. S = "abc" "a, b, c, ab, bc, abc"
""" n=input("Enter the n:")
ss=[]
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        ss.append(n[i:j])
print(ss) """  

#72Print all substrings of length n. S = "ab…




#70Compare the number of times 'the' and 'is' appear. S = "the cat is on the mat" the: 2, is: 1 (theis)
"""
s=input("enter str :")
s1=s.split()

print("the",s1.count("the"))
print("is",s1.count("is"))
"""
    

#71Print all substrings. S = "abc" "a, b, c, ab, bc, abc"








#72Print all substrings of length n. S = "abc", n = 2 "ab, bc"
#73Find the longest palindromic subs







