# Configure the Google Stackdriver Registry Client

from google.cloud import logging

def setup_logging():
    client = logging.Client()
    logger = client.logger('api-access')

    # Access log 

    logger.log_text("API has been accessed", severity="INFO")

setup_logging()