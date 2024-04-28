import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    return {
        'PORT': int(os.getenv('PORT', 8000))
    }
