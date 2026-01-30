import json
import os


# The data we want to save
data = [
    {"Name": "Alice", "age": 25, "birthyear": 1998},
    {"Name": "Bob", "age": 30, "birthyear": 1993}
]

# Create the file 'input.json' and write the data into it
with open('input.json', 'w') as f:
    f.write(json.dumps(data))

print("Success! input.json has been created.")


if __name__ == "__main__":
    try:
        with open('input.json', 'r')as f:
            data = json.loads(f.read())

        output = ','.join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'

        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')
