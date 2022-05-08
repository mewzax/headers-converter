headers = open("headers.txt", "r+").read().splitlines()
file = open("file.txt", "r+")

for header in headers:
    header2 = "\"" + header.split(":")[0] + "\"" + ": " + "\"" + header.split(":")[1].strip() + "\""
    file.write(header2 + "\n")
