import boto3
import json
import config

def create_secrets_manager_client():
    profile_name = config.profile_name
    region_name = config.region_name
    session = boto3.Session(profile_name=profile_name)
    client = session.client('secretsmanager', region_name = region_name)
    return client

def get_secret_value_by_id(scm_client, secret_id ):

    response = scm_client.get_secret_value(SecretId=secret_id)
    secret_string = response['SecretString']
    '''
    Expected Keys:
    'SecretString': '{"username":"username",
                         "password":"password ",
                         "engine":"postgres",
                         "host":"hostname",
                         "port":5432,
                         "dbInstanceIdentifier":"database"}'
    '''
    secret_dict = json.loads(secret_string)
    return secret_dict
