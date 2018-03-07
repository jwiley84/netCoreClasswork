# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

#function output
#[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
array = []
for key in my_dict:
    a = key, my_dict[key]
    array.append(a)
    #print(value)
    #print(extra)
print(array)