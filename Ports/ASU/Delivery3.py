# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyodbc


cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=CASC9MSDB03;"
                      "Database=stg_mainpac_Prd;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
#cursor.execute('SELECT name FROM sys.tables')


# Reading the data from file into DataFrames
cursor.execute("SELECT * FROM WorkOrderDetail")
workOrderTable1 = cursor.fetchall()
workOrderTable2 = workOrderTable1[pd.notnull(workOrderTable1.Model) | pd.notnull(workOrderTable1.Make)]

operAssTable1 = cursor.execute("SELECT * FROM OperationalAsset")
operAssTable = operAssTable1[pd.notnull(operAssTable1.Make)]

# Additional filters in Operational Asset - May be required - Confirm with MARTHA
operAssTable = operAssTable[
    (operAssTable["SortKeyName"] != "INFRASTRUCTURE") & (operAssTable["SortKeyName"] != "AUXILIARY")]

operAssTable['Name'] = operAssTable['Name'].astype(str)
operAssTable = operAssTable[
    ~operAssTable["Name"].str.contains("GROUP") & ~operAssTable["Name"].str.contains("AA") & ~operAssTable[
        "Name"].str.contains("TM") & ~operAssTable["Name"].str.contains("PRE-TRIP") & ~operAssTable[
        "Name"].str.contains("WITHOUT") & ~operAssTable["Name"].str.contains("RETIRED") & ~operAssTable[
        "Name"].str.contains("MISC")]

workOrderTable2 = workOrderTable2[~workOrderTable2["OperationalAssetName"].str.contains("GROUP") & ~workOrderTable2[
    "OperationalAssetName"].str.contains("AA") & ~workOrderTable2["OperationalAssetName"].str.contains("TM") & ~
                                  workOrderTable2["OperationalAssetName"].str.contains("PRE-TRIP") & ~workOrderTable2[
    "OperationalAssetName"].str.contains("WITHOUT") & ~workOrderTable2["OperationalAssetName"].str.contains(
    "RETIRED") & ~workOrderTable2["OperationalAssetName"].str.contains("MISC")]

# Inner Join between Operational Assets and Workorders
workOrderTable = pd.merge(workOrderTable2, operAssTable[['OperationalAssetID']], how='inner',
                          left_on=['OperationalAssetID'], right_on=['OperationalAssetID'])

# Taking only the columns that are required
workOrderTable = workOrderTable[
    ['OperationalAssetID', 'OperationalAssetName', 'Make', 'Model', 'Year', 'NatureOfFaultDescription', 'MakenMod',
     'WorkTypeName']]
operAssTable = operAssTable[['OperationalAssetID', 'Name', 'Make', 'Model', 'Year', 'MakenMod', 'SortKeyName']]

# List of Incorrect Makes to correct
replaceList1 = ['terex/noel', 'terex/noell', 'terex noel', 'terex noell', 'noell', 'terex/fantuzzi reggiane',
                'terex/fantuzzi']
replaceList2 = ['fantuzzi reggiani', 'fantuzzi', 'fantuzzi reggiane']
replaceList3 = ['chev', 'chevrolet', 'chevy']
replaceList4 = ['frueha', 'fruehauf', 'freuhauf']

workOrderTable['Make'] = workOrderTable['Make'].str.strip()
workOrderTable['Model'] = workOrderTable['Model'].str.strip()
workOrderTable['MakenMod'] = workOrderTable['MakenMod'].str.strip()

operAssTable['Make'] = operAssTable['Make'].str.strip()
operAssTable['Model'] = operAssTable['Model'].str.strip()
operAssTable['MakenMod'] = operAssTable['MakenMod'].str.strip()

# To replace and correct values of Makes
for operAssData in [workOrderTable, operAssTable]:
    operAssData['Make'] = operAssData['Make'].str.lower()
    operAssData['Model'] = operAssData['Model'].str.lower()
    operAssData['MakenMod'] = operAssData['MakenMod'].str.lower()

    for element in replaceList1:
        operAssData.replace(to_replace=element, value='terex', inplace=True)
    for element in replaceList2:
        operAssData.replace(to_replace=element, value='fantuzzi', inplace=True)
    for element in replaceList3:
        operAssData.replace(to_replace=element, value='chevrolet', inplace=True)
    for element in replaceList4:
        operAssData.replace(to_replace=element, value='fruehauf', inplace=True)

    operAssData.replace(to_replace='liebherr-america', value='liebherr', inplace=True)
    operAssData.replace(to_replace='maffi', value='mafi', inplace=True)
    operAssData.replace(to_replace='sterling/lorain', value='sterling', inplace=True)
    operAssData.replace(to_replace='taylor dunn', value='taylor', inplace=True)
    operAssData.replace(to_replace='theuer', value='theurer', inplace=True)
    operAssData.replace(to_replace='utility enterprise', value='utility', inplace=True)
    operAssData.replace(to_replace='tug mfg', value='tug', inplace=True)
    operAssData.replace(to_replace='track mobile', value='trackmobile', inplace=True)

    operAssData.replace(to_replace='treberg', value='terberg', inplace=True)
    operAssData.replace(to_replace='fontai', value='fontaine', inplace=True)

operMake = operAssTable.groupby('Make')["OperationalAssetID"].count().reset_index(name="CountOfAssetMakes")
# operMake.to_csv('operAssMake.csv',columns=['Make','CountOfAssetMakes'],index=False)

# Take only Fail, Failold, SCH, SCHold, Tires work types
workOrderMMFails = workOrderTable[
    (workOrderTable.WorkTypeName == 'FAIL') | (workOrderTable.WorkTypeName == 'FAILold') | (
                workOrderTable.WorkTypeName == 'SCH') | (workOrderTable.WorkTypeName == 'SCHold') | (
                workOrderTable.WorkTypeName == 'TIRES')]
# workOrderMMFails.to_csv('workOrderMMFails.csv',index=False)

wOrderOper1 = pd.merge(workOrderMMFails, operMake, how='left', left_on=['Make'], right_on=['Make'])

# Counts of Work Orders Based on Make
workOrderMake = workOrderMMFails.groupby('Make')["OperationalAssetID"].count().reset_index(
    name="CountOfMakesInWorkOrders")
# workOrderMake.to_csv('workOrderMakeCounts.csv',columns=['Make','CountOfMakesInWorkOrders'],index=False)

wOrderOper2 = pd.merge(wOrderOper1, workOrderMake, how='left', left_on=['Make'], right_on=['Make'])

# Counts of Work Orders Based on Model
workOrderModel = workOrderMMFails.groupby('MakenMod')["OperationalAssetID"].count().reset_index(name="CountOfModels")
# workOrderModel2=workOrderMMFails.groupby('MakenMod').count().reset_index(name="CountOfModels")
# workOrderModel.to_csv('workOrderModelCounts.csv',columns=['Model','CountOfModels'],index=False)

wOrderOper3 = pd.merge(wOrderOper2, workOrderModel, how='left', left_on=['MakenMod'], right_on=['MakenMod'])

# Counts of Operational Assets Based on Model
operModel = operAssTable.groupby('MakenMod')["OperationalAssetID"].count().reset_index(name="CountOfAssetModels")
# operModel.to_csv('operAssModel.csv',columns=['Model','CountOfAssetModels'],index=False)

wOrderOper4 = pd.merge(wOrderOper3, operModel, how='left', left_on=['MakenMod'], right_on=['MakenMod'])

wOrderOper5 = pd.merge(wOrderOper4, operAssTable[['OperationalAssetID', 'SortKeyName']], how='left',
                       left_on=['OperationalAssetID'], right_on=['OperationalAssetID'])

wOrderOper5.to_csv('C:\\Users\\seangi\\OneDrive - Ports America\\_Projects\EDW\Mainpac\\2018_ASU\\Ports America Final Deliverables\\Ports America Final Deliverables\\Del_3_Make_Model\\Delivery3_Output.csv', index=False)
