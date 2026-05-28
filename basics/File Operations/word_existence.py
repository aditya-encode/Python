# check whether word "learning" exist in practice or not?
with open("practice.txt","r") as f:
    data=f.read()
    word="learning"
    if (data.find(word)!=-1):
        print("found")
    else:
        print("not found")