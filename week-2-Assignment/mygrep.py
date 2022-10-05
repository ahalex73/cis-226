# Alexander Holmes
# 9/9/22
# CRN: 10235
# CIS 226: Advanced Python Programming
# TOTAL TIME TO COMPLETE: --- 5 hours ---

'''
This program allows the user to use the mygrep utility tool. This tool
allows us to take in two parameters - the file name, and the string that you
are searching for. The program also prints out only the lines that match in
a given text file.

How to use
----------------
After downloading program and having python installed, run the command
mygrep.py "String you want to search for" "File you want to search in"
'''
import sys

def text_in_file(search_text, filename):
    ''' Searches for a given text inside of given filename'''
    # Try to open file, if not found, return error message.
    try:
        target_file = open(filename, "r")
    except OSError:
        print("File could not be opened/read:", filename)
        sys.exit()

    for line in target_file:    # for each line in the file
        if search_text in line: # search for our search text
            print(line.strip("\n"))
        
    target_file.close()


def main():
    # DONE: Check len(sys.argv) and warn if missing arguments
    
    # The reason why the check below is to 3, is because sys.argv[0] would
    # be the script name, the sys.argv[1] and sys.argv[2] 
    # arguments are our search_text and filename respectively
    

    if len(sys.argv) < 3 or len(sys.argv) > 3:
        sys.stdout.write("Please input only the search inquiry and filename \n")
        return

    search_text = sys.argv[1]
    filename = sys.argv[2]

    text_in_file(search_text,filename)
    

if __name__ == '__main__':
    main()
