str="welcome to python class"
words=str.split(" ")
print(words)
words=words[-1::-1]
print(words)
outputstr=''.join(words)
print(outputstr)