# Write the solution for "Split the files".
import re
import os
word=''
path= "/Users/smrithichakravarthy/ctci---regex-and-io-smrithi-c/inputs/split/github.txt"
file=open(path,"r+")
first_line=file.read().split()
first=len(first_line)
print(first)
count=0
new_path=path.replace('github.txt',f'dist./github_1.txt')
file2=open(new_path,"w")
for i in range(0,int(first*0.33)):
    file2.write(' ')
    file2.write(first_line[i])
file2.close()

new_path=path.replace('github.txt',f'dist./github_2.txt')
file2=open(new_path,"w")
for i in range(int(first*0.33),int(first*0.66)):
    file2.write(' ')
    file2.write(first_line[i])
file2.close()
new_path=path.replace('github.txt',f'dist./github_3.txt')
file2=open(new_path,"w")
for i in range(int(first*0.66),first):
    file2.write(' ')
    file2.write(first_line[i])
file2.close()

  
                  
                        
                          
                        
               
   
               
               
             
               
                    
                

        
            
            
file.close()



