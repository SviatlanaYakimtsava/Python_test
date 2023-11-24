string_def = """  
homEwork:
    tHis iz your homeWork, copy these Text to variable.

    You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

    it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

    last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.

"""

string_def = string_def.lower()     # converting string to lover case
string_def = string_def.capitalize()  # converting string to make first word capitalized
split_string = string_def.split()     # variable to keep list of words of the provided text
flag = False
new_sen = ''

# normalizing string from letter case point of view
for i in range(len(string_def)):
    if flag and string_def[i].isalpha():
        string_def = string_def[:i] + string_def[i].swapcase() + string_def[i + 1:]
        flag = False
    if string_def[i] in ['.', '\n', '\t']:
        flag = True

#create new sentence
for i in range(len(split_string)):
    if split_string[i][len(split_string[i])-1] == '.':
        new_sen += split_string[i].replace('.',' ')
new_sen = new_sen.capitalize()
new_sen = f"{new_sen[0: -1]}." #replace last element to .
print('New sen = ', new_sen)

#add new sentence to the end of the paragrah
index = string_def.find('paragraph.')+len('paragraph.')
string_def = string_def[:index] + ' ' + new_sen + string_def[index:]

#replace iz to is
string_def = string_def.replace(' iz ', ' is ')
print(string_def)

#count of whitespace
c = 0
for i in string_def:
    if(i.isspace()):
        c += 1
print("Number of Spaces : "+str(c))

