from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    ENV = os.getenv(
        "ENV",
        "test"
    )
    
    BASE_URL = os.getenv(
        "BASE_URL",
        "https://jsonplaceholder.typicode.com"
    )
    
    RETRY_STATUS = int(
        os.getenv(
            "RETRY_STATUS",
            "3"
        )
    )

    RETRY_BACKOFF_FACTOR = float(
        os.getenv(
            "RETRY_BACKOFF_FACTOR",
            "1"
        )
    )

    ALLOWED_ENVS = {"dev", "test", "prod"}
    def validate(self):
        if self.ENV not in self.ALLOWED_ENVS:
            raise ValueError(
                f"Unknown environment: {self.ENV}. "
                f"Allowed: {self.ALLOWED_ENVS}"
            )
        

settings = Settings()
settings.validate()