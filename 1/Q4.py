'''Merge the first name and last name as sigle token  in the given sentence
input: text = "Robert Langdon is a famous character in various books books and movies" 
Desired output: Robert Langdon  
        is  
        a  
        famous  
        character  
        in  
        various   
        books  
        and   
        movies
'''

def merge_name_and_tokenize(text, first_name, last_name):
    # Replace the first and last name with a single token
    full_name = first_name + " " + last_name
    text = text.replace(full_name, full_name.replace(" ", "_"))
    
    # Split the text into words
    words = text.split()
    
    # Replace underscores with spaces in the full name
    words = [word.replace("_", " ") for word in words]
    
    # Print each word on a new line
    for word in words:
        print(word)

# Example usage
text = "Robert Langdon is a famous character in various books and movies"
first_name = "Robert"
last_name = "Langdon"
merge_name_and_tokenize(text, first_name, last_name)


