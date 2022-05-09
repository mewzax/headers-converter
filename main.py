headers = open('headers.txt', 'r').read().splitlines()
output = open('output.txt', "w")

output.write("headers = {\n")

for header in headers:
  header = "\t\""+header.split(":")[0]+"\""+": "+"\""+header.split(":")[1].strip()+"\",\n"
  output.write(header)
  
output.write('}')
output.close()