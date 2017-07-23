import sys
import os
import subprocess

def createCodeFile(filename, extension, code):
    # # At first Checking if the code file already exists or not
    # # 'W+' should overwrite (?)
    # # Get the code as an argument from PHP
    # # Save The Code as the Extension Suggests
    print("Stage 1")
    if extension == 'c':
        codeFile = open(filename+'.c', 'w+')
        codeFile.write(code);
        codeFile.close();
    elif extension == 'c++':
        codeFile = open(filename+'.cpp', 'w+')
        codeFile.write(code);
        codeFile.close();
    elif extension == 'java':
        codeFile = open(filename+'.java', 'w+')
        codeFile.write(code);
        codeFile.close();
    else:
        print("File Not Found")
        return

    # # If no code file Found then Simply return

    # # done with file preparation

    # #Lets COMPILE :D
    compileCodeFile(filename, extension)


def compileCodeFile(filename, extension):
    print("Stage 2")
    # # At first Lets check if there is already an EXE file
    # # If exists then it must be removed

    if os.path.isfile(filename+'.exe'):
        os.remove(filename+'.exe')
    if os.path.isfile(filename+'.class'):
        os.remove(filename+'.class')

    # # Removing Done.

    if os.path.isfile(filename+'.'+extension):
        # # Compiling C file from Command Line
        # # 'TDM\\bin\\gcc -o filename filename.c
        # # This will generate filename.exe

        if extension == 'c':
           compilingFile = filename+".c"
           os.system('TDM\\bin\\gcc -o ' + filename + " " + compilingFile)

        # # Compiling C++ file from Command Line
        # # 'TDM\\bin\\g++ -o filename filename.cpp
        # # This will generate filename.exe

        elif extension == 'cpp':
           compilingFile = filename+".cpp"
           os.system('TDM\\bin\\g++ -o ' + filename + " " + compilingFile)

        # # Compiling JAVA file from Command Line
        # # 'JAVA\\bin\\javac filename.java
        # # This will generate filename.class

        elif extension == 'java':
            compilingFile = filename + '.java'
            os.system('JAVA\\bin\\javac ' + compilingFile)

    # # Lets return if No file found
    # # no Reason to go forward.
    else:
        print("File not Created Properly")
        return
    # # filename.c / filename.cpp / filename.java
    # # All of them finished Compiling
    # # No need to keep them. So, removing them

    #if os.path.isfile(filename+'.'+extension):
        #os.remove(filename+'.'+extension)

    runTheCode(filename, extension)
    # #Done with compiling

def runTheCode(filename, extension):
    print("Stage 3")
    # # We will execute command based on extension
    # # C and C++ will generate exe files

    if extension == 'c' or extension == 'cpp':
        command = filename+'.exe'

    # # Java will generate a .Class file
    # # for Java .Class must be ignored

    elif extension == 'java':
        command = 'JAVA\\bin\\java ' + filename

    # # We can't just run a null or whitespace command , right?

    if command and not command.isspace():
        output = ""
        #run = os.system(command + ' < '+filename+'.txt > out.txt')
        run = os.system(command + ' > out.txt')

        # # Run has finished, So we don't need those EXE or Class Files
        if os.path.isfile(filename+'.exe'):
            os.remove(filename+'.exe')
        elif os.path.isfile(filename+'.class'):
            os.remove(filename+'.class')

        # # Here value 0 Means program executed successfully
        # # So No Compilation Error
        #if run == 0:
            #print ('Success')
        # # If not successful run then there is a Run Time Error
        # # Removing the out.txt
        #else:
            #if os.path.isfile('out.txt'):
                #os.remove('out.txt')
                #os.remove(filename+'.txt')
            #print('Run Time Error')


#if len(sys.argv) < 4:
    #print("Invalid Arguments")
    #exit(1)

# # First Argument From PHP Should be File Name
#codeName = sys.argv[1]
# # Second Argument MUST BE extension (C , CPP, JAVA)
#codeExtension = sys.argv[2]
# # Third extension MUST BE the code itself.
#codeText = sys.argv[3]
# # Fourth Argument MUST BE input file IFF User gives any input

#if len(sys.argv) == 5:
    # # user will give input like '1 2 3 4 5'
    # # So this input needs to be split by Space
    #codeInput = sys.argv[4]
    # # Before calling any functions these values must be checked
    # # whether they are null or not
    #codeInput = codeInput.split();

    # # If code file found then create an input file

    #inputFile = open(codeName+'.txt', 'w+')
    #inputFile.write(codeInput);
    #inputFile.close();


#createCodeFile(filename=codeName, extension=codeExtension, code=codeText)


compileCodeFile(sys.argv[1], sys.argv[2])
