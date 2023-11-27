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
new_sen = ''
c = 0

def normstring (string_def):
    flag = False
    # normalizing string from letter case point of view
    for i in range(len(string_def)):
        if flag and string_def[i].isalpha():
            string_def = string_def[:i] + string_def[i].swapcase() + string_def[i + 1:]
            flag = False
        if string_def[i] in ['.', '\n', '\t']:
            flag = True
    return string_def

#create new sentence
def newstring (split_string):
    global new_sen
    for i in range(len(split_string)):
        if split_string[i][len(split_string[i])-1] == '.':
            new_sen += split_string[i].replace('.',' ')
    new_sen = new_sen.capitalize()
    new_sen = f"{new_sen[0: -1]}." #replace last element to .
    return new_sen

def addstring (string_def, new_sen):
    #add new sentence to the end of the paragrah
    index = string_def.find('paragraph.')+len('paragraph.')
    string_def = string_def[:index] + ' ' + new_sen + string_def[index:]
    return string_def

#replace iz to is
def replstring (string_def):
    string_def = string_def.replace(' iz ', ' is ')
    return string_def

def countspace (string_def) ->int:
#count of whitespace
    global c
    for i in string_def:
        if(i.isspace()):
            c += 1
    return c

string_def = normstring(string_def)
new_sen = newstring(split_string)
print('New sen = ', new_sen)
string_def = addstring(string_def, new_sen)
string_def = replstring(string_def)
print(string_def)
c = countspace(string_def)
print("Number of Spaces :", c)