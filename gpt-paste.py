import os
import glob
import pyperclip

#This code concatenates the contents of all .py files in the current directory (excluding the current script file)
#The name of each file is added as a comment before the contents. 
#The resulting output is then copied to the clipboard using the pyperclip module.
#This allows you to paste your project into GPT-3 as a single file.

# Get all .py files in the current directory, except for this script
this_file = os.path.basename(__file__)
files = [file for file in glob.glob("*.py") if file != this_file]

# Concatenate all the files and add the filename as a comment
#exclude this file
output = ""
for file in files:
    with open(file, "r") as f:
        contents = f.read()
        output += f"# File: {file}\n{contents}\n"

# Copy the output to the clipboard
pyperclip.copy(output)
