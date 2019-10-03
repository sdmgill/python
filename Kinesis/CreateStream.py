import boto3

client = boto3.client('kinesis', region_name='us-west-2')

response = client.create_stream(
    StreamName='BotoDemo',
    ShardCount=1
)

# response = client.describe_stream(StreamName='BotoDemo',Limit=1,ExclusiveStartShardId='shardId-000000000000')
response = client.describe_stream(StreamName='BotoDemo')
print(response)
# my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']

response2 = client.list_streams()
print(response2)

