# Write the solution for "Longest Word".
import re
import os
count= 0
word=''
path= "/Users/smrithichakravarthy/ctci---regex-and-io-smrithi-c/inputs/longest.txt"
file= open(path,"r+")
for line in file.readlines():
            sentence=line.split()
            for part in sentence:
                if(len(part)>count):
                   count=len(part)
                   word=part
                  
file.seek(0)

new_word= re.sub(f"{word}", f"**{word}**" , word)
for line in file.readlines():
            if word in line:
                    print('found')
                    file.write(line.replace(word,new_word))
                  

            
file.close()
