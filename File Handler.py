import os
import shutil


def createfolder():
    print "Enter Folder name:"
    name=raw_input()
    folder = os.getcwd()+"/"+name
    if not os.path.exists(folder):
        os.makedirs(folder,0777)
    else:
        print "Folder already exsits"

def change_extension():
    print "Enter old Extension:"
    oldext=raw_input()
    print "Enter new Extension:"
    newext=raw_input()
    folder = os.getcwd()
    for filename in os.listdir(folder):
        infilename = os.path.join(folder,filename)
        if not os.path.isfile(infilename): continue
        oldbase = os.path.splitext(filename)
        newname = infilename.replace(oldext, newext)
        output = os.rename(infilename, newname)
    print "Modifying Extension Complete"

def create_copy():
    print "Enter file Name with Extension"
    filenm=raw_input()
    if os.path.isfile(filenm):
        shutil.copy2(filenm, '(copy)'+filenm)
        print "Copy Created"
    else:
        print "No such file"

def delfile():
    print "Enter file Name with Extension"
    filenm=raw_input()
    if os.path.isfile(filenm):
        os.remove(filenm)
        print "File Removed!"
    else:
        print "No such File"

def delfolder():
    print "Enter folder"
    filename=raw_input()
    if os.path.exists(filename):
        shutil.rmtree(filename, ignore_errors=True)
    else:
        print "No Such Folder"

def mvfile():
    print "Enter filename:"
    filename=raw_input()
    if os.path.exists(filename):
        print "Enter subfolder:"
        folder=raw_input()
        if os.path.exists(folder):
            os.rename(filename,folder+'/'+filename)
            print "File moved"
        else:
            print "Folder doesnt exist. Would you like to create folder (yes/no)"
            f=raw_input()
            if f == 'yes':
                os.makedirs(folder,0777)
                os.rename(filename,folder+'/'+filename)
                print "File moved"
            elif f == 'no':
                print "Folder not created"
            else:
                print "invalid input"
    else:
        print "No such file"

def mvext():
    print "Enter Extension:"
    ext=raw_input()
    print "Enter subfolder:"
    folder=raw_input()
    flag=0
    if not os.path.exists(folder):
        print "Folder doesnt exist. Would you like to create folder (yes/no)"
        f=raw_input()
        if f == 'yes':
            os.makedirs(folder,0777)
        elif f == 'no':
            print "Folder not created"
        else:
            print "invalid input"
    if  os.path.exists(folder):
        for filename in os.listdir(os.getcwd()):
            if ext in filename:
                os.rename(filename,folder+'/'+filename)
                flag=1
    if flag == 0:
        print "No files moved"
    else:
        print "Moving of files complete"

print "\n         EASY FILE HANDLER           "
print "         By Aditya Sanghi            "
print " ------------------------------------"
while True:
    print "\n1.Change Extension"
    print "2.Create a folder"
    print "3.Create copy of a file"
    print "4.Delete file"
    print "5.Delete folder"
    print "6.Move specific file to subfolder"
    print "7.Move according to extension"
    print "0.Exit"
    cmd = raw_input()
    if cmd == '1':
        change_extension()
    elif cmd == '2':
        createfolder()
    elif cmd == '3':
        create_copy()
    elif cmd == '4':
        delfile()
    elif cmd == '5':
        delfolder()
    elif cmd == '6':
        mvfile()
    elif cmd == '7':
        mvext()
    elif cmd == '0':
        break
    else:
        print "Invalid command."

