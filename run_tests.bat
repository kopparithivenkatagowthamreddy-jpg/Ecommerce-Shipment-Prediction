@echo off
pip install -r requirements-api.txt
pytest tests -v
pause
