
list_names = ["andrzej", "antoni", "aleksander", "bartek", "cezary", "daniel"]
list_names = [name for name in list_names if not name.startswith("a")]

for elem in list_names:
    print(elem)