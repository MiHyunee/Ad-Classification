import boto3
import time

def get_records(streamName):
    client = boto3.client('kinesis', region_name='ap-northeast-1', aws_access_key_id='AKIARW7HGNHWTGRI2GVZ', aws_secret_access_key='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')

    response = client.describe_stream(StreamName=streamName)

    my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']
    # shard가 여러개이거나 reshard되어 일시적으로 여러개인 경우 Shards 갯수만큼 for loop 해야함.

    shard_iterator = client.get_shard_iterator(StreamName=streamName, ShardId=my_shard_id, ShardIteratorType='TRIM_HORIZON')

    my_shard_iterator = shard_iterator['ShardIterator']

    record_response = client.get_records(ShardIterator=my_shard_iterator, Limit=10)

    while 'NextShardIterator' in record_response:
        record_response = client.get_records(ShardIterator=record_response['NextShardIterator'], Limit=10)
        # get_records 매번 호출시마다 NextShardIterator 값이 나오므로, 그걸로 session(?)을 유지해서 놓치는 데이터가 없도록 함.

        response = record_response['Records']
        if(len(response)>0):
            print(response) #페이지 연결되면 삭제 (확인용 출력 코드)
            return record_response['Records']

