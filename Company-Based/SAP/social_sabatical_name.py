# maximum number of letters(ignoring spaces and duplicates) if tie choose alphabetical order. 
# import sys
# text = "".join(sys.stdin.readlines())
# name_list = text.split("\n")
inputList = ["kylan charles", "raymond strickland", "julissa shepard", "andrea meza", "destiny alvarado"]
inputList2 = ["maria garcia", "smith hernandez", "hernandez smith", "mary martinez", "james johnson"]
inputList3 = ["Sheldon Cooper", "Howord Wolowitz", "Amy Farrah Fowler", "Leonard Hofstadter", "Bernadette R"]
name_store = {}
for name in inputList3:
    name_store[name] = len(set(name.lower().replace(" ", "")))   # Remove spaces using replace and remove duplicates using set
res = []
maxLen = -float("inf")
for name in name_store.keys():
    if name_store.get(name) > maxLen:
        res.clear()
        res.append(name)
        maxLen = name_store.get(name)
    elif name_store.get(name) == maxLen:
        res.append(name)
res.sort()
print(res[0])