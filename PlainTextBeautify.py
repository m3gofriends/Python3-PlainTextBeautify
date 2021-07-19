"""                                      
      First publication date : 2020 / 11 / 1
      Author : 張哲銘(CHANG, CHE-MING)
"""

""" Pure Python version """

from os import rename, remove
from sys import exit as sys_exit
import re

programming_language_dic = { #["all_beautify_char", "right_beautify_char", "pointer", "pointer_list"]
    0 : ["+-*/%=!><&|^,", ",", False], #Support Python
    1 : ["+-*/%=!><&|?^,", ",", True, []], #Support C, C++, C#
    2 : []
    }

c_type_keyword = ["void", "char", "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union", "enum", "typedef"]

beautify_list = []

try:
    beautify_char = programming_language_dic.get(int(input("Input your programming language number:\n0 : Support Python\n1 : Support C, C++, C#\n2 : Input string by yourself\n")), -1)
    if beautify_char == -1:
        sys_exit(0)
        
    elif beautify_char == []:
        print("Input three string follow a sequence:\nall_beautify_char (String)\nright_beautify_char (String)\npointer (True or False)")
        for i in range(3):
            beautify_char.append(input())
            
    file_path = input("Input your Text file path: (Example: C:\\Users\\user\\Desktop\\test.txt)\n")
    file_name = file_path.split("\\")[-1]
    file = open(file_path, 'r+', encoding = 'utf8')
    
except:
    print("Program terminated with wrong input.")
    sys_exit(1)
    
print("----- Begin -----")

for line in file:
    for position in range(len(beautify_char[0])):
        next_position = line.rfind(beautify_char[0][position])
        for times in range(line.count(beautify_char[0][position])):
            if beautify_char[0][position] == "*" and beautify_char[2] == True and any(keyword in line.split()[0] for keyword in c_type_keyword):
                for position in range(len(list(filter(None, re.split(" |, |,|;", line)))) - 1):
                    if "*" in (list(filter(None, re.split(" |, |,|;", line))))[position + 1]:
                        beautify_char[3].append((list(filter(None, re.split(" |, |,|;", line))))[position + 1])
                break
            
            elif beautify_char[0][position] == "*" and beautify_char[2] == True and any(pointer in line for pointer in beautify_char[3]):
                for pointer_position in range(len(beautify_char[3])):
                    if beautify_char[3][pointer_position] in line and line.index(beautify_char[3][pointer_position]) <= line.rfind(beautify_char[0][position], 0, next_position + 1) and line.index(beautify_char[3][pointer_position]) + len(beautify_char[3][pointer_position]) - 1 >= line.rfind(beautify_char[0][position], 0, next_position + 1):
                        continue
                    
            elif beautify_char[0][position] == "=" and line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] not in " =":
                line = line[:line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] + ' ' + line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1:]
                
            elif line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] not in " '\"=" and line[line.rfind(beautify_char[0][position], 0, next_position+1) + 1] != beautify_char[0][position]:
                line = line[:line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] + ' ' + line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1:]
                
            if line[line.rfind(beautify_char[0][position], 0, next_position + 1) - 1] not in " '\"=" and line[line.rfind(beautify_char[0][position], 0, next_position + 1) - 1] not in beautify_char[0] and line[line.rfind(beautify_char[0][position], 0, next_position + 1)] not in beautify_char[1]:
                line = line[:line.rfind(beautify_char[0][position], 0, next_position + 1)] + ' ' + line[line.rfind(beautify_char[0][position], 0, next_position + 1):]
                
            next_position = line.rfind(beautify_char[0][position], 0, next_position)
            
    beautify_list.append(line)

file_copy_path = file_path[:-len(file_name)] + file_name.split(".")[0] + "_copy." + file_name.split(".")[-1]
file_copy = open(file_copy_path, 'w+', encoding = 'utf8')
file_copy.writelines(beautify_list)
file_copy.seek(0)
print(file_copy.read())

print("----- End -----")

ans = input("\n----- Want to change file? Y/N -----\n")

if ans.upper() == "Y" or ans.upper() == "YES":
    file.close()
    remove(file_path)
    file_copy.close()
    rename(file_copy_path, file_path)
    print("File was changed!")
    
else:
    file_copy.close()
    remove(file_copy_path)
    file.close()
    print("Nothing change.")