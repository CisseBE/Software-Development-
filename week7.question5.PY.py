input1=input("Enter first sentence")
input2=input("Enter second sentence")
concatenation = " ".join([input1, input2])
list = concatenation.split()
sort = sorted(list, key = str.lower)
print(list)
print(sort)
print(len(list))
dict = {}
for word in range(len(list)):
    dict[list[word]] = list.count(list[word])
print(dict)
for word in dict:
    print (word)
