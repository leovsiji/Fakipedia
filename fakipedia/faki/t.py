import textwrap as tw

with open("Nuclear power.txt","r",encoding='utf-8-sig')as f:
    raw = f.read()

clean = tw.fill(raw,width=70)

with open("Nuclear power.txt","w",encoding='utf-8-sig')as f:
    f.write(clean) 