"""
1. Count Vowels

Write a program to count the number of vowels in a string.

Input

s = "Programming"

Output

Vowels = 3
"""
"""
s=input("enter your string: ").lower()
c=0
for i in s:
    if i=="a" or i=="e" or i=="o" or i=="i" or i=="u" :
        c=c+1
    else:
        pass
print("total vowel count",c)
"""
"""
2. Reverse a String

Reverse a string without using slicing ([::-1]).

Input

s = "Python"

Output

nohtyP
"""
"""
s=input("enter your string: ")
sum=""
for i in s:
    sum=i+sum
print(sum)
"""
"""
3. Check Palindrome

Check whether a string is a palindrome.

Input

s = "madam"

Output

Palindrome
"""
"""
s=input("enter your string: ")
sum1=s
sum=""
for i in s:
    sum=i+sum
if sum==sum1:
    print("palindrome")
else:
    print("not palindrome")
"""
"""
4. Character Frequency

Print the frequency of every character without using count().

Input

s = "banana"

Output

b -> 1
a -> 3
n -> 2
"""
"""
s=input("enter your string: ")
v=""
for i in s:
    c=0
    if i not in v:
        for j in s:
            if i==j:
                c=c+1
     
        print(i,"-->",c)
        v=v+i
"""
"""
5. Remove Duplicate Characters

Remove duplicate characters while preserving the original order.

Input

s = "programming"

Output

progamin
"""
"""
s=input("enter your string: ")
v=""

for i in s:
    if i not in v:
        v=v+i
    else:
        pass
print(v)
"""
"""
6. Longest Word in a Sentence

Find the longest word in a sentence.

Input

s = "Python is an amazing programming language"

Output

programming
"""
"""
s=input("enter your string: ")
s1=s.split()
print(s1)
max=""
for i in s1:
    if len(str(i))>len(str(max)):
        max=i
print(max)
"""
"""

7. Count Occurrences of a Substring

Count how many times a substring appears in a string without using count().

Input

text = "abababa"
sub = "aba"

Output

3
"""
"""
s=input("enter your string: ")
ss=input("enter substring: ")
print(s.count(ss))

"""

