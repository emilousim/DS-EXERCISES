"""Restaurant rating lister."""
# put your code here
file = open("scores.txt")
d = {}
for line in file:
    x = line.rstrip("\n").split(":")
    a = x[0]
    b = x[1]
    d[a] = b
# print(d)
sortedList = (sorted(d.items()))

print(sortedList)

newRest = ""
newRest = str(input("Enter another restaurant!: "))

newRestRating = ""
newRestRating = int(input("Rate it, 1-5: "))
d.update({newRest: newRestRating})

print(sorted(d.items()))


# the first step we take is importing the file into this file by using the code in line 3. we use the open function to
# open and read the content. second step = (d={}), this creates an empty dictionary to put our key/value pairs in.
# .rstrip takes the \n off and .split slices everything into their key and value pair. once that's done, we just use the
# sorted function which sorts by key, alphabetically.
