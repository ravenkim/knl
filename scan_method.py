import requests

def scan_method():
    scan_url = input("사용 method 확인 URL :")
    res_head = requests.head(scan_url)
    res_get = requests.get(scan_url)
    res_post = requests.post(scan_url)
    res_option = requests.options(scan_url)
    res_put = requests.put(scan_url)
    res_delete = requests.delete(scan_url)

    print("\n 사용중인 메소드\n")
    if res_head.status_code == 200 : print("HEAD")
    else : print("응답코드",res_head.status_code," HEAD 미사용")
    if res_get.status_code == 200 : print("GET")
    else : print("응답코드 ",res_head.status_code," GET 미사용")
    if res_post.status_code == 200 : print("POST")
    else : print("응답코드 ",res_head.status_code," POST 미사용")
    if res_option.status_code == 200 : 
        print("OPTION")
        print("header 정보\n",res_option.headers)
    else : print("응답코드 ",res_head.status_code," OPTION 미사용")
    if res_put.status_code == 200 : print("PUT")
    else : print("응답코드 ",res_head.status_code," PUT 미사용")
    if res_delete.status_code == 200 : print("DELETE")
    else : print("응답코드 ",res_head.status_code," DELETE 미사용")