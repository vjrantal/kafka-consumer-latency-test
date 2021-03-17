import os

from dotenv import load_dotenv
load_dotenv()


def get_kafka_config():
    return {
        'bootstrap_servers': os.environ['BOOTSTRAP_SERVERS'],
        'security_protocol': 'SASL_SSL',
        'sasl_mechanism': 'PLAIN',
        'sasl_plain_username': '$ConnectionString',
        'sasl_plain_password': os.environ['SASL_PLAIN_PASSWORD']
    }


def get_kafka_topic():
    return os.environ['KAFKA_TOPIC_NAME']
