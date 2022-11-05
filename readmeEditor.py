import os

def printNotes(): # function to write the names ad urls of each file to README.md file
    global text_
    global path
    text_ = ''
    list_ = os.listdir() # list of all folders
    for folder in list_:
        if str(folder)[0] == '0':
            files = os.listdir(folder) # list of all folders in that file
            text_ = text_+'\n **'+str(folder)+'**:  \n' # Folder name in md **bold**
            for file in files:
                folder_ = folder.replace(' ','%20')
                file_ = file.replace(' ','%20')
                path = f'{folder}/{file}'
                md = f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[{file}](https://github.com/abhisindh/study/blob/master/{folder_}/{file_})  \n' # url and link text 
                text_ = text_ + md 

if __name__ == '__main__':
    printNotes()
    f = open('README.md','w')
    f.write(text_)
    print("Finished writing, last entry : ",path)
    f.close()
    a = input("Press Enter to exit")
