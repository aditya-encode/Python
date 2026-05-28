with open("practice1.txt","r") as f:
    data=f.read()
    new_data=data.split(",")
    count=0
    for i in new_data:
        if int(i)%2==0:
            count+=1
print(count)