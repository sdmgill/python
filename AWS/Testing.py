from boto3 import client

files = []
conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
for key in conn.list_objects(Bucket='pa-bi')['Contents']:
    files.append(key['Key'])

load_files = [s for s in files if 'LOAD' in s]
latch_type_files = [s for s in load_files if 'LatchType' in s]
processed_files = []

while latch_type_files:
    current_file=latch_type_files.pop()
    new_file = current_file.replace('LOAD', 'INITIAL')

    print("Processing file: " + current_file + " and renameing to: " + new_file)