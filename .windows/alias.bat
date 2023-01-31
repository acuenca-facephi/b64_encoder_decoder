@echo off
REM TODO: Append the doskey to existing AutoRun instead overwritting.

ECHO Installing Base64 Encoder/Decoder...
SET parent=%~dp0
FOR %%a IN ("%parent:~0,-1%") DO SET grandparent=%%~dpa
REG ADD "HKLM\Software\Microsoft\Command Processor" /f /v "AutoRun" /d "DOSKEY b64ed=python3 \"%grandparent%\main.py\" $*"
ECHO Now you can run 'b64ed' command
PAUSE
