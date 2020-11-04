import sys

programming_language_dic = { #["all_beautify_char", "right_beautify_char", "do_nothing_char"]
    0 : ["+-*/%=!><&|^,", ",", None], #Support Python
    1 : ["+-*/%=!><&|?^,", ",", "#"], #Support C, C++, C#, Java, JavaScript
    2 : []
    }

try:
    beautify_char = programming_language_dic.get(int(input("Input your programming language number:\n0 : Support Python\n1 : Support C, C++, C#, Java, JavaScript\n2 : Input string by yourself\n")), -1)
except:
    print("Program terminated with wrong input.")
    sys.exit(0)

if beautify_char == []:
    print("Input three string follow a sequence:\nall_beautify_char\nright_beautify_char\ndo_nothing_char")
    for i in range(3):
        beautify_char.append(input())
if beautify_char == -1:
    sys.exit(0)

beautify_list = []
textfile_path = input("Input your Text file path:\n")
print("-----Begin -----") 
f = open(textfile_path, 'r+', encoding = 'utf8')

for line in f:
    if beautify_char[2] != None and beautify_char[2] in line:
        print(line, end = "")
        beautify_list.append(line)
        continue
    for position in range(len(beautify_char[0])):
        next_position = line.rfind(beautify_char[0][position])
        for times in range(line.count(beautify_char[0][position])):
            if beautify_char[0][position] == "=" and line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] != ' ' and line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] != '=':  
                line = line[:line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] + ' ' + line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1:] 
            elif line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] != ' ' and line[line.rfind(beautify_char[0][position], 0, next_position+1) + 1] not in beautify_char[0] and line[line.rfind(beautify_char[0][position], 0, next_position + 1)] not in beautify_char[1]:
                line = line[:line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] + ' ' + line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1:]
            if line[line.rfind(beautify_char[0][position], 0, next_position + 1) - 1] != ' ' and line[line.rfind(beautify_char[0][position], 0, next_position + 1) - 1] not in beautify_char[0] and line[line.rfind(beautify_char[0][position], 0, next_position + 1)]:
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
