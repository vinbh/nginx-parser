# nginx-parser
This is a repo for parsing nginx log files. Written in python.

# Getting started
The parser fetches access logs from a url and downloads them using inbuilt urllib module.
Then it uses a simple regex to convert that fiel to csv, the csv is then imported to 
sqliteDB where queries are run on it programatically using python or using 
sqlite3 shell.

## After cloning
1. chmod +x nginxlogs.csv
2. ./nginxlogs.csv

