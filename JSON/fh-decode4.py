import json

decoder = json.JSONDecoder()

with open("test2.json", "w+") as w:
    w.write("[")

with open("fh-pnct-n4-invmoveevent.json", "r") as content_file:
    content = content_file.read()

    content_length = len(content)
    decode_index = 0

    while decode_index < content_length:
        try:

            obj, decode_index = decoder.raw_decode(content, decode_index)
            mydict = obj
            deser = str(mydict.values())
            deser2 = deser.replace("}, {", ", ").replace("dict_values([", '').replace("])", ",").replace("'",
                                                                                                         '"').replace(
                '"is_deleted": False', '"is_deleted": "False"').replace('"is_deleted": True',
                                                                        '"is_deleted": "True"')  # .replace('"{"','{"')

            with open("test2.json", "a+") as f:
                f.write(deser2)


        except Exception as e:
            print("JSONDecodeError:", e)
            # Scan forward and keep trying to decode
            decode_index += 1

with open("test2.json", 'a+') as q:
    q.seek(0, 2)
    q.write("]")

with open("test2.json", 'r') as z:
    for row in z:
        newrow = str(row).replace(',]', ']')

        with open("test3.json", "w+") as d:
            d.write(newrow)

newj = json.load(open("test3.json"))

for line in newj:
    result = (
    line["operation"], line["MVE_GKEY"], line["MOVE_KIND"], line["UFV_GKEY"], line["LINE_OP"], #line["CARRIER_GKEY"],
    line["EXCLUDE"], line["FM_POS_LOCTYPE"], line["FM_POS_LOCID"], line["FM_POS_LOC_GKEY"], line["FM_POS_SLOT"],
    line["FM_POS_NAME"], line["FM_POS_BIN"], line["FM_POS_TIER"], line["TO_POS_LOCTYPE"], line["TO_POS_LOCID"],
    line["TO_POS_LOC_GKEY"], line["TO_POS_SLOT"], line["TO_POS_NAME"], #line["CHE_FETCH"],
    #line["CHE_CARRY"],
    #line["CHE_PUT"], #line["CHE_QC"],
     line["DIST_START"], line["DIST_CARRY"], #line["T_CARRY_COMPLETE"],
    #line["T_DISPATCH"],
    #line["T_FETCH"],
    line["T_PUT"], #line["T_CARRY_FETCH_READY"],
    #line["T_CARRY_PUT_READY"],
    #line["T_CARRY_DISPATCH"],
    line["REHANDLE_COUNT"], line["TWIN_FETCH"], line["TWIN_CARRY"], line["TWIN_PUT"], #line["PROCESSED"],
    #line["POW"],
    #line["CHE_CARRY_LOGIN_NAME"],
    #line["CHE_PUT_LOGIN_NAME"], #line["CHE_FETCH_LOGIN_NAME"],
    line["CATEGORY"],
    line["FREIGHT_KIND"], line["is_deleted"])
    # print(line)
    print(result)
# except Exception as e:
#     print(e)
