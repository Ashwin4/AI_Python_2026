#to checck multiple condtions we can use if elif
dtype=input("Please enter a data type ")
if dtype=="list":
    print("List is muutable")
elif dtype=="tuple":
    print("Tuple is Immutbale")
elif dtype=="set":
    print("set is mutable")
elif dtype=="dict":
    print("dict is Mutable")
else:
    print("Please enter a valid data type")
