

try:
    with open('data.txt', 'r') as data_file:
        data = data_file.readlines()
        for line in data:
            print(line)
        #file is closed here.

except FileNotFoundError as err:
    print("I'm sorry that file does not exist.")
    print(err)