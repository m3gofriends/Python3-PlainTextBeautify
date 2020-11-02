import sys

programming_language_dic = {
    0 : "+-*/%=!><&|", #Support Python
    1 : "+-*/%=!><&|?^", #Support C, C++, C#, Java, JavaScript
    2 : None
    }

try:
    beautify_char = programming_language_dic.get(int(input("Input your programming language number:\n0 : Support Python\n1 : Support C, C++, C#, Java, JavaScript\n2 : Input string by yourself\n")), -1)
except:
    print("Program terminated with wrong input.")
    sys.exit(0)

if beautify_char == None:
    beautify_char = input()
if beautify_char == -1:
    sys.exit(0)

beautify_list = []
textfile_path = input("Input your Text file path:\n")
print("-----Begin -----") 
f = open(textfile_path, 'r+', encoding = 'utf8')

for line in f:
    for position in range(len(beautify_char)):
        next_position = 0
        for times in range(line.count(beautify_char[position])):
            if line[line.find(beautify_char[position],next_position + 1) + 1] != ' ' and line[line.find(beautify_char[position],next_position + 1) + 1] not in beautify_char:
                line = line[:line.find(beautify_char[position],next_position + 1) + 1] + ' ' + line[line.find(beautify_char[position],next_position + 1) + 1:]
            if line[line.find(beautify_char[position],next_position + 1) - 1] != ' ' and line[line.find(beautify_char[position],next_position + 1) - 1] not in beautify_char:
                line = line[:line.find(beautify_char[position],next_position + 1)] + ' ' + line[line.find(beautify_char[position],next_position + 1):]
            if line[line.find(beautify_char[position],next_position + 1) - 1] in beautify_char:
                next_position = line.find(beautify_char[position],next_position + 1) + 1
            else:
                next_position = line.find(beautify_char[position],next_position + 1)
    print(line, end = "")
    beautify_list.append(line)

print("\n-----End -----") 
ans = input("\n-----Change? Y/N-----\n") 
if ans.upper() == "Y" or ans.upper() == "YES":
    f.seek(0)
    f.writelines(beautify_list)
f.close()

