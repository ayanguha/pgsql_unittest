# Objective

This project is a sample project as an instructive module for automating `unit test` in data engineering


# What does this project do?

This project has following (very simple) features

- Use AWS SSM service to get database connection keys (currently postgres only)
- Set up and destroy unit test fixtures
- Run a set of tests

# Prerequisite

- Python 3.7+
- Pip compable with Python 3.x

This readme assumes you have `pip3` to point to pip and `python3` to point to Python 3.

# Steps to get it working


### Create AWS Profile Locally

Create a local AWS credential profile following instructions
https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/keys-profiles-credentials.html

Note the profile name  


### Create AWS SSM Entries
Use AWS Secret manager to create secrets related to database connections.

  `Expected Keys:
  'SecretString': '{"username":"username",
                       "password":"password ",
                       "engine":"postgres",
                       "host":"hostname",
                       "port":5432,
                       "dbInstanceIdentifier":"database"}'`



### Create Python Virtual Env & Activate it

`python3 -m venv pgsql_unittest`
`source <virtual_env_loc>/pgsql_unittest/bin/activate`

### Clone this repo

`git clone <this repo>`

### Install dependencies

`pip3 install -r requirements.txt`

### Modify `config`

Configure the app. Following tokens are expected.

`secret_id = "your_secret_name"
profile_name = "your_profile_name"
region_name = 'your_region_name'`

There is a `config.py.template` is provided - you can rename it to `config.py` and modify.

### Run Tests

`python3 test.py`
