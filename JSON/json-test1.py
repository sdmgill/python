import ast
import json

# d1 = json.load(open("oneline.json"))
# print(d1)

# d2 = json.load(open("PALSCostWithPP_mod.json"))
# for line in d2:
#     for k,v in line.items():
#         print(k,v)

d3 = json.load(open("fh-pnct-n4-invmoveevent.json"))
for line in d3:
    for kv in line.items():
        print(kv[0])

# d4 = json.load(open("PALSCostWithPP_mod.json"))
# for line in d4:
#     # print(type(line))
#     print(line)


# d5 = json.load(open("PALSCostWithPP_mod.json"))
# for line in d5:
#     result = (line['CompanyGLString'],line['GLString'],line['JobNumber'],line['ServiceGLString'],line['CustomerGLString'],line['PayPeriodId'],
#           line['PayPeriod'],line['RosterId'],line['BadgeNumber'],line['FullName'],line['JobCodeId'],line['JobCode'],line['JobCodeDescription'],
#           line['TimesheetDetailId'],line['STUnitHrs'],line['STHrs'],line['STRate'],line['STWages'],line['OTUnitHrs'],line['OTHrs'],line['OTRate'],
#           line['OTWages'],line['MHUnitHrs'],line['MHHrs'],line['MHRate'],line['MHWages'],line['FTUnitHrs'],line['FTHrs'],line['FTRate'],
#           line['FTWages'],line['DTUnitHrs'],line['DTHrs'],line['DTRate'],line['DTWages'],line['PensionBurdenRate'],line['UnallocatedBurdenRate'],
#           line['FICARate'],line['FUIRate'],line['SUIRate'],line['WorkersCompRate'],line['STFICA'],line['STFUI'],line['STSUI'],line['STWorkersComp'],
#           line['STPension'],line['STUnallocated'],line['OTFICA'],line['OTFUI'],line['OTSUI'],line['OTWorkersComp'],line['OTPension'],
#           line['OTUnallocated'],line['MHFICA'],line['MHFUI'],line['MHSUI'],line['MHWorkersComp'],line['MHPension'],line['MHUnallocated'],
#           line['FTFICA'],line['FTFUI'],line['FTSUI'],line['FTWorkersComp'],line['FTPension'],line['FTUnallocated'],line['DTFICA'],line['DTFUI'],
#           line['DTSUI'],line['DTWorkersComp'],line['DTPension'],line['DTUnallocated'])
#     sql = (f"insert into mytable values {result}")
#     print(sql)


# read in PALS data
# d6 = json.load(open("PALS Cost-formatted with PP.json"))
# # iterate through records
# for line in d6:
#     # need to enforce order from the Dict, grabbing only the Values of the Key:Value pairings
#     result = (line['CompanyGLString'],line['GLString'],line['JobNumber'],line['ServiceGLString'],line['CustomerGLString'],line['PayPeriodId'],
#           line['PayPeriod'],line['RosterId'],line['BadgeNumber'],line['FullName'],line['JobCodeId'],line['JobCode'],line['JobCodeDescription'],
#           line['TimesheetDetailId'],line['STUnitHrs'],line['STHrs'],line['STRate'],line['STWages'],line['OTUnitHrs'],line['OTHrs'],line['OTRate'],
#           line['OTWages'],line['MHUnitHrs'],line['MHHrs'],line['MHRate'],line['MHWages'],line['FTUnitHrs'],line['FTHrs'],line['FTRate'],
#           line['FTWages'],line['DTUnitHrs'],line['DTHrs'],line['DTRate'],line['DTWages'],line['PensionBurdenRate'],line['UnallocatedBurdenRate'],
#           line['FICARate'],line['FUIRate'],line['SUIRate'],line['WorkersCompRate'],line['STFICA'],line['STFUI'],line['STSUI'],line['STWorkersComp'],
#           line['STPension'],line['STUnallocated'],line['OTFICA'],line['OTFUI'],line['OTSUI'],line['OTWorkersComp'],line['OTPension'],
#           line['OTUnallocated'],line['MHFICA'],line['MHFUI'],line['MHSUI'],line['MHWorkersComp'],line['MHPension'],line['MHUnallocated'],
#           line['FTFICA'],line['FTFUI'],line['FTSUI'],line['FTWorkersComp'],line['FTPension'],line['FTUnallocated'],line['DTFICA'],line['DTFUI'],
#           line['DTSUI'],line['DTWorkersComp'],line['DTPension'],line['DTUnallocated'])
#     #prep call to Snowflake
#     sql = (f"insert into mytable values {result}")
#     print(sql)





# with open('oneline.json','r') as f:
#     data = ast.literal_eval(f.read())
#     # data = eval(f.read())
#     print(data)


# def reading(self):
#     with open('PALSCostWithPP.json', 'r') as f:
#         s = f.read()
#         self.whip = ast.literal_eval(s)
#         return(self.whip)
#         print(self.whip)

# dic = open('PALSCostWithPP.json', 'r')
#
# print(dic)

