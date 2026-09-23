from dotenv import load_dotenv
import os

load_dotenv()

ENV = os.getenv(
    "ENV",
    "test"
)

ALLOWED_ENVS = {"dev", "test", "prod"}
if ENV not in ALLOWED_ENVS:
    raise ValueError(
        f"Unknown environment: {ENV}. "
        f"Allowed: {ALLOWED_ENVS}"
    )

BASE_URL = os.getenv(
    "BASE_URL",
    "https://jsonplaceholder.typicode.com"
)