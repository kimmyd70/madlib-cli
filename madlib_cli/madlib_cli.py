import re


# Print welcome with instructions
def welcome():
    print("""\n ***  Let\'s Play MadLibs!  ***\n
    I\'ll ask you for words in a specific category of speech.  I'll use your 
    choices to fill in a template and print your story to the screen\n""")
    

# Create and test a read_template function that takes in a path to text file
# and returns a stripped string of the file’s contents. Should raise a 
# FileNotFoundError if path is invalid.
def read_template(my_path):
    try:
        lib_template = open(my_path, 'r') 
        contents = lib_template.read()
        return contents
    
    except FileNotFoundError:
        print("The file path is not correct")

# Create and test a parse_template function that takes in a template string 
# and returns a string with language parts removed and a separate list of those 
# language parts.(I chose RegEx approach; tested w/regex101.com)
def parse_template(template):
    find_word = re.findall('({\w*})',template)
        
    # print(find_word)
    return find_word

# Prompt user for inputs
def get_input(list):
    user_words =[]
    for word in range (0,len(list)):
        print(f'Please enter a word in the category {list[word]}')
        user_words.append(input('> ').lower())   
        word =+ 1
    return (user_words)

# Create and test a merge function that takes in a “bare” template and a list 
# of user entered language parts, and returns a string with the language parts 
# inserted into the template.
def merge(template,list):
    for position in range (0,len(list)):
        merged_lib = re.sub('({\w*})',list[position],template)
        position += 1
    # print(list)
    # print(merged_lib)
    # print(template)
    return merged_lib



# Print the completed MadLib to the command line and 
# Write the completed MadLib to a new file
def write_madlib(new_path,info):
    with open (new_path,'w') as complete_lib:
        print(f'\n Here is your story\n {info}')
        complete_lib.write(info)


# chained functions ugly programming but produces output
welcome()

write_madlib('complete_lib_file.txt', 
        merge(read_template('template.txt'),
    (get_input(parse_template(read_template('template.txt'))))))
