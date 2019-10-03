import boto3

client = boto3.client('lambda', region_name='us-west-2')

client.update_function_configuration(
    FunctionName='mistar-pnct-incremental-fm-cleanup',
    Environment={
        'Variables': {
            'S3_FOLDER': 'mistar/pnct/incremental/fm/tire/',
            'SOURCE_BUCKET' : 'pa-dms-staging',
            'TARGET_BUCKET' : 'pa-processed'
        }
    }
)

client.invoke(FunctionName='mistar-pnct-incremental-fm-cleanup')