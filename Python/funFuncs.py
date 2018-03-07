def oddEven():
    for value in range(1, 2000):
        if (value % 2 == 0):
            print(str(value) + " is an even number")
        else:
            print(str(value) + " is an odd number")

setArray = [1,2,3,4,5]

def multiply(arr, multiple):
    for item in range(0, len(arr)):
        arr[item] = arr[item] * multiple;
    
    return arr;

def layered_multiples():
    newArr = [];
    too_many_arrays = [];
    too_many_arrays = multiply(setArray, 2);
    for item in too_many_arrays:
        playArr = [];
        for bit in range(0, item):
            playArr.append(1)
        newArr.append(playArr);
    print(newArr);


