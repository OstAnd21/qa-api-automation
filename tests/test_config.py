from config import ENV, BASE_URL


def test_environment():
    assert ENV in {"dev", "test", "prod"}

def test_base_url():
    assert BASE_URL.startswith("https://")