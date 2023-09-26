#Write a function in Python to parse a string such that it accepts a parameter- an encoded string. 
# This encoded string will contain a first name, last name, and an id. 
# You can separate the values in the string by any number of zeros. 
# The id will not contain any zeros. The function should return a Python dictionary with the first name, last name, and id values. 
# For example, if the input would be "John000Doe000123". Then the function should return: { "first_name": "John", "last_name": "Doe", "id": "123" }

def parse_encoded_string(encoded_string):
    # Initialize variables to store the parsed values
    first_name = ""
    last_name = ""
    id = ""

    # Split the encoded string by consecutive zeros
    parts = encoded_string.split('0')

    # Iterate through the parts to extract values
    for part in parts:
        if part:
            # If part is not empty, check if it contains only digits (ID)
            if part.isdigit():
                id = part
            # If it's not all digits, it's either the first or last name
            elif not first_name:
                first_name = part
            else:
                last_name = part

    # Create and return the dictionary
    result = {
        "first_name": first_name,
        "last_name": last_name,
        "id": id
    }

    return result

# Test the function with your example
encoded_string = "John000Doe000123"
parsed_data = parse_encoded_string(encoded_string)
print(parsed_data)
