str=('Life is not good')

x=1
while (x<2):
    print("This is our string: "+str)
    rm_character = input("What do you want to remove: ")
    if rm_character in str:
        str=str.replace(wanted_character,'')
        print(str)
    else:
        print("Not Found")
