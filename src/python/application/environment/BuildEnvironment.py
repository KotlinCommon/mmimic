import os
from dotenv import load_dotenv


def buildEnvironment():
    projectRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
    dockerEnvDevPath = os.path.join(projectRoot, '.docker', '.env.dev')
    dockerEnvProdPath = os.path.join(projectRoot, '.docker', '.env.prod')
    nonDockerEnvPath = os.path.join(projectRoot, 'src', 'resources', 'environment', '.env')
    if os.path.isfile(dockerEnvDevPath):
        load_dotenv(dockerEnvDevPath)
    elif os.path.isfile(dockerEnvProdPath):
        load_dotenv(dockerEnvProdPath)
    elif os.path.isfile(nonDockerEnvPath):
        load_dotenv(nonDockerEnvPath)
    else:
        raise FileNotFoundError("No .env file found")
