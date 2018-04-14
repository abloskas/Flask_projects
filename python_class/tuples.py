my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def makeTuple(dict):
    lst = []
    for key, value in dict.items():
        lst.append((key, value))
    return lst
print(makeTuple(my_dict))   

