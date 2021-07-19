"""                                      
      First publication date : 2020 / 11 / 1
      Author : 張哲銘(CHANG, CHE-MING)
"""

""" Cython version """

from os import rename, remove
from sys import exit as sys_exit
from Cython_module import Cython_PlaintextProcessing

programming_language_dic = { #["all_beautify_char", "right_beautify_char", "pointer", "pointer_list"]
    0 : ["+-*/%=!><&|^,", ",", False], #Support Python
    1 : ["+-*/%=!><&|?^,", ",", True, []], #Support C, C++, C#
    2 : []
    }

c_type_keyword = ["void", "char", "short", "int", "long", "float", "double", "signed", "unsigned", "struct", "union", "enum", "typedef"]

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

beautify_list, file_copy, file_copy_path = Cython_PlaintextProcessing.plaintext_processing(beautify_char, c_type_keyword, file, file_path, file_name)

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