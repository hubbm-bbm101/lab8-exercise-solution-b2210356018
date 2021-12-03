import sys
with open(sys.argv[1]) as data:
    data_dict = {}
    dataList = [x.split(":") for x in data.read().splitlines()]
    for names in dataList:
        data_dict[names[0]] = str(names[1])
    for input in sys.argv[2].split(","):
        try:
            print(f"Name:{input},University:{data_dict[input]}")
        except:
            FileNotFoundError
            print(f"No record '{input}'was found.")



