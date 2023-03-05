import math
import time

from requests import post


class YMCHECK1:
    def __init__(self):
        self.url = 'https://www.ename.net/domain/domainAjax'
        self.codeList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't',
                         'u', 'v', 'w', 'x', 'y', 'z']
        self.domain = ''

    def clear(self):
        self.domain = ''

    def getCom(self):
        p.domain += '.com'  # 这里可以加规则，进行筛选，可以筛选后缀和其他规则。

        header = {
            'Origin': 'https://www.ename.net',
            'Referer': 'https://www.ename.net/domain',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        datas = {
            'choseType': '1',
            'domain': p.domain,
            'key': '807a589630ea9ba867cd0f83594b0836',
            'time': '1543559128'
        }
        res = post(self.url, headers=header, data=datas)

        # 返回数据   ====>>>   {"result":{"iwkk.com":{"code":1,"md5":"3b6abbf210e53e5cbfca1c1ed62673f5","domain":"iwkk.com"}},"code":100}

        ress = res.json()
        result = ress.get('result')
        res_code = result.get(self.domain)
        print(ress)
        print(result)
        print(res_code)
        print(res_code.get('code'))


if __name__ == '__main__':
    for i in range(1000):
        p = YMCHECK1()
        # debug
        p.domain = 'a'
        p.getCom()
