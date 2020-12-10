from ipwhois import IPWhois
from pprint import pprint
import socket
import json
from googlesearch import search
import sublist3r
from pyhunter import PyHunter


def get_ip(hostname):
    try:
        getting_ip = socket.gethostbyname(hostname)
        return getting_ip

    except:
        return "Не удалось получить IP"


def information_receipt():
    try:
        obj_host = IPWhois(host)
        result = obj_host.lookup_rdap(depth=10)
        return result
    except:
        return "Не удалось получить информаци об IP"


def dork(input_text):
    try:
        urls = []
        dork_text = "filetype:" \
                    "(doc | pdf | xls | txt | ps | rtf | odt |" \
                    " sxw | psw | ppt | pps | xml) " \
                    "site:" + input_text
        for url in search(dork_text):
            urls.append(url)
        return urls
    except:
        return "Не удалось сделать Dork запрос"


def get_subdomains(input_domain):
    try:
        subdomains = sublist3r.main(input_domain, 40,
                                    'subdomains.txt',
                                    ports=None,
                                    silent=False,
                                    verbose=False,
                                    enable_bruteforce=False,
                                    engines=None)
        return subdomains
    except:
        return "Не удалось получить Субдомены"


def hunter_emails_and_info(input_domain):
    try:
        hunter = PyHunter('f697810b67d3c3e059c172dabc02cb94e724f4ec')
        hunter_json = hunter.domain_search(input_domain, emails_type='personal')
        return hunter_json
    except:
        return "Не удалось получить информацию о пользователях"


def write_to_file():
    data = {
        'Host': host,
        'Dork_Request': dorking,
        'Sub_Domains': subdomains,
        'Users_Info': hunter,
        'Ip_info': info
    }
    with open('Scanner.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    host_entered_by_the_user = input("Введите хост (Например vk.com): ")
    host = get_ip(str(host_entered_by_the_user))
    dorking = dork(str(host_entered_by_the_user))
    subdomains = get_subdomains(str(host_entered_by_the_user))
    hunter = hunter_emails_and_info(str(host_entered_by_the_user))
    info = information_receipt()
    write_to_file()
