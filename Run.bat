@echo off
python listreplace.py
start "C:\Program Files\Mozilla Firefox\firefox.exe" .\webui-aria2\docs\index.html
aria2c --conf-path=./aria2.conf
