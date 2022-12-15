message = "Hello, world!"

print(len(message))

f = open("message.txt", "w")
f.write(message)
f.close()
