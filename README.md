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

```
./nglogparser.py

Main Choice: Choose 1 of 5 choices
Choose 1 for top requested pages
Choose 2 for percentage requests status
Choose 3 for unsuccessful page requests
Choose 4 for top 10 hosts with top 5 pages TODO
Choose 5 to exit
Please make a choice: 1

Here are top requested pages
Webiste http://www.almhuette-raith.at/apache-log/, hits are 42974
Webiste http://www.almhuette-raith.at/, hits are 11258
Webiste http://www.almhuette-raith.at, hits are 9349
Webiste http://almhuette-raith.at/, hits are 4567
Webiste http://www.almhuette-raith.at/index.php?option=com_phocagallery&view=category&id=1&Itemid=53, hits are 3905
Webiste http://www.almhuette-raith.at/administrator/, hits are 2032
Webiste http://www.almhuette-raith.at/apache-log/access.log, hits are 1412
Webiste http://almhuette-raith.at/index.php?option=com_phocagallery&view=category&id=1&Itemid=53, hits are 1152
Webiste http://www.almhuette-raith.at/templates/jp_hotel/css/template.css, hits are 890
Webiste https://www.google.com/, hits are 674
Webiste http://www.almhuette-raith.at/index.php?option=com_phocagallery&view=category&id=4:ferienwohnung2&Itemid=53, hits are 635
Press any key to goto menu

Main Choice: Choose 1 of 5 choices
Choose 1 for top requested pages
Choose 2 for percentage requests status
Choose 3 for unsuccessful page requests
Choose 4 for top 10 hosts with top 5 pages TODO
Choose 5 to exit
Please make a choice: 2

Here's failed and success percentage
Successful req percent is 95.58372236308918
Failed req percent is 4.620323971203937
Press any key to goto menu



Main Choice: Choose 1 of 5 choices
Choose 1 for top requested pages
Choose 2 for percentage requests status
Choose 3 for unsuccessful page requests
Choose 4 for top 10 hosts with top 5 pages TODO
Choose 5 to exit
Please make a choice: 3
Here are the top failed pages

Failed req for url http://www.almhuette-raith.at, hits are 4140
Failed req for url http://www.almhuette-raith.at/, hits are 1255
Failed req for url http://www.almhuette-raith.at/apache-log/access.log, hits are 1175
Failed req for url http://www.almhuette-raith.at/apache-log/, hits are 593
Failed req for url http://almhuette-raith.at/, hits are 465
Failed req for url http://simplesite.com, hits are 455
Failed req for url https://www.google.com/, hits are 252
Failed req for url http://www.almhuette-raith.at/index.php?option=com_phocagallery&view=category&id=1&Itemid=53, hits are 244
Failed req for url http://www.almhuette-raith.at/index.php?option=com_content&view=article&id=49&Itemid=55, hits are 174
Failed req for url https://www.google.com/search, hits are 150
Failed req for url http://www.almhuette-raith.at/index.php?option=com_content&view=article&id=50&Itemid=56, hits are 134
Press any key to goto menu


Main Choice: Choose 1 of 5 choices
Choose 1 for top requested pages
Choose 2 for percentage requests status
Choose 3 for unsuccessful page requests
Choose 4 for top 10 hosts with top 5 pages TODO
Choose 5 to exit
Please make a choice: 5
Exiting!
```
