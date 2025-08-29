@echo off
title Inquiro AI Starter
echo Starting Inquiro AI...

:: OPTIONAL - Activate virtual environment if you have one
:: call venv\Scripts\activate

:: Start backend in new terminal
start cmd /k "uvicorn backend:app --host 127.0.0.1 --port 9999 --reload"

:: Wait 2 seconds for backend to start
timeout /t 2 /nobreak >nul

:: Start frontend in another terminal
start cmd /k "streamlit run frontend.py"

echo Backend and Frontend are now running.
pause
