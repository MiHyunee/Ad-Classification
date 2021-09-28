# -*- coding: utf-8 -*-

import boto3
import json

def put_to_stream(thing_id, property_value, property_timestamp, streamName):
    key_id = ''
    secret_key = ''
    client = boto3.client('kinesis', region_name='ap-northeast-1', aws_access_key_id=key_id,
                          aws_secret_access_key=secret_key)

    payload = {
                'Data': str(property_value),
                'timestamp': str(property_timestamp),
                'partition key': thing_id
              }

    client.put_record(StreamName=streamName,
                      Data=json.dumps(payload),
                      PartitionKey=thing_id)