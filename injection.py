import requests

def injection():
    list_file = open("injection_bypass.txt", 'r', encoding='utf-8')
    while(True):
        bypass_injection = list_file.readline()
        if bypass_injection == '' : break
        print(bypass_injection)
        