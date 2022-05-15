import requests

def find_form(form_val):
    if form_val[0].find("name") == 1: form_val = form_val[1]
    else :
        cnt = 0
        while(True):
            if form_val[cnt].find("name") == 1 : 
                form_val = form_val[cnt+1]
                break
            else : cnt += 1
    return form_val

def injection():
    list_file = open("injection_bypass.txt", 'r', encoding='utf-8')

    sql_url = input("SQL Injection 입력 폼이 존재하는 URL 입력 \n입력:")
    temp_address = requests.post(sql_url)
    textbox = temp_address.text.split('<input type="text"')
    textbox = textbox[1].split("\"")
    find_form()
    while(True):
        bypass_injection = list_file.readline()
        if bypass_injection == '' : break
        print(bypass_injection)
        