@echo off
REM Активация виртуального окружения
if exist .venv\Scripts\activate.bat (
    call .venv\Scripts\activate.bat
) else (
    if exist .venv\Scripts\activate.bat (
        call .venv\Scripts\activate.bat
    ) else (
        echo Виртуальное окружение не найдено!
        echo Создаю виртуальное окружение...
        python -m venv venv
        call venv\Scripts\activate.bat
    )
)

uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

pause