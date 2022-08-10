def Char_Count(char,str):

    str=input("Type some words: ")
    x = 1
    while (x < 2):
        char=input("Which character you want to count: ")

        count=0
        for a in range(len(str)):
            if char in str[a]:
                count=count+1

        print(char+':',count)

word=''
Char=''
Char_Count(Char,word)
