import boto3
import json
import time

client = boto3.client('kinesis', region_name='us-west-2')

stream_name = 'PALSData'

response = client.describe_stream(StreamName=stream_name)

shard_id = response['StreamDescription']['Shards'][0]['ShardId']

# print(shard_id)

# shard_it = client.get_shard_iterator(StreamName=stream_name,ShardId=shard_id,ShardIteratorType='LATEST')
shard_it = client.get_shard_iterator(StreamName=stream_name,ShardId=shard_id,ShardIteratorType='TRIM_HORIZON')

my_shard_it = shard_it['ShardIterator']
# print(shard_it)

record_response = client.get_records(ShardIterator=my_shard_it,Limit=2)

while 'NextShardIterator' in record_response:
    record_response = client.get_records(ShardIterator=record_response['NextShardIterator'],Limit=2)

    for o in record_response['Records']:
        jdat = json.loads(o['Data'])
        result = (jdat['CompanyGLString'], jdat['GLString'], jdat['JobNumber'], jdat['ServiceGLString'],
                      jdat['CustomerGLString'] or 0, jdat['PayPeriodId'],
                      jdat['PayPeriod'], jdat['WorkDate'], jdat['RosterId'], jdat['BadgeNumber'], jdat['FullName'],
                      jdat['JobCodeId'], jdat['JobCode'], jdat['JobCodeDescription'],
                      jdat['TimesheetDetailId'], jdat['STUnitHrs'], jdat['STHrs'], jdat['STRate'], jdat['STWages'],
                      jdat['OTUnitHrs'], jdat['OTHrs'], jdat['OTRate'],
                      jdat['OTWages'], jdat['MHUnitHrs'], jdat['MHHrs'], jdat['MHRate'], jdat['MHWages'],
                      jdat['FTUnitHrs'], jdat['FTHrs'], jdat['FTRate'],
                      jdat['FTWages'], jdat['DTUnitHrs'], jdat['DTHrs'], jdat['DTRate'], jdat['DTWages'],
                      jdat['PensionBurdenRate'], jdat['UnallocatedBurdenRate'],
                      jdat['FICARate'], jdat['FUIRate'], jdat['SUIRate'], jdat['WorkersCompRate'], jdat['STFICA'],
                      jdat['STFUI'], jdat['STSUI'], jdat['STWorkersComp'],
                      jdat['STPension'], jdat['STUnallocated'], jdat['OTFICA'], jdat['OTFUI'], jdat['OTSUI'],
                      jdat['OTWorkersComp'], jdat['OTPension'],
                      jdat['OTUnallocated'], jdat['MHFICA'], jdat['MHFUI'], jdat['MHSUI'], jdat['MHWorkersComp'],
                      jdat['MHPension'], jdat['MHUnallocated'],
                      jdat['FTFICA'], jdat['FTFUI'], jdat['FTSUI'], jdat['FTWorkersComp'], jdat['FTPension'],
                      jdat['FTUnallocated'], jdat['DTFICA'], jdat['DTFUI'],
                      jdat['DTSUI'], jdat['DTWorkersComp'], jdat['DTPension'], jdat['DTUnallocated'])
        print(result)

        # print(jdat)
    # for metadata in jdat.items():
    #     print(metadata)

    # wait for 5 seconds
    time.sleep(0.2)