import boto3

session = boto3.Session(profile_name='slalomlabs')
rds_data = session.client('rds-data', region_name = 'us-east-1')

db_clust_arn = 'arn:aws:rds:us-east-1:747843067444:cluster:rb-dev'

db_secret_arn = 'arn:aws:secretsmanager:us-east-1:747843067444:secret:rb/dev-N2BHBV'



sql = """
    select * from test
        """


response1 = rds_data.execute_statement(
        resourceArn = db_clust_arn,
        secretArn = db_secret_arn,
        database = 'postgres',
        sql = sql)

#recs is a list (of rows returned from Db)
recs = response1['records']
print(recs)
