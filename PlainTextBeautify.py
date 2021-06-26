"""                                      
      First publication date : 2020 / 11 / 1
      Author : 張哲銘(CHANG, CHE-MING)
"""
import sys
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
    if beautify_char == []:
        print("Input three string follow a sequence:\nall_beautify_char (String)\nright_beautify_char (String)\npointer (True or False)")
        for i in range(3):
            beautify_char.append(input())
    if beautify_char == -1:
        sys.exit(0)
    textfile_path = input("Input your Text file path: (Example: D:\\Users\\user\\Desktop\\test.txt)\n")
    f = open(textfile_path, 'r+', encoding = 'utf8')
except:
    print("Program terminated with wrong input.")
    sys.exit(1)
    
print("-----Begin -----") 
for line in f:
    for position in range(len(beautify_char[0])):
        next_position = line.rfind(beautify_char[0][position])
        for times in range(line.count(beautify_char[0][position])):
            if beautify_char[0][position] == "*" and beautify_char[2] == True and any(keyword in line.split()[0] for keyword in c_type_keyword):
                for position in range(len(list(filter(None, re.split(" |, |,|;", line)))) - 1):
                    if "*" in (list(filter(None, re.split(" |, |,|;", line))))[position + 1]:
                        beautify_char[3].append((list(filter(None, re.split(" |, |,|;", line))))[position + 1])
                break
            if "".join(line.split())["".join(line.split()).rfind(beautify_char[0][position], 0, next_position + 1) - 1] == '=':
                next_position = line.rfind(beautify_char[0][position], 0, next_position)
                continue
            elif beautify_char[0][position] == "*" and beautify_char[2] == True and any(pointer in line for pointer in beautify_char[3]):
                for pointer_position in range(len(beautify_char[3])):
                    if beautify_char[3][pointer_position] in line and line.index(beautify_char[3][pointer_position]) <= line.rfind(beautify_char[0][position], 0, next_position + 1) and line.index(beautify_char[3][pointer_position]) + len(beautify_char[3][pointer_position]) - 1 >= line.rfind(beautify_char[0][position], 0, next_position + 1):
                        print("|")
                        continue
                    
            elif beautify_char[0][position] == "=" and line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] not in " =":
                line = line[:line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] + ' ' + line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1:]
            elif line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] not in " '\"=" and line[line.rfind(beautify_char[0][position], 0, next_position+1) + 1] != beautify_char[0][position]:
                line = line[:line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] + ' ' + line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1:]
            if line[line.rfind(beautify_char[0][position], 0, next_position + 1) - 1] not in " '\"=" and line[line.rfind(beautify_char[0][position], 0, next_position + 1) - 1] not in beautify_char[0] and line[line.rfind(beautify_char[0][position], 0, next_position + 1)] not in beautify_char[1]:
                line = line[:line.rfind(beautify_char[0][position], 0, next_position + 1)] + ' ' + line[line.rfind(beautify_char[0][position], 0, next_position + 1):]
            next_position = line.rfind(beautify_char[0][position], 0, next_position)
    print(line, end = "")
    beautify_list.append(line)

print("\n-----End -----")
ans = input("\n-----Change? Y/N-----\n") 
if ans.upper() == "Y" or ans.upper() == "YES":
    f.seek(0)
    f.writelines(beautify_list)
f.close()
