import random
carta={}
lista=("B","I","N","G","O")
numberc=input("Introduce number of cards ")

for j in range(int(numberc)):
    print("Card N°",j+1)
    for i in lista:
        carta[i]=[]
    min = 1
    max = 15
    valuess=5

    for letter in carta:
        carta[letter] = random.sample(range(min, max), valuess)
        carta[letter].sort()
        min += 15
        max += 15
        if letter == "N":
            carta[letter][2] = "X" # free space!
        print(letter,carta[letter])

    print("-------------")
