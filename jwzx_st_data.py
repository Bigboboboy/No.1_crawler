import requests
from pyquery import PyQuery as pq
import os

FILE = None

def get_main_page(url):
    headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Cache-Control": "max-age=0",
                    "Connection": "keep-alive",
                    "Host": "jwc.cqupt.edu.cn",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
                    "Referer": "http://jwc.cqupt.edu.cn/kebiao/kb_stu.php?xh=2018211781",
                    "Upgrade-Insecure-Requests": "1",
                    "Cookie":"_gscu_1026695571=63867326hevvfa19; vvjcgVbcZbczS=5UjfqIslYF54LY2N3mTP12hqnwTcLh_75PXs03OrqkK69fmXrrwLXt73XW7tfe_PZr6tDnzxgeG0UVVMYuLsU0q; mLvnBZTNP4mtS=5THlPEuRJEVOYGDGNgH2M7jIfkctzEaws8p5RH3qXzQFtIpbX2dyXUPQBmCM9.x9SpjZOw8xwt8HLOOgZqp0R6A; PHPSESSID=ST-146435-JmtamC07Flad3McwBQINQgE6dG0authserver2; mLvnBZTNP4mtT=53U000DmeJAlqqqmZ01ry_AV3H6IEQ.Z8Ww4x5KCmcifqwqj1PP_DIcSVcVh0JC3vubBn2iIPs3B4.3HzoCtEN9FD.a5T1MSJ7hYspWPAk5uM8cDb3zHwfbuc3Tn0uzbUM1Al5SsVQJUY0.VxIePhZXthDvJ4y1u0k_LQrpLRADqDw_smSlPRZWIuE8Hsw6gg7s9VAOzOTcbJqTgziHAnQEfimZqkDKSbsT425JlzcPrpWmixtekbt6aOAQ0pdU.Br.zdCZG98l19mGFmWTdW7gvhl.v023ZBFcwSaE7Ixdo52xZF7EZl.uqHJT1oQodDpXVUkt2OP7ul0X6PKojMnc"
    }
    r = requests.get(url, headers=headers)
    print(r.status_code)
    if r.status_code == 200:
        return r.text   #str类型
    return None


def parse_main_page(html):
    d = pq(html)
    
    items = d("div#stuListTabs-current table tbody tr")
    for idx, item in enumerate(items.items()):
        detail = item.find("td").text()
        detail = detail.split(' ')
        stu = {
            'No': detail[0],
            '学号': detail[1],
            '姓名': detail[2],
            '性别': detail[3],
            '班级': detail[4],
            '专业号': detail[5],
            '专业名': detail[6],
            '学院': detail[7],
            '年级': detail[8],
            '学籍状态': detail[9],
            '选课状态': detail[10],
            '课程类别': detail[11],
        }
        yield stu


def sav_to_file(data):
    if not os.path.exists("./data"):
        '''一个点退一级父目录'''
        os.mkdir("./data")
    with open("./data/jwzx_st_data.txt", 'a', encoding='utf-8') as f:
        f.write(str(data) + '\n')


if __name__ == '__main__':
    class_id = 'A04211A2040580001'
    url = f"http://jwc.cqupt.edu.cn/kebiao/kb_stuList.php?jxb={class_id}"
    html = get_main_page(url)
    for i in parse_main_page(html):
        sav_to_file(i)
