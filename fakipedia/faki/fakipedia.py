from bs4 import BeautifulSoup as b
import requests as r
import random
import textwrap as tw
import sqlite3 as sq


def beyond():
    h = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15']

    def banner():
        F = [
                                                    
        "              +•♦◦°∫-:i-∫∏,",   
        "            .≥♦♦♦♦♦♦♦♦♦♦♦♦l",        
        "          I≈∑∫∇◦♦♦♦♦♦°◦♦♦♦♦♦•-.",         
        "          ≤♦♦♦√ .♦♦♦♫±",
        "          ≤♦♦♦√ .♦♦♦♦≠::::::",            
        "    -♦♦♦♦♦♦♦♦♦√ .♦♦♦♦♦♦♦♦♦♦>",            
        "  I♦♦♦♦♦♦♦♦♦♦♦√ .♦♦♦♦♦♦♦♦♦∇",             
        "  ⋆∇i     ≤♦♦♦√ .♦♦♦♫              mm        ##                               mm     ##",                   
        "          ≤♦♦♦√ .♦♦♦♫             ##                                         ##        ",                   
        "          ≤♦♦♦√ .♦ m#####m  ##  ##      ####     ##m###m    m####m    m###m##   ####   m#####m",                   
        '          ≤♦♦♦√ .♦♦  mmm##  ##m##        ##     ##"  "##  ##mmmm##  ##"  "##     ##      mmm##',                   
        '          ≤♦♦♦√ . m##"""##  ##"##m      ##     ##    ##  ##""""""  ##    ##     ##    m##"""##',                   
        '          ≤♦♦♦√ . ##mmm###  ## "#m  mmm##mmm  ###mm##"  "##mmmm#  "##mm###  mmm##mmm  ##mmm###',                   
        '          ≤♦♦♦≥ -♦ """" ""  ""   "" """""""  ## """      """""     """"""  """"""""   """""""',                   
        "          ≤♦♦◦..•♦♦◦l                        ##  ",                   
        " Il.      ∂♦•;+◦♦♦≥",                     
        "♦♦♦♦♦⋆+  +♦√-•♦⋆÷",                       
        "♦♦♦♦♦♦♦♦♦♦°√>.",                          
        "  i±∂∫-: "                          
        "                                                    ",
        "                        online(wiki extraction) - /on    offline storage - /of  ",
        "                        exit - /e                                               ",                                        
                                            
        ]
        print()
        for i in F:
            print(i)
        print()


    con = sq.connect('lib.db')
    c = con.cursor()
    c.execute(""" 
CREATE TABLE IF NOT EXISTS wikidata(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              heading TEXT,
              content TEXT 
              )
""")

    def extract():
        file_name = " "
        def he(rw):
            y =[]
            j =rw.split(r"/")
            for i in range(len(j)):
                if "_" in j[4]:
                    h = j[4].split("_")
                    hed = " ".join(h)
                    print()
                    print("---",hed,"---")
                    break
                elif "_" not in j[4]:
                    hed = j[4]
                    print()
                    print(f"--- {hed} ---")
                    break
            c.execute("INSERT INTO wikidata (heading) VALUES(?)",(hed,))


        url = input("LINK:- ")
        if url in "/e":
            print("さよなら")
            exit()
        else:
            y =[]
            j =url.split(r"/")
            for i in range(len(j)):
                if "_" in j[4]:
                    hr = j[4].split("_")
                    hed = " ".join(hr)
                    print()
                    print("---",hed,"---")
                    break
                elif "_" not in j[4]:
                    hed = j[4]
                    print()
                    print(f"--- {hed} ---")
                    break
            c.execute("INSERT INTO wikidata (heading) VALUES(?)",(hed,))
            
        
        headers = {'user-agent':random.choice(h)}
        re = r.get(url,headers=headers)
        s = b(re.text,'html.parser')
        string = ''
        for p in s.find_all('p'):
            string += p.text + '\n'
            for i in range(500):
                string = string.replace(f'[{i}]', '')
        #print(string)
        clean = tw.fill(string,width=100)
        print(clean)
        aid = c.lastrowid
        with open("temp.txt","a",encoding='utf-8-sig')as f:
            f.write('\n'+clean)
        with open("temp.txt","r+",encoding='utf-8-sig')as f:
            st = f.read()
            c.execute("UPDATE wikidata SET content =? WHERE id =?",(st,aid))
            con.commit()
            f.truncate(0)
        
    def off(ofin):
        c.execute("SELECT COUNT(*) FROM wikidata")
        lel = c.fetchone()[0]
        if "/help" in ofin:
            print("""
/li - lists the topics available in offline library syntax - /li 
/fi - find the topics in library syntax - /fi topic
/e - exit syntax - /e
/del - delete offline library /del topic - delete the topic from the library 
""")    
            
        elif "/li" in ofin:
            if lel == 0:
                print("library is empty")
            elif lel > 0 : 
                c.execute("select heading FROM wikidata")
                rows = c.fetchall()
                print()
                for i, row in enumerate(rows, start=1):
                    print(f"{i} - {row[0]} ")
            
        elif "/fi " in ofin:
            re = ofin.split(" ")
            del re[0]
            rem = " ".join(re).capitalize()
            c.execute("select * FROM wikidata WHERE heading = ?",(rem,))
            rows = c.fetchall()
            for row in rows:
                print()
                print(f"--- {row[1]} ---")
                print(row[2])
        elif "/del" in ofin:
            de = ofin.split(" ")
            if lel == 0:
                print("library is empty")
            elif lel > 0:
                if len(de) == 1:
                    dis = input(f"confirm delete all content by typing y to exit n --> ")
                    if dis == "y":
                        c.execute("DELETE FROM wikidata")
                        con.commit()
                        print("library deleted")
                    else:
                        print("さよなら")
                        exit()
                else:
                    del de[0]
                    dell = " ".join(de).capitalize()
                    dis = input(f"confirm delete of {dell} by typing y to exit n --> ")
                    if dis == "y":
                        c.execute("DELETE FROM wikidata WHERE heading = ?",(dell,))
                        con.commit()
                        print(f"{dell} deleted")
                    else:
                        print("さよなら")
                        exit()    

    banner()
    while True:
        print()
        dec = input("input:- ")
        if dec in "/e,e,E":
            print("さよなら")
            exit()
        elif dec == "/on":
            while True:
                print()
                extract()
        elif dec == "/of":
            while True:
                print()
                ofin = input("図書館:- ")
                if ofin in "/e,e,E":
                    print()
                    print("さよなら")
                    exit()
                else:
                    off(ofin)
                    
            
    con.close()
beyond()
    
        
       

 
