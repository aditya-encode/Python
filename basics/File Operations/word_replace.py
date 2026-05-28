#write a code that change the occurrence of java to Python in file named "practice.txt"

with open("practice.txt","r") as f:
    data=f.read()

new_data=data.replace("Java","Python")

with open("practice.txt","w") as f:
    g=f.write(new_data)
