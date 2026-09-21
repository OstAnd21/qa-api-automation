# QA API Automation

API automation testing project built with Python, pytest, and requests.

## Tech Stack

- Python 3.14
- pytest
- requests
- JSON Schema
- Allure
- Git
- GitHub Actions

## Project Structure

```text
qa-api-automation/
├── api/
│   ├── base_api.py
│   └── users_api.py
├── schemas/
│   └── user_schema.py
├── test_data/
│   └── users_data.py
├── tests/
│   ├── conftest.py
│   ├── test_create_users.py
│   ├── test_delete_users.py
│   ├── test_errors.py
│   ├── test_get_users.py
│   ├── test_response_validator.py
│   ├── test_update_users.py
│   ├── test_users_mock.py
│   ├── test_users_parametrize.py
│   ├── test_users_schema.py
│   ├── test_users_schema_negative.py
│   └── test_users_validation.py
├── utils/
│   ├── allure_helpers.py
│   ├── logger.py
│   └── response_validator.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── .gitignore
├── config.py
├── pytest.ini
└── requirements.txt
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/OstAnd21/qa-api-automation.git
cd qa-api-automation
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run tests

```bash
python -m pytest
```

### 4. Run tests with logs

```bash
python -m pytest -s
```

## Test Results

80 tests passed.

## CI/CD

Tests are automatically executed using GitHub Actions on:
- push to master
- pull requests to master
