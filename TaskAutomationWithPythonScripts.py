import re
import os

#Input source and destination file path
source_path = input("Enter path of .txt file:")
Destination_path = input("Enter path of new .txt file: ")

#Find file is exist or not using 'os' library
if not  os.path.isfile(source_path):
    print("Does not exist file")
else:
    #Read txt file
    with open(source_path, 'r') as f:
        file = f.read()

# All types of Email pattern for 're' library
emailPatterns = r"\b[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"

# re library used to find emails using email pattern in List class
emailsMatch = re.findall(emailPatterns, file)
#convert List to String class
allEmails = '\n'.join(emailsMatch)

#Create new file other wise not existing thus file and write all emails inside thus txt file
with open(Destination_path, 'w') as f:
    f.write(allEmails)

