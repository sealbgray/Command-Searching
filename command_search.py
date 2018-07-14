#command_search.py: Matches Makefile command formats.

#Imports the regular expressions module.
import re

#Creates a list of lists containing all the file's contents.
def create_file_list(f):

    #Initializes the variable.
    file_contents = []

    #Iterates through the input file.
    for line in f:

        #Splits each word in the line and creates a list.
        line_list = line.split()

        #Determines if a created list is not empty.
        if line_list != []:

            #If so, add the created list to the file_contents list.
            file_contents.append(line_list)

        #If the list is empty, ignore it.
        else:
            pass

    #Returns the final list of lists.
    return file_contents

#Sections each line from the file into a list.
def decipher_contents(f_contents):

    #Iterate through the list of lists,
    #looking at one list at a time.
    for lst in contents:

        #Prints the current list.
        print "List:"
        print lst
        print ""

        #Further analyzes the contents for
        #commands and arguments for those commands.
        analyze_content_list(lst)

#Analyzes the line to match commands and their respective arguments.
def analyze_content_list(l):

    #Iterates through each input list.
    for entry in l:

        #Determines if the first element of a list
        #is the make command.
        #Currently need to match flags (i.e. "-C") after "make".
        if l[0] == "make":
            
            #If so, print the file paths captured
            #by the regular expression.
            print "make regular expressions:"
            print re.findall("/.*", entry)
            print ""

        #If not, determine if the first element of a 
        #list is #; this is to capture comments.
        elif l[0] == "#":

            #If so, print the comment contents captured
            #by the regular expression in a list.
            print "comment regular expressions: "
            print re.findall(".", entry)
            print ["".join(re.findall(".", entry))]
            print ""

        #If not, determine if the list is a label, 
        #captured by the regular expression.
        elif l == re.findall(".*:", entry):

            #If so, print the contents of the label
            #captured by the regular expression.
            print "label regular expressions:"
            print re.findall(".*:", entry)
            print ""

        #More elif statements can be added here to
        #analyze other commands/operations such as
        #rm, +=, $(), etc.

#Prompts the user for the file path and the file name.
file_name = raw_input("Please enter a path for the input file: ")

#Opens the specified file.
input_file = open(file_name, "r")

#Stores each line of the input file in a list of lists.
contents = create_file_list(input_file)

#Closes the input file.
input_file.close()

#Analyzes the list of lists to print command formats.
decipher_contents(contents)