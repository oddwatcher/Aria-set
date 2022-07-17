@echo off
cd trackerslist
git pull
cd ..
python listreplace.py
start  .\webui-aria2\docs\index.html
aria2c --conf-path=./aria2.conf
