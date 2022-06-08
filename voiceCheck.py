from voiceR import *
from os import walk


filenames = next(walk("voices"), (None, None, []))[2]
print(filenames)

count = 0

for file in filenames:
    output = voice("voices\\" + file)
    print(str.lower(file))
    if (output == str.lower(file[0])):
        count += 1

print(count)