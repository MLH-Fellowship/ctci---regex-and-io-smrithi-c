# Write the solution for "Filter Vowels".
import re
import os
vowels = {'a' , 'e' , 'i' , 'o' , 'u' }
count=0;
path= "/Users/smrithichakravarthy/ctci---regex-and-io-smrithi-c/inputs/vowels.txt"
file= open(path,"r")
for line in file.readlines():
    
    for word in line:
        
        for letter in word:
            
            if(letter in vowels):
                count+=1


file.close()
print(count)
newPath = re.sub('vowels', f"vowels_{count}" , path)
os.rename(path, newPath)
            
    

    
