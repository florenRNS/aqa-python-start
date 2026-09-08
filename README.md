# AQA Python Start — Junior Test Automation

![tests](https://github.com/FlorenRNS/aqa-python-start/actions/workflows/tests.yml/badge.svg)

Manual QA → AQA: API + UI автотесты с CI.

## Stack
Python, pytest, requests, Playwright, GitHub Actions

## Structure
- `pages/login_page.py` — PageObject для saucedemo login
- `test_auth.py` — API: POST /auth позитив + 3 негатива
- `test_ui.py` — UI: standard_user + locked_out_user
- `.github/workflows/tests.yml` — CI

## How to run
```bash
pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -v
```
## What is covered
- API auth: 200 + token, wrong pass, missing fields
- UI login: happy path to inventory, locked user error
- CI on every push