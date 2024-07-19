
file = open("./bear.txt", "w")
file.write("Hey, I am Bear.")
file.close()

file = open("./bear.txt", "r")


cont = file.read()
print(cont)