"""
1.
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc
"""
"""
s=input("enter str ")
l=""
for i in range(len(s)):
    t=""
    for j in range(i,len(s)):
        if s[j] in t:
            break
        t=t+s[j]
    if len(t)>len(l):
        l=t
print(l)
"""
"""
2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india
"""
"""
s = input("Enter Sentence : ")

rep = ""
ls = s.split()

high = 0

for ch in ls:
    count = 0
    for w in ls:
        if ch == w:
            count=count+1
    if count>high:
        rep = ch
        high = count
    
print(rep)
"""
"""
s = input("Enter String : ")
new = ""

for ch in s:
    if ch not in new:
        new = new + ch
    
print("Output : ",new)
"""
"""
s = input("Enter String: ")

max_freq = 0
result = ""

for ch in s:
    # 1. Count how many times 'ch' appears
    count = 0
    for i in range(len(s)):
        if s[i] == ch:
            count = count + 1
            
    if count > max_freq:
        max_freq = count
        result = ch + " "
        
    elif count == max_freq:
        already_exists = False
        for j in range(len(result)):
            if result[j] == ch:
                already_exists = True
                
        if not already_exists:
            result = result + ch + " "

print("Output:", result)
"""
