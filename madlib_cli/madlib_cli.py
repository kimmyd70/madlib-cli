

# Print welcome with instructions
def welcome():
    print("""\n ***  Let\'s Play MadLibs!  ***\n
    I\'ll ask you for words in a specific category of speech.  I'll use your 
    choices to fill in a template and print your story to the screen\n""")
    

# Create and test a read_template function that takes in a path to text file
# and returns a stripped string of the file’s contents. should raise a 
# FileNotFoundError if path is invalid.
# def read_template(my_path):
def read_template():
    # print(my_path)
    try:
        lib_template = open('dark_and_stormy_night.txt', 'r') 
        contents = lib_template.read()
        print(contents)
        return contents
    
    except FileNotFoundError:
        print("The file path is not correct")

# Create and test a parse_template function that takes in a template string 
# and returns a string with language parts removed and a separate list of those 
# language parts.

# Prompt user for inputs


# Create and test a merge function that takes in a “bare” template and a list 
# of user entered language parts, and returns a string with the language parts 
# inserted into the template.


# Print the completed MadLib to the command line

# Write the completed MadLib to a new file
def write_madlib(new_path):
    with open ('new_path','w') as complete_lib:
        complete_lib.write()


welcome()
read_template()
# write_madlib('completed_lib.txt')
