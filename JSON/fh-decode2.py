import json

decoder = json.JSONDecoder()

with open('fh-pnct-n4-invmoveevent.json', 'r') as content_file:

    content = content_file.read()

    content_length = len(content)
    decode_index = 0

    while decode_index < content_length:
        try:

            obj, decode_index = decoder.raw_decode(content, decode_index)
            #print("File index:", decode_index)
            mydict = obj
            mylist = [obj]
            # myj = json.dump(data, mydict)
            # data = json.loads(mydict)
            # print(data)
            # mylist1 = mylist[0]["data"].values()
            # print(mylist[0]["data"].values())
            # print(mydict["data"].values())
            # print(mylist)
            deser = str(mylist.values())
            # print(type(row))
            deser2 = deser.replace("}, {", ", ")

            with open("test.json","a+") as f:
                for row in deser2:
                    print(row)
                    # f.write("%s\n" % row)
            # print(mydict)
        except Exception as e:
            # continue
            print("JSONDecodeError:", e)
            # Scan forward and keep trying to decode
            decode_index += 1