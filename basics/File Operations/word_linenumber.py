#write a code that prints the line number on which the word "learning" exist and print(-1) if word does notexist in file
with open("practice.txt","r") as f:
    word="learning"
    line_number=1
    data=True
    found=False
    while data:
        data=f.readline()
        if word in data:
            print(line_number)
            found=True
        else:
            line_number+=1
    
if found==False:
    print(-1)