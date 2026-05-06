from bs4 import BeautifulSoup as b
import requests as r
import random


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
    "  ⋆∇i     ≤♦♦♦√ .♦♦♦♫             mm             ##                               mm     ##",                   
    "          ≤♦♦♦√ .♦♦♦♫             ##                                             ##        ",                   
    "          ≤♦♦♦√ .♦♦♦♫    m#####m  ##  ##      ####     ##m###m    m####m    m###m##   ####   m#####m",                   
    '          ≤♦♦♦√ .♦♦♦♫      mmm##  ##m##        ##     ##"  "##  ##mmmm##  ##"  "##     ##      mmm##',                   
    '          ≤♦♦♦√ .♦♦♦♫   m##"""##  ##"##m      ##     ##    ##  ##""""""  ##    ##     ##    m##"""##',                   
    '          ≤♦♦♦√ .♦♦♦♫   ##mmm###  ## "#m  mmm##mmm  ###mm##"  "##mmmm#  "##mm###  mmm##mmm  ##mmm###',                   
    '          ≤♦♦♦≥ -♦♦♦♦   """" ""  ""   """  """"""""## """      """""     """ ""  """"""""   """" ""',                   
    "          ≤♦♦◦..•♦♦◦l                             ##  ",                   
    " Il.      ∂♦•;+◦♦♦≥",                     
    "♦♦♦♦♦⋆+  +♦√-•♦⋆÷",                       
    "♦♦♦♦♦♦♦♦♦♦°√>.",                          
    "  i±∂∫-: "                          
    "                                                    ",
    "                        online(wiki extraction) - /on         exit - /e"                                        
                                        
    ]
    print()
    for i in F:
        print(i)
    print()
    banner.dec = input("input:- ")
    print()
banner()
dd = banner.dec
def extract():
    def he(rw):
        y =[]
        j =rw.split(r"/")
        for i in range(len(j)):
            if "_" in j[4]:
                h = j[4].split("_")
                print()
                print("---",*h,"---")
                break
            elif "_" not in j[4]:
                print()
                print(f"--- {j[4]} ---")
                break


    url = input("LINK:- ")

    he(url)

    headers = {'user-agent':random.choice(h)}
    re = r.get(url,headers=headers)
    s = b(re.text,'html.parser')
    string = ''
    for p in s.find_all('p'):
        string += p.text + '\n'
        for i in range(500):
            string = string.replace(f'[{i}]', '')
    print(string)

if dd == "/on":
   extract()
elif dd == "/e":
    exit()
else:
    banner()
    

 
