'''write a python program that inputs a text file and outputs a new file where all the words are converted to lowercase.

input: a text file named "Sample_text.txt" with the following content:
outputs: a new text file named "Lowercase_text.txt" with the following content'''

# Open the file in read mode
file = open("Sample_text.txt", "r")
# Open the new file in write mode
new_file = open("Lowercase_text.txt", "w")
# Loop through the file
for line in file:
    # Convert the line to lowercase
    new_line = line.lower()
    # Write the new line to the new file
    new_file.write(new_line)
# Close the files
file.close()
new_file.close()
# Print the results

print("The file has been converted to lowercase.")

