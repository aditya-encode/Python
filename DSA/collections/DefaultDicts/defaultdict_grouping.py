from collections import defaultdict
d=defaultdict(list)
words=['apple','banana','carrot','cat']
for word in words:
    d[word[0]].append(word)

print(d)