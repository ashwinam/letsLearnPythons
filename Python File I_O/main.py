# ----------Working with file In python----------
# In programming everything is about give the data and receive the processed data, Its called Input and Output(I/O)

# in python we can work with files

# myFile = open('text.txt')
# print(myFile.read())
# # In here Why it didn't print Three Times ?
# # Theres a concept called cursor = just read the once and print one by one, it works like how human reads, Put finger on characters and go line by line but if you want restart your reading you need to put your finger where it starts, just it happens here
# myFile.seek(0)
# # its the think that put finger on start, here we reset the cursor
# print(myFile.read())
# myFile.seek(0)
# print(myFile.read())

# print(myFile.readline())  # read line by line
# print(myFile.readlines())  # it return the list with items is readline()
# # print(myFile.readline())
# myFile.close()  # it a general way to close the file

# ------------Read, Write, append---------------

# Another way to operate files in python

# with open('text.txt', mode='r') as myFile:  # dont need close the file
#     print(myFile.read())

# print(myFile.read()) # outside indentation its closed the file

# types of modes
# 1. r = read mode (default one) able to read files
# 2. w = write mode able to write files and if file does not exist it creates one
# 3. r+ = read/write mode, perform both operations, not able to create new files and it overwrite the characters where the cursor is
# 4. a = append mode, its a write the end of the file

# with open('happy.txt', mode='w') as myFile:
#     myFile.write('123456') # write mode overwrite the data if exist


# with open('happy.txt', mode='r+') as myFile:
#     # read/write mode replace only that much character and it reset the cursor.
#     myFile.write(':)')
with open('happy.txt', mode='a') as myFile:
    myFile.write(':)')  # in append mode it write the end of the file
