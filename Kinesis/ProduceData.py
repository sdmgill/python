import boto3
import json

client = boto3.client('kinesis', region_name='us-west-2')

pals = json.load(open("PALSGulfportPP1419.json"))

for line in pals:
    client.put_records(
                Records=[
                            {
                                'Data': json.dumps(line),
                                'PartitionKey':'partitionkey'
                            },
                        ],
                StreamName = 'BotoDemo'
                )