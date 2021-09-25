# -*- coding: utf-8 -*-

import boto3
import json

def put_to_stream(thing_id, property_value, property_timestamp, streamName):
    client = boto3.client('kinesis', region_name='ap-northeast-1', aws_access_key_id='AKIARW7HGNHWTGRI2GVZ', aws_secret_access_key='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')

    payload = {
                'Data': str(property_value),
                'timestamp': str(property_timestamp),
                'partition key': thing_id
              }

    client.put_record(StreamName=streamName,
                      Data=json.dumps(payload),
                      PartitionKey=thing_id)