from dotenv import load_dotenv()
import from os

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API KEY not found in the env file")