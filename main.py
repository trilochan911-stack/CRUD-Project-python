
# This is for CRUD Project
# I will apply createfile,readfile,updatefile,deletefile


from pathlib import Path

import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")


def Createnewfile() :
    try:
        readfileandfolder()
        name = input("Enter file name : ")
        p = Path(name)
        if not p.exists():
            with open(p,'w') as fs :
                data = input("Write what you want to write : ")
                fs.write(data)
        else:
            print(f"This file is already exist")

        print("A new file is Created Successfully")
    
    except Exception as err:
        print(f"Error occured as {err}")
    

def Readfile():
    try:
        readfileandfolder()
        name = input("Enter file name : ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs :
                content = fs.read()
                print(content)
                print("File readed successfully")
        else:
            print(f"SORRY! This file doesnot exist")

    except Exception as err:
        print(f"Error occured as {err}")


def Updatefile():
    try:
        readfileandfolder()
        name = input("Enter file name : ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("1) Press 1 if you want to update file name ")
            print("2) Press 2 if you want to Add new content ")
            print("3) Press 3 if you want to Overrite the existing content ")
            ch = int(input(f"Enter your choice : "))
            if ch == 1 :
                name2 = input("Suggest your new file name")
                p2 = Path(name2)
                p.rename(p2)
            elif ch == 2 :
                with open(p,'a') as fs :
                    data = input("Write what you want to write : ")
                    fs.write(data)
            else:
                with open(p,'w') as fs :
                    data = input("Write what you want to append : ")
                    fs.write(" "+data)


            print("File updated successfully")
        else :
            print(f"SORRY! This file doesnot exist")
    except Exception as err :
        print(f"Error occured as {err}")


def Deletefile():
    try:
        readfileandfolder()
        name = input("Enter file name which you want to Delete : ")
        p = Path(name)
        if p.exists() and p.is_file() :
            os.remove(p)
            print("File deleted successfully")
        else : 
            print(f"SORRY! This file doesnot exist")
    except Exception as err :
        print(f"Error occured as {err}")

exit = True
while exit :
    print("1) Press 1 if you want to Create new file ")
    print("2) Press 2 if you want to Read file ")
    print("3) Press 3 if you want to Update file ")
    print("4) Press 4 if you want to Delete file ")
    print("5) Press 5 if you want to exit")

    choice = int(input("Enter your choice :"))

    if(choice == 1):
        Createnewfile()

    if(choice == 2):
        Readfile()

    if(choice == 3):
        Updatefile()

    if(choice == 4):
        Deletefile()

    if(choice == 5):
        print("Exiting.....")
        exit = False
