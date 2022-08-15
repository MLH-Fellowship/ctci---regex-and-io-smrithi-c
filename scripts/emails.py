# Write the solution for "New Emails".
import csv
import re

f = open("email_output.txt", "w")
valid = ".@gmail\.com"
path="/Users/smrithichakravarthy/ctci---regex-and-io-smrithi-c/inputs/emails.csv"
f.write("abhorrence@mlh.io")
f.write("\n")
with open(path) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        old_email=row["abhorrence@gmail.com"]
        if re.search(valid,old_email):
           f.write(old_email.replace("gmail.com","mlh.io"))
        else:
            f.write(old_email)
        f.write("\n")
           
f.close();
csv_file.close();
    
