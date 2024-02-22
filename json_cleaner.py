#this python script opens a json file, reads the data, and replaces the key values with a placeholder text of the same data type
#the script then writes the data to a new json file
#this script is used to anonymize data for testing purposes

import json
import random
import string

#print out some sweet ascii art that says "JSON CLEANER"
print("      /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$")                              
print("     |__  $$ /$$__  $$ /$$__  $$| $$$ | $$")                             
print("        | $$| $$  \__/| $$  \ $$| $$$$| $$")                            
print("        | $$|  $$$$$$ | $$  | $$| $$ $$ $$")                              
print("   /$$  | $$ \____  $$| $$  | $$| $$  $$$$")                             
print("  | $$  | $$ /$$  \ $$| $$  | $$| $$\  $$$")                              
print("  |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$ \  $$")                             
print("   \______/  \______/  \______/ |__/  \__/")                                                                 
print("  /$$$$$$  /$$       /$$$$$$$$  /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$ ")
print(" /$$__  $$| $$      | $$_____/ /$$__  $$| $$$ | $$| $$_____/| $$__  $$")
print("| $$  \__/| $$      | $$      | $$  \ $$| $$$$| $$| $$      | $$  \ $$")
print("| $$      | $$      | $$$$$   | $$$$$$$$| $$ $$ $$| $$$$$   | $$$$$$$/")
print("| $$      | $$      | $$__/   | $$__  $$| $$  $$$$| $$__/   | $$__  $$")
print("| $$    $$| $$      | $$      | $$  | $$| $$\  $$$| $$      | $$  \ $$")
print("|  $$$$$$/| $$$$$$$$| $$$$$$$$| $$  | $$| $$ \  $$| $$$$$$$$| $$  | $$")
print(" \______/ |________/|________/|__/  |__/|__/  \__/|________/|__/  |__/")

#Let the user know that the file should be in the same directory as the script
print("Please ensure that the file you would like to anonymize is in the same directory as this script and is a .json file.")
#prompt the user for the name of the file they would like to anonymize
file_name = input("Please enter the name of the file you would like to anonymize: ")

#put the cleaning process into a function:
def clean(data):
    for key in data:
        if type(data[key]) == str:
            #replace it with a randomly generated string
            data[key] = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10))
        elif type(data[key]) == int:
            data[key] = 0
        elif type(data[key]) == float:
            data[key] = 0.0
        elif type(data[key]) == bool:
            data[key] = False
        elif type(data[key]) == list:
            data[key] = ["list"]
        elif type(data[key]) == dict:
            data[key] = {"dictionary"}
        else:
            data[key] = "unknown"
    return data


#open the file and read the data
with open(file_name, 'r') as file:
    data = json.load(file)

#check the data type of the loaded json.
#If it is a list, check the length of the list; we will iterate through the list and anonymize each dictionary in the list
#The returned data for each dictionary will be appended to the list
if type(data) == dict:
    data = clean(data)


#If it is a dictionary, we will anonymize the dictionary
if type(data) == list:
    for i in range(len(data)):
        data[i] = clean(data[i])


#output the new data as a file with the original file name and "_anonymized" appended to the end
with open(file_name[:-5] + "_anonymized.json", 'w') as file:
    json.dump(data, file, indent=4)

#let the user know that the file has been anonymized and the new file name
print("The file has been anonymized and saved as " + file_name[:-5] + "_anonymized.json")

#exit the program
exit()

#end of script


