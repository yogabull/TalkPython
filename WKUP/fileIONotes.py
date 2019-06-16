
'''
Research on Journal App

File I/O (input/output)

print() Function:
    displays text in the CLI.

.write() methond:
    you can use .write() to write data to a file.

sys.stdout:
    Standard output file can be named: 'sys.stdout'


File I/O
ie (copied from repl.it website):
    file = open('output.txt', 'w')
    file=open('output.txt', "w")
    file.write("hello, World!")
    file.close()
    file2=open('input.txt',"r")
    contents=file2.readline()
    print(contents)
    contents=file2.readline()
    print(contents)
    file2.close()


        "w" means makes the file writeable and it is called a "mode"

        when it reads the content it goes to end of file  in  file2.read

        note diff between read and readline

        note that the output has a space inbetween which is because print inserts an enter at the end
