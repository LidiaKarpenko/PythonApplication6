from random import *
def lugemine(f:str,l:list):
    """info logins f listisse l
    """
    fail=open(f,"r") #,encloding="utf-8-sig"
    for rida in fail:
        l.append(rida.strip()) #"\n"
    fail.close()
    return l
def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def uus_sõna(f:str,rida:str) -> list:
    """:param str file: Faili nimetus
       :param str x: lisatav sõna
    """
    l=[]
    with open(f,"a",encoding=utf-8-sig
