@echo off
for /f "delims=" %%a in ('type "%~1"')do echo/%%a >> "new_%~nx1"
start "new_%~nx1"