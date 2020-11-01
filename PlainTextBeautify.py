beautify_char = "+-*/%=!><&|"
beautify_list = []

textfile_path = input("Input your Text file path:\n")
print(" -----Begin -----") 
f = open(textfile_path, 'r+', encoding = 'utf8')

for line in f:
    for position in range(len(beautify_char)):
        next_position = 0
        for times in range(line.count(beautify_char[position])):
            a = line.count(beautify_char[position])
            c = line.find(beautify_char[position],next_position + 1)
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

print("\n -----End -----") 
ans = input("\n-----Change? Y/N -----\n") 
if ans.upper() == "Y" or ans.upper() == "YES":
    f.seek(0)
    f.writelines(beautify_list)
    f.close()
if ans.upper() == "N" or ans.upper() == "NO":
    f.close()
