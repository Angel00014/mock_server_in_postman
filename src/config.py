from dotenv import load_dotenv
import os


load_dotenv()

base_url_mock = os.getenv('BASE_URL_MOCK')
auth_token = os.getenv('AUTH_TOKEN')
