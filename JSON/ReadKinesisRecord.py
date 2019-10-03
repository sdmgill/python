import ast
import json

d1 = json.load(open("KinesisRecord.json"))
print(d1)

# d2 = json.load(open("KinesisRecord.json"))
# for line in d2:
#     for k,v in line.items():
#         print(k,v)

# d3 = json.load(open("KinesisRecord.json"))
# for line in d3:
#     for kv in line.items():
#         print(kv[0])