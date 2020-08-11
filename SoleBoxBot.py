from requet import Requet
import re
from random import randint
from urllib.parse import unquote, quote
import html
import time
from sys import argv as av


class SoleBoxBot:
    def createAccount(self, name: str, surname: str):
        requestAPI = Requet(True, "www.solebox.com", timeout=20)
        result, cookies = requestAPI.requet("/en_FR/registration?rurl=1")
        csrf_token = re.findall(
            "name=\"csrf_token\" value=\"(.*)", result)[0].rstrip("\"/>")
        print(csrf_token)
        js, additionalCookies = requestAPI.requet(
            url="https://www.solebox.com/on/demandware.static/Sites-solebox-Site/-/en_FR/v1596783584181/js/accountNamespace.js",
            method="GET",
            cookies=cookies, body="", headers={
                'Content-Length': '0',
                'Host': 'www.solubox.com',
                'Accept': 'raw',
                'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8,zh-HK;q=0.7,zh-CN;q=0.6,zh-TW;q=0.5',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
            })
        email = name+"."+surname+"@gmail.com"
        payload = "dwfrm_profile_register_title=Herr" + "&dwfrm_profile_register_firstName="+name + "&dwfrm_profile_register_lastName="+surname + "&dwfrm_profile_register_email="+email + "&dwfrm_profile_register_emailConfirm="+email + \
            "&dwfrm_profile_register_password="+email + "&dwfrm_profile_register_passwordConfirm="+email + "&dwfrm_profile_register_phone=" + \
            "&dwfrm_profile_register_birthday=" + \
            "&dwfrm_profile_register_acceptPolicy=true" + "&csrf_token="+csrf_token
        print(requestAPI.requet(url="https://www.solebox.com/on/demandware.store/Sites-solebox-Site/en_FR/Account-SubmitRegistration?rurl=1&format=ajax",
                                method="POST",
                                cookies=additionalCookies,
                                body=payload,
                                headers={
                                    'Content-Length': len(payload),
                                    'Host': 'www.solubox.com',
                                    'Accept': 'raw',
                                    'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8,zh-HK;q=0.7,zh-CN;q=0.6,zh-TW;q=0.5',
                                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                    'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
                                }
                                ))

    def authenticate(self, email: str):
        requestAPI = Requet(True, "www.solebox.com", timeout=20)
        result, cookies = requestAPI.requet("/en_FR/login")
        csrf_token = re.findall(
            "name=\"csrf_token\" value=\"(.*)", result)[0].rstrip("\"/>")
        print(csrf_token)
        js, newCookies = requestAPI.requet(
            url="/on/demandware.static/Sites-solebox-Site/-/en_FR/v1596872710721/js/accountNamespace.js",
            method="GET",
            cookies=cookies, body="", headers={
                'Content-Length': '0',
                'Host': 'www.solubox.com',
                'Accept': 'raw',
                'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8,zh-HK;q=0.7,zh-CN;q=0.6,zh-TW;q=0.5',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            })
        cookies.update(newCookies)
        js, newCookies = requestAPI.requet(
            url="/on/demandware.store/Sites-solebox-Site/en_FR/Page-GetCustomerCountry?format=ajax",
            method="GET",
            cookies=cookies, body="", headers={
                'Content-Length': '0',
                'Host': 'www.solubox.com',
                'Accept': 'raw',
                'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8,zh-HK;q=0.7,zh-CN;q=0.6,zh-TW;q=0.5',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            })
        cookies.update(newCookies)
        payload = "dwfrm_profile_login_password="+email + \
            "&dwfrm_profile_customer_email=" + email + "&csrf_token="+csrf_token
        data, cookies = requestAPI.requet(
            url="/en_FR/authentication?rurl=1&format=ajax",
            method="POST",
            cookies=cookies,
            body=payload,
            headers={
                'Content-Length': len(payload),
                'Host': 'www.solubox.com',
                'Accept': 'raw',
                'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8,zh-HK;q=0.7,zh-CN;q=0.6,zh-TW;q=0.5',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }
        )
        return cookies

    def fetchShoeList(self, cookies: dict):

        requestAPI = Requet(True, "www.solebox.com", timeout=20)
        data, newCookies = requestAPI.requet(
            url="https://www.solebox.com/en_FR/c/footwear",
            method="GET",
            cookies=cookies, body="", headers={
                'Content-Length': '0',
                'Host': 'www.solubox.com',
                'Accept': 'raw',
                'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8,zh-HK;q=0.7,zh-CN;q=0.6,zh-TW;q=0.5',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            })
        links = re.findall(
            "b-product-tile-image-link js-product-tile-link\" href=\"(.*)", data)
        links = [l.rstrip("\">") for l in links]
        print(links)
        cookies.update(newCookies)
        return links, cookies

    def getSizes(self, data):
        data = data.split("\n")
        dump = []
        for i in range(10, len(data)):
            if len(re.findall("b-swatch-value--sold-out", data[i - 7])) > 0 or len(re.findall("b-swatch-value--orderable", data[i - 7])) > 0 or len(re.findall("b-swatch-value--in-store-only", data[i - 7])) > 0:
                for j in range(0, 7):
                    if len(re.findall("(\d)", data[i - j])) > 0 and data[i - j][-1].isdigit():
                        dump.append(data[i - j].lstrip(" "))
                        break
        return dump

    def forgeId(self, sizes, pid, size):
        idx = 0
        for s in sizes:
            if size == s:
                pid += ((7 - (idx > 9)) * '0') + str(idx + 1 + (idx > 1))
            idx += 1
        return pid

    def addShoeToBasket(self, urls, cookies):
        headers = {
            'Content-Length': '0',
            'Host': 'www.solubox.com',
            'Accept': 'raw',
            'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8,zh-HK;q=0.7,zh-CN;q=0.6,zh-TW;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }
        requestAPI = Requet(True, "www.solebox.com", timeout=30)
        data, newCookies = requestAPI.requet(
            url="/on/demandware.static/Sites-solebox-Site/-/en_FR/v1596955988784/js/productNamespace.js", method="GET", cookies=cookies, body="", headers=headers)
        cookies.update(newCookies)
        data, newCookies = requestAPI.requet(
            url=urls[randint(0, len(urls) - 1)], cookies=cookies, body="", headers=headers)
        cookies.update(newCookies)
        sizes = self.getSizes(data)
        options = re.findall("data-href=\"/en_FR/p/(.*)", data)
        sizeOptions = []
        for i in range(1, len(options), 2):
            sizeOptions.append(html.unescape(options[i]))
        ids = [re.findall("(.*).html", Id)[0][len(re.findall("(.*).html", Id)[0]) - 8:]
            for Id in sizeOptions]
        chosenSizeIndex = randint(0, len(ids) - 1) % 4
        data, newCookies = requestAPI.requet(
            url="/en_FR/p/"+sizeOptions[chosenSizeIndex].rstrip("\">")+"&format=ajax", method="GET", cookies=cookies, body="", headers=headers)
        cookies.update(newCookies)
        shoeSize = re.findall("=(.*)", re.findall("=(.*)\"",
                                                sizeOptions[chosenSizeIndex])[0])[0]
        pid = self.forgeId(sizes, ids[chosenSizeIndex],
                    unquote(shoeSize, encoding="ascii"))
        url = "/on/demandware.store/Sites-solebox-Site/en_FR/Product-Extras?format=ajax&pid=" + \
            pid + "&format=ajax"
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
        headers["Accept-Encoding"] = "gzip deflate"
        requestAPI.timeout = 40
        data, newCookies = requestAPI.requet(url=url, method="GET",
                                        cookies=cookies, body="", headers=headers)
        cookies.update(newCookies)
        body = "pid="+pid+"&options="+quote("([{\")")+"optionId"+quote("\":\"")+"212"+quote("\"),\"")+"selectedValueId"+quote("\":\"") + \
            shoeSize+quote("\"}]")+"&quantity=1"
        headers["Content-Length"] = str(len(body))
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        time.sleep(10)
        requestAPI.requet(url="/en_FR/add-product?format=ajax",
                                method="POST", cookies=cookies, headers=headers, body=body)

    def run(self, name: str, surname: str, create: bool):
        try:
            if (create):
              self.createAccount(name, surname)
            c = self.authenticate(name + "."+ surname + "@gmail.com")
            l, c = self.fetchShoeList(c)
            self.addShoeToBasket(l, c)
        except:
            print("Something went wrong error")
            exit(1)
    
s = SoleBoxBot()
if len(av) <= 2:
    print("usage: python3 SoleBoxBot.py name surname [-c]")
    exit(1)
    
if "-c" in av:
    s.run(av[1], av[2], True)
else:
    s.run(av[1], av[2], False)
