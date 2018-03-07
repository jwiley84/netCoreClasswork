chair = {
    "name": "Jessica",
    "nickname": "JJ",
    "ghosts_Belief": True,
    "age": 33,
    "veteran": True,
    "hometown": "Tacoma",
    "fave_language": "Python",
}

def unzip(dictMe):
    keyArray = []
    valueArray = []
    fullArray = []
    for (key, value) in dictMe.items():
        keyArray.append(key);
        valueArray.append(value);
    #print(keyArray)
    #print(valueArray)
    fullArray.append(keyArray)
    fullArray.append(valueArray)
    return fullArray;

print(unzip(chair))
