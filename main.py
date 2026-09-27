# import re
try:
    with open("file.txt" ,"r") as file:
        content = file.read()
    split_content = content.split()
    # split_content = re.split(r'\s+', content)


    print(len(split_content))

except FileNotFoundError:
    print("Error: Create file.txt file")
    exit()
