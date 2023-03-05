import math
import time

from requests import post


class YMCHECK:
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
        try:
            res = post(self.url, headers=header, data=datas)

        except:
            return -100
        else:
            # 返回数据   ====>>>   {"result":{"iwkk.com":{"code":1,"md5":"3b6abbf210e53e5cbfca1c1ed62673f5","domain":"iwkk.com"}},"code":100}
            try:
                ress = res.json()
                result = ress.get('result')
                res_code = result.get(self.domain)
                code = res_code.get('code')

            except:
                return -100
            else:
                return code


if __name__ == '__main__':

    p = YMCHECK()
    # debug
    # p.domain = 'quanyu'
    # a = p.getCom()
    # print(a)

    length = 4
    codeList = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    full = 1
    collections = []
    for i in range(length):
        full *= 27
    start_time = time.time()
    for i in range(1, full - 1):  # i为某一位
        if i % 10 == 0:
            # anti-
            p.domain = 'quanyus'
            a = p.getCom()
            while a == -100:
                print("connect failed, trying to reconnect")
                p.domain = 'quanyus'
                a = p.getCom()
            if a != 0:
                print("error occur!  ")
                print("code = " + str(a))

            end_time = time.time()
            disp = "cur: " + str(i) + "   /total: " + str(full) + "   time used: " + str(end_time - start_time) + "s"
            print(disp)
        p.clear()
        cur = i
        for j in range(0, length):
            p.domain += codeList[cur % len(codeList)]
            cur //= len(codeList)
        a = p.getCom()
        while a == -100:
            print("connect failed, trying to reconnect")
            p.domain = p.domain[:-4]
            a = p.getCom()
        if a == 0:
            collections.append(p.domain)
            disp = "find treasure!   " + p.domain
            print(disp)
            f = open("k.txt", "w")
            f.write('\n'.join(collections))
