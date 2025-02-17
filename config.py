import os

from dotenv import load_dotenv

load_dotenv()
USER_MONGO = os.getenv('USER_MONGO')
PASSWORD_MONGO = os.getenv('PASSWORD_MONGO')
uri = f'mongodb+srv://{USER_MONGO}:{PASSWORD_MONGO}@mycluster.mnzxi.mongodb.net/?retryWrites=true&w=majority&appName=myCluster'
print(uri)