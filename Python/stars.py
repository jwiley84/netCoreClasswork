def draw_stars(arr):
    for item in arr:
        if (type(item) is int):
            print("*"*item);
        elif (type(item) is str):
            meep = item[0].lower()
            print(meep * len(item))

draw_stars([1,"Tom",5,"Michael",3,5,7,"bob",5,7])