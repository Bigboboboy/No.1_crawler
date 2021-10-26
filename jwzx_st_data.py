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
                    "Cookie": "_gscu_1026695571=63867326hevvfa19; vvjcgVbcZbczS=5UjfqIslYF54LY2N3mTP12hqnwTcLh_75PXs03OrqkK69fmXrrwLXt73XW7tfe_PZr6tDnzxgeG0UVVMYuLsU0q; mLvnBZTNP4mtS=5THlPEuRJEVOYGDGNgH2M7jIfkctzEaws8p5RH3qXzQFtIpbX2dyXUPQBmCM9.x9SpjZOw8xwt8HLOOgZqp0R6A; PHPSESSID=ST-699551-L5Y--FdS4sDBz1Ur1C0oObPpdKYauthserver2; mLvnBZTNP4mtT=53UIs1Dm606LqqqmZBrh8KqyYiuao1EkETNJyUS0QYvboDp6mhzYL.5otXw8YjF8jPAfSF9RzlP2YuJf2dFS3WuHrUpm2CBOWxmk_vbO0imB0wVd__SWVE39h.CSTQmY2S2COEaUN1X.uT7p0ADIxSMD7tfGcYFFvixDZ_E6l2jdC5KJiCZALC3a5r6s.IexfghZahKZKglqkyBvOtyd3wWcKrAF9xrDtIPLmCDi1TTngY_1id7wmex_ihKVvmkCEUJgrbiCFnjc1bzckv_gT5ZAcrC4pC0s8SVm5QxbVP9QW1uUGeUWid1024EOljOkFqLUyxpiOzE6vvZvDcVUBdg"
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
        FILE.write(str(stu) + '\n')


if __name__ == '__main__':
    url = "http://jwc.cqupt.edu.cn/kebiao/kb_stuList.php?jxb=A00211A1040110001"
    html = get_main_page(url)
    if not os.path.exists("../data"):
        os.mkdir("../data")
    try:
        FILE = open("../data/jwzx_st_data.txt", 'w', encoding='utf-8')
    except Exception as e:
        print(e)
        exit(-1)
    parse_main_page(html)
    FILE.close()
