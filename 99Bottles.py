bottles = 99
while bottles > 1:
    print(bottles,"Bottles of beer on the wall,", bottles, "bottles of beer")
    print("take one down, pass it around", bottles, "of beer on the wall")
    bottles = bottles-1
    if bottles == 1:
        print(bottles, "bottle of beer on the wall, only one bottle of beer,")
        print("take one down, pass it around, only", bottles, "of beer on the wall")
   