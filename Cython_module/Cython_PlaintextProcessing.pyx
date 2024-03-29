# cython: language_level=3

from re import split as re_split

def plaintext_processing(list beautify_char, list c_type_keyword, file, str file_path, str file_name):
     
    cdef list file_list = file.readlines()
    cdef list beautify_list = []
    cdef int times
    cdef int position
    cdef int next_position
    cdef int pointer_position
    cdef str line

    for line in file_list:
        for position in range(len(beautify_char[0])):
            next_position = line.rfind(beautify_char[0][position])
            for times in range(line.count(beautify_char[0][position])):

                # It will search for pointer variables and store them(for C, C++, C#)
                if beautify_char[0][position] == "*" and beautify_char[2] == True and any(keyword in line.split()[0] for keyword in c_type_keyword):
                    for position in range(len(list(filter(None, re_split(" |, |,|;", line)))) - 1):
                        if "*" in (list(filter(None, re_split(" |, |,|;", line))))[position + 1]:
                            beautify_char[3].append((list(filter(None, re_split(" |, |,|;", line))))[position + 1])
                    break
                
                # It will beautify your pointer variables(for C, C++, C#)
                elif beautify_char[0][position] == "*" and beautify_char[2] == True and any(pointer in line for pointer in beautify_char[3]):
                    for pointer_position in range(len(beautify_char[3])):
                        if beautify_char[3][pointer_position] in line and line.index(beautify_char[3][pointer_position]) <= line.rfind(beautify_char[0][position], 0, next_position + 1) and line.index(beautify_char[3][pointer_position]) + len(beautify_char[3][pointer_position]) - 1 >= line.rfind(beautify_char[0][position], 0, next_position + 1):
                            continue

                # It will beautify sign's right side(example: a=1+2-3*4/5 -> a= 1+ 2- 3* 4/ 5)
                elif line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] not in " '\"=" and line[line.rfind(beautify_char[0][position], 0, next_position+1) + 1] != beautify_char[0][position]:
                    line = line[:line.rfind(beautify_char[0][position], 0, next_position + 1) + 1] + ' ' + line[line.rfind(beautify_char[0][position], 0, next_position + 1) + 1:]

                # It will beautify sign's left side(example: a=1+2-3*4/5 -> a =1 +2 -3 *4 /5)
                if line[line.rfind(beautify_char[0][position], 0, next_position + 1) - 1] not in " '\"=" and line[line.rfind(beautify_char[0][position], 0, next_position + 1) - 1] not in beautify_char[0] and line[line.rfind(beautify_char[0][position], 0, next_position + 1)] not in beautify_char[1]:
                    line = line[:line.rfind(beautify_char[0][position], 0, next_position + 1)] + ' ' + line[line.rfind(beautify_char[0][position], 0, next_position + 1):]
                    
                next_position = line.rfind(beautify_char[0][position], 0, next_position)
                
        beautify_list.append(line)

    cdef str file_copy_path = file_path[:-len(file_name)] + file_name.split(".")[0] + "_copy." + file_name.split(".")[-1]
    file_copy = open(file_copy_path, 'w+', encoding = 'utf8')
    file_copy.writelines(beautify_list)
    file_copy.seek(0)
    print(file_copy.read())
    
    return beautify_list, file_copy, file_copy_path