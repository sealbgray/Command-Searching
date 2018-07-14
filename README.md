# Command-Searching

## command_search.py

### Overview
This Python program, `command_search.py`, utilizes lists and regular expressions to recognize various commands as well as arguments to these commands. Currently, this analysis is for `Makefile` commands and operations, which is able to be expanded to shell commands and operations.

### Functionality
First, the program prompts the user for the path leading to a `Makefile` or any file format, i.e. `.../directory1/directory2/.../Makefile`. Then, the program proceeds to process the input file line-by-line, while creating lists to store each line of the input file. When a list for a line of the input file is created, it is added to another list to create a list of lists containing each line from the input file.

Now, this list of lists is then analyzed one list at a time for each line of the input file. One approach utilized to analyze these lists involves observing the first element (i.e. the element at index 0) and determining whether that element is a specific command. If the first element is a specific command (i.e. `make` or `rm`), regular expressions are utilized to match arguments in these commands. Some of these arguments include file paths and comment text. Another approach utilized to analyze these lists involves capturing specific elements of the list using regular expressions. This approach was used to capture labels in a `Makefile`.

Both of the aforementioned approaches are able to be extended to determine various other commands and operations to capture their arguments with regular expressions, i.e. IP addresses, flags, and various other arguments.

### Future Steps
The output for this program is to create an output file containing the identified command or operation from the input file following the types of each argument encapsulated in < and >.

For example, the output file would exhibit the following format:
```
# <text>
include <package name>
<label>:
rm <flag> <file path>
```

Additionally, the code is able to be extended to identify and capture various commands and operations with their arguments. This can be achieved by adding additional `if` or `elif` statements where indicated in the `analyze_content_list()` function.

### Testing
A benign `Makefile` to analyze with the `command_search.py` program is the Unicorn Engine `Makefile` located at https://github.com/unicorn-engine/unicorn/blob/master/Makefile. Other `Makefiles` from various other projects may be collected and analyzed simultaneously in conjunction with the Unicorn Engine `Makefile`. The `command_search.py` program would be modified to handle such a change.
