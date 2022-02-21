import platform

def main():
    message()
	
def message():
    print('This is python version {}'.format(platform.python_version()))

if __name__ == '__main__': main()

#in this second version, by having a conditional statement that calls main, it then forces the interpreter to read the entire code before excecuting, 
#this allows for a more procedial style of programming. 
