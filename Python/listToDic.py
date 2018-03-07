names = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "tidepods", "chickens", "llamas"]


def make_dict(list1, list2):
  new_dict = {}
  new_dict = dict(zip(list1, list2))
  print(new_dict) 

  return new_dict


make_dict(names, favorite_animal)