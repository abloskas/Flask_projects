name = ["Nick", "Alice", "Kitty", "Bob", "Sally"]
hobby = ["Reading", "Gardening", "Running", "Weightlifting", "Netflix"]

def makeDict(lst1, lst2):
    dictHobby = {}
    for i in range(len(lst1)):
        dictHobby[lst1[i]] = lst2[i]
    print(dictHobby)    

makeDict(name, hobby)    