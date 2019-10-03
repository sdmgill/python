import snowflake.connector
import json

con = snowflake.connector.connect(
  user= 'sdmgill',
  password= 'Sn0wB@llZ',
  account= 'le31528',
  autocommit=True)

cursor = con.cursor()
cursor.execute("USE WAREHOUSE LOAD_WH")
cursor.execute("USE STAGING_DB.PUBLIC")

d6 = json.load(open("PALSGulfportPP1419.json"))
# iterate through records
for line in d6:
    # need to enforce order from the Dict, grabbing only the Values of the Key:Value pairings
    result = (line['CompanyGLString'],line['GLString'],line['JobNumber'],line['ServiceGLString'],line['CustomerGLString'] or 0,line['PayPeriodId'],
          line['PayPeriod'],line['WorkDate'],line['RosterId'],line['BadgeNumber'],line['FullName'],line['JobCodeId'],line['JobCode'],line['JobCodeDescription'],
          line['TimesheetDetailId'],line['STUnitHrs'],line['STHrs'],line['STRate'],line['STWages'],line['OTUnitHrs'],line['OTHrs'],line['OTRate'],
          line['OTWages'],line['MHUnitHrs'],line['MHHrs'],line['MHRate'],line['MHWages'],line['FTUnitHrs'],line['FTHrs'],line['FTRate'],
          line['FTWages'],line['DTUnitHrs'],line['DTHrs'],line['DTRate'],line['DTWages'],line['PensionBurdenRate'],line['UnallocatedBurdenRate'],
          line['FICARate'],line['FUIRate'],line['SUIRate'],line['WorkersCompRate'],line['STFICA'],line['STFUI'],line['STSUI'],line['STWorkersComp'],
          line['STPension'],line['STUnallocated'],line['OTFICA'],line['OTFUI'],line['OTSUI'],line['OTWorkersComp'],line['OTPension'],
          line['OTUnallocated'],line['MHFICA'],line['MHFUI'],line['MHSUI'],line['MHWorkersComp'],line['MHPension'],line['MHUnallocated'],
          line['FTFICA'],line['FTFUI'],line['FTSUI'],line['FTWorkersComp'],line['FTPension'],line['FTUnallocated'],line['DTFICA'],line['DTFUI'],
          line['DTSUI'],line['DTWorkersComp'],line['DTPension'],line['DTUnallocated'])
    #prep call to Snowflake
    sql = (f"insert into WRKPALSLaborAll (CompanyID,SiteID,JobNumber,ServiceID,CustomerID,PayPeriodId,PayPeriod,WorkDate,RosterId,"
           f"BadgeNumber,FullName,JobCodeId,JobCode,JobCodeDescription,TimesheetDetailId,STUnitHrs,STHrs,STRate,STWages,"
           f"OTUnitHrs,OTHrs,OTRate,OTWages,MHUnitHrs,MHHrs,MHRate,MHWages,FTUnitHrs,FTHrs,FTRate,FTWages,DTUnitHrs,DTHrs,"
           f"DTRate,DTWages,PensionBurdenRate,UnallocatedBurdenRate,FICARate,FUIRate,SUIRate,WorkersCompRate,STFICA,STFUI,"
           f"STSUI,STWorkersComp,STPension,STUnallocated,OTFICA,OTFUI,OTSUI,OTWorkersComp,OTPension,OTUnallocated,MHFICA,"
           f"MHFUI,MHSUI,MHWorkersComp,MHPension,MHUnallocated,FTFICA,FTFUI,FTSUI,FTWorkersComp,FTPension,FTUnallocated,"
           f"DTFICA,DTFUI,DTSUI,DTWorkersComp,DTPension,DTUnallocated) values {result}")
    # cursor.execute(sql)

# cursor.execute(sql)
cursor.commit()

cursor.close()

