from config import settings


def test_environment():
    assert settings.ENV in {"dev", "test", "prod"}

def test_base_url():
    assert settings.BASE_URL.startswith("https://")