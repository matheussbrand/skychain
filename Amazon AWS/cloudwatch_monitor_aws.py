# Configure the CloudWatch client for monitoring and logs

import boto3
import logging

def setup_cloudwatch_logging():
    client = boto3.client('logs', region_name='us-west-2')
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Configure logs for a specific log group
    client.create_log_group(logGroupName='API_Access')
    client.put_log_events(
        logGroupName='API_Access',
        logStreamName='API_Access_Stream',
        logEvents=[
            {
                'timestamp': int(time.time()* 1000),
                'message': 'API access started'
            }
        ]
    )