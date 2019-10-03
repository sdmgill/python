import json
import pymssql

# conn = pymssql.connect(host=r'CASC9MSDD04',
#                        # Credentials not required if coming from a Windows Machine. Assumed Trusted Connection uses
#                        # AD Authentication.
#                        # user=r'ports\seangi',
#                        # password='',
#                        database='Staging')
#
# cursor = conn.cursor()


d6 = json.load(open("fh-pnct-n4-invmoveevent.json"))

d7 = d6.map(lambda x : re.sub("}{", "}\n{", x, flags=re.UNICODE)).flatMap(lambda line: line.split("\n"))
# iterate through records
# for line in d6:
#     # need to enforce order from the Dict, grabbing only the Values of the Key:Value pairings
#     result = (line['CompanyGLString'],line['GLString'],line['JobNumber'],line['ServiceGLString'],line['CustomerGLString'],line['PayPeriodId'],
#           line['PayPeriod'],line['WorkDate'],line['RosterId'],line['BadgeNumber'],line['FullName'],line['JobCodeId'],line['JobCode'],line['JobCodeDescription'],
#           line['TimesheetDetailId'],line['STUnitHrs'],line['STHrs'],line['STRate'],line['STWages'],line['OTUnitHrs'],line['OTHrs'],line['OTRate'],
#           line['OTWages'],line['MHUnitHrs'],line['MHHrs'],line['MHRate'],line['MHWages'],line['FTUnitHrs'],line['FTHrs'],line['FTRate'],
#           line['FTWages'],line['DTUnitHrs'],line['DTHrs'],line['DTRate'],line['DTWages'],line['PensionBurdenRate'],line['UnallocatedBurdenRate'],
#           line['FICARate'],line['FUIRate'],line['SUIRate'],line['WorkersCompRate'],line['STFICA'],line['STFUI'],line['STSUI'],line['STWorkersComp'],
#           line['STPension'],line['STUnallocated'],line['OTFICA'],line['OTFUI'],line['OTSUI'],line['OTWorkersComp'],line['OTPension'],
#           line['OTUnallocated'],line['MHFICA'],line['MHFUI'],line['MHSUI'],line['MHWorkersComp'],line['MHPension'],line['MHUnallocated'],
#           line['FTFICA'],line['FTFUI'],line['FTSUI'],line['FTWorkersComp'],line['FTPension'],line['FTUnallocated'],line['DTFICA'],line['DTFUI'],
#           line['DTSUI'],line['DTWorkersComp'],line['DTPension'],line['DTUnallocated'])

print(d7)







    #prep call to Snowflake
#     sql = (f"insert into WRKPALSLaborAll values {result}")
#     cursor.execute(sql)
#
# # cursor.execute(sql)
# conn.commit()
#
# conn.close()