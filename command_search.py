#command_search.py: Matches Makefile command formats.

#Imports necessary modules.
import re
import os
import sys

#Goes through the input line-by-line and determines
#if there are specific commands that match specified
#regular expressions, i.e. comment_regex, label_regex, etc.
def process_input_file(f_name):

    #Opens the input file.
    in_file = open(f_name, "r")

    #Iterates through the file line-by-line.
    for line in in_file:
        
        #Removes unecessary characters such as newlines.
        line = line.strip()

        #Prints the line.
        print line

        #Captures input with regular expressions and, if necessary,
        #removes the actual command to retrieve the desired input.
        comment_regex = re.findall("#.*", line)
        comment_regex = [c.replace("# ", "") for c in comment_regex]
        label_regex = re.findall(".*:", line)
        echo_regex = re.findall("echo.*", line)
        echo_regex = [e.replace("echo ", "") for e in echo_regex]
        #More regular expressions for other commands can be specified here.

        #Determines if comment_regex is not an empty list.
        if comment_regex != []:

            #If so, print the results.
            print ""
            print "Comment list:"
            print comment_regex
            print ""

        #Determines if label_regex is not an empty list.
        elif label_regex != []:

            #If so, print the results.
            print ""
            print "Label list:"
            print label_regex
            print ""

        #Determines if echo_regex is not an empty list.
        elif echo_regex != []:

            #If so, print the results.
            print ""
            print "Echo list:"
            print echo_regex
            print ""

        #Tests for other commands, like above, can be specified here.
    
    #Closes the input file.
    in_file.close()

#Retrieves a path to an input file from the command line.
file_name = sys.argv[1]

#Determines if the input file exists in the given path.
if os.path.exists(file_name):

    #Prints a status message showing what file is processing.
    print "Processing " + os.path.basename(file_name) + " located at " + file_name + "..."

    #Calls process_input_file.
    process_input_file(file_name)

#If the file does not exist in the given path, print an error.
else:
    print "The input file does not exist. Please try again."