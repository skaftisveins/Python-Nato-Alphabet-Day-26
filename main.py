import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(key, value)

student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    print(index, row)
    #Access row.student or row.score
    print(row.student)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("nato_phonetic_alphabet.csv")
phoentic_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(phoentic_dict)
# print(result)


# new_dict = {new_key:new_value for (key, value) in list}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_word = input("Enter a word: ").upper()
new_dict = [phoentic_dict[letter] for letter in input_word]
print(new_dict)

