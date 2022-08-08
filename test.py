import unittest
from client import *
from sqlalchemy import create_engine
import config

class TestPGSQL(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        secret_id = config.secret_id
        client = create_secrets_manager_client()
        secrets = get_secret_value_by_id(client, secret_id)
        engine_str = 'postgresql://{username}:{password}@{host}:{port}/{dbInstanceIdentifier}'.format(**secrets)
        print(engine_str)
        engine = create_engine(engine_str)
        cls.connection = engine.connect()


    def setUp(self):
        self.connection = TestPGSQL.connection




    def test_case1(self):
        sql = open("test_case1.sql").read()
        res = self.connection.execute(sql).fetchall()


        self.assertEqual(len(res), 2)

    def test_case2(self):
        sql = open("test_case2.sql").read()
        res = self.connection.execute(sql).fetchall()
        ## Suppossed to fail 
        self.assertEqual(res[0][0], 2)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestPGSQL('test_case1'))
    suite.addTest(TestPGSQL('test_case2'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
