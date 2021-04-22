#!/usr/bin/env python3.8
## __author__ : Vinayak Bhatt
## __type__: python3 code to parse an nginx log file, make it a csv,
## put it in a in a sqlite3 DB, no external deps.
import os,sys
import re
import csv
import sqlite3
import socket
import urllib.request

def get_log_file():
    socket.setdefaulttimeout(15)
    try:
        url = 'http://www.almhuette-raith.at/apache-log/access.log'
        urllib.request.urlretrieve(url, 'access.log.txt')
    except Exception as cannotDownload:
        print("Was unable to download log file, download manually to access.log.txt in code dir")
        input("Press any key to continue once the above step is done!")

def logs_to_csv():
    pattern = re.compile(r'([(\d\.)]+) - - \[(.*?)\] "(GET|POST|PUT|PATCH|DELETE)(.*?)" (\d+) (\d+) "(.*)" "(.*?)" "(.*?)"')
    with open("access.log.txt") as fhand:
        with open("nginxlogs.csv","w") as out:
                csv_out=csv.writer(out)
                for line in fhand:
                    m = pattern.search(line)
                    if m:
                        result = (m.groups())
                        csv_out.writerow(result)

def upload_to_sqlite():
    try:
        put_header = ''' sed -i '1 i\ipaddr,datentime,req,path,statuscode,size,url,useragent  nginxlogs.csv' '''
        os.system(put_header)
        import_csv = """sqlite3 database.db <<< ".mode csv ; .import nginxlogs.csv nglogs" """
        os.system(import_csv)

    except Exception as cant_make_db:
        print("Run this manually")
        print("sed -i '1 i\ipaddr,datentime,req,path,statuscode,size,url,useragent  nginxlogs.csv'")
        print('''sqlite3 database.db <<< ".mode csv ; .import nginxlogs.csv nglogs''')
        input("After running above command manually, Press any key to continue")

def top_req_pages():
    count = 0
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("select url, count(*) from nglogs GROUP BY url ORDER BY count(*) DESC limit 20")
    for var in (cursor.fetchall()):
        #count = while count <= 10:
            if var[0].startswith("http") and count <=10:
                #print(var[0])
                print(f"Webiste {var[0]}, hits are {var[1]}")
                count += 1
    cursor.close()

def success_and_fails():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute('''select count (statuscode)  from nglogs where statuscode like "3%" ''')
        success3 = cursor.fetchall()
        cursor.execute('''select count (statuscode)  from nglogs where statuscode like "2%" ''')
        success2 = cursor.fetchall()
        cursor.execute(''' select count(statuscode)  from nglogs ''')
        all_count = cursor.fetchall()
        total_success =  (int(success3[0][0]) +  int(success2[0][0]))
        all_count = int(all_count[0][0])
        print(f"Successful req percent is {total_success/all_count*100} ")
        print(f"Failed req percent is {((all_count-total_success)/total_success)*100}")
        cursor.close()
        #print(all_count)

def top_failed_pages():
    # select url, count(*) from nglogs WHERE statuscode like "4%" OR statuscode like "1%" OR statuscode like "5%" GROUP BY url ORDER BY count(*) DESC limit 20;
    count = 0
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(''' select url, count(*) from nglogs WHERE statuscode like "4%" OR statuscode like "1%" OR statuscode like "5%" GROUP BY url ORDER BY count(*) DESC limit 20;''')
    for var in (cursor.fetchall()):
        #count = while count <= 10:
            if var[0].startswith("http") and count <=10:
                #print(var[0])
                print(f"Failed req for url {var[0]}, hits are {var[1]}")
                count += 1
    cursor.close()

def top_ips():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(''' select ipaddr, count(*) from nglogs GROUP BY ipaddr ORDER BY count(*) DESC limit 10; ''')
    for var in (cursor.fetchall()):
        print(f"The IP {var[0]} makes {var[1]} requests")


def main():

    while True:
        os.system('clear')
        print("Main Choice: Choose 1 of 5 choices")
        print("Choose 1 for top requested pages")
        print("Choose 2 for percentage requests status")
        print("Choose 3 for unsuccessful page requests")
        print("Choose 4 for top 10 hosts with top 5 pages TODO")
        print("Choose 5 to exit")

        choice = input ("Please make a choice: ")

        if choice == "5":
            print("Exiting!")
            sys.exit()
            second_menu()
        elif choice == "4":
            print("TODO")
            sys.exit()
        elif choice == "3":
            os.system('clear')
            print("Here are the top failed pages \n")
            top_failed_pages()
            input("Press any key to goto menu")
        elif choice == "2":
            os.system('clear')
            print("Here's failed and success percentage")
            success_and_fails()
            input("Press any key to goto menu")

        elif choice == "1":
            os.system('clear')
            print("Here are top requested pages")
            top_req_pages()
            input("Press any key to goto menu")
        else:
            print("I don't understand your choice.")
            os.system('clear')



    #get_log_file()
    #logs_to_csv()
    #upload_to_sqlite()
    #top_req_pages()
    #success_and_fails()
    #top_failed_pages()
    #top_ips()






if __name__ == '__main__':
    main()


# sqlite commands
# sqlite3 sqlite3 vbtest2.db
# sqlite> .mode csv
#         .import nginx-logs.csv vblogs
#
# sqlite> select url, count(*)
#   ...> from vblogs
#   ...> GROUP BY url
#   ...> ORDER BY count(*) DESC
#   ...> limit 20;
#'''

#con = sqlite3.connect("nginxlatest.db")
#cur = con.cursor()
#cur.execute("DROP TABLE IF EXISTS vblogs;");
#cur.execute("""
#    CREATE TABLE "vblogs" (
#        "ipaddr_1" TEXT
#        "req_type_1" TEXT
#        "status_code_1" REAL
#        "size_1" REAL
#        "req_url_1" TEXT
#        "user_agent_1" TEXT
#    ); """)
