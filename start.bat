@echo off
title Offline AI Study Assistant

echo ==========================================
echo     Offline AI Study Assistant
echo ==========================================
echo.

echo [1/3] Checking Ollama...

ollama --version >nul 2>&1

if errorlevel 1 (
    echo.
    echo ERROR: Ollama is not installed or not available in PATH.
    echo Please make sure Ollama is installed.
    echo.
    pause
    exit /b
)

echo Ollama is available.
echo.

echo [2/3] Starting Ollama...

start "" /min ollama serve

timeout /t 3 /nobreak >nul

echo.
echo [3/3] Starting Study Assistant...
echo.

call .venv\Scripts\activate.bat

start "" http://127.0.0.1:5000

python app.py

pause