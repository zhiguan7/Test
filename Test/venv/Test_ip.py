#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 9:25
# @Author  : Wind
# @File    : Test_ip.py
# @Software: PyCharm


import json
import sys
import time

import requests
import re
import random

class GetIP(object):
    IPS = []
    url_list = ['http://www.xicidaili.com/nn/',
                'http://www.xicidaili.com/nn/2',
                'http://www.xicidaili.com/nn/3', ]
    UA_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36"
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER"
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36"
    ]

    def _get_random_header(self):
        headers = {
            'User-Agent': random.choice(self.UA_list),
            'Upgrade-Insecure-Requests': '1',
        }
        return headers

    def _get_ip_list(self):
        for url in self.url_list:
            res = requests.get(url=url, headers=self._get_random_header())
            sel = Selector(response=res)
            ip_list = sel.css('#ip_list tr')
            for i in range(1, len(ip_list)):
                try:
                    ip = {'ip_addr': ip_list[i].css('td:nth-child(2) ::text').extract_first(),
                          'ip_port': ip_list[i].css('td:nth-child(3) ::text').extract_first(),
                          'server_addr': ip_list[i].css('td:nth-child(4) > a ::text').extract_first(),
                          'anonymous': ip_list[i].css('td:nth-child(5) ::text').extract_first(),
                          'http_type': ip_list[i].css('td:nth-child(6) ::text').extract_first(),
                          'speed': float(re.findall(r'([\d\.]+)',
                                                    ip_list[i].css(
                                                        'td:nth-child(7) > div ::attr(title)').extract_first())[
                                             0]),
                          'conn_time': float(re.findall(r'([\d\.]+)',
                                                        ip_list[i].css(
                                                            'td:nth-child(8) > div ::attr(title)').extract_first())[0]),
                          'validate_time': "20" + ip_list[i].css('td:nth-child(10) ::text').extract_first() + ":00"}
                    alive_time = ip_list[i].css('td:nth-child(9) ::text').extract_first()
                    time = re.findall(r'([\d]+)', alive_time)[0]
                    if '天' in alive_time:
                        ip['alive_time'] = int(time) * 1440
                    elif '小时' in alive_time:
                        ip['alive_time'] = int(time) * 60
                    else:
                        ip['alive_time'] = int(time)
                    self.IPS.append(ip)
                except IndexError as e:
                    print(e)
                    pass

    def test_ip(self, ip_addr, ip_port, http_type, test_url='https://ip.cn/index.php', time_out=10):
        try:
            local_proxy = {
                str(http_type): str(http_type + '://' + ip_addr + ':' + ip_port)
            }
            params = {
                'ip': str(ip_addr + ':' + ip_port)
            }
            res = requests.get(url=test_url, params=params, proxies=local_proxy, headers=self._get_random_header(),
                               timeout=time_out)
            sel = Selector(res)
            print(str(res.status_code) + '/'.join(sel.css('#result > div ::text').extract()))
            return True
        except requests.exceptions.ProxyError as e:
            print('连接次数达上限！')
            return False
        except requests.exceptions.Timeout as e:
            print('连接超时！')
            return False
        except requests.exceptions.ConnectionError as e:
            print('连接失败！')
            return False

    def test_ip_and_get(self):
        self._get_ip_list()
        ips_active = []
        for i in range(0, len(self.IPS) - 290):
            import time
            time.sleep(1)
            if float(self.IPS[i]['speed']) > 1 or float(self.IPS[i]['conn_time']) > 1 or float(self.IPS[i][
                                                                                                   'alive_time']) < 60:
                print(self.IPS[i]['ip_addr'] + ':不符合要求!')
                continue
            print('test ip {0}'.format(i) + ': ' + self.IPS[i]['ip_addr'] + ':' + self.IPS[i]['ip_port'])
            result = self.test_ip(self.IPS[i]['ip_addr'], self.IPS[i]['ip_port'], self.IPS[i]['http_type'].lower())
            if result:
                j = json.dumps(str(self.IPS[i]))
                ips_active.append(j)
        # with open("active_ips.txt", "a") as f:
        #     f.writelines(ips_active)
        return ips_active

    # def test_ip_and_delect(self, ip_list):
    #     ips_active = []
    #     for i in range(0, len(ip_list)):
    #         import time
    #         time.sleep(1)
    #         print('test ip {0}'.format(i) + ': ' + self.IPS[i]['ip_addr'] + ':' + self.IPS[i]['ip_port'])
    #         result = self.test_ip(ip_list[i]['ip_addr'], ip_list[i]['ip_port'], ip_list[i]['http_type'].lower(), 60)
    #         if result:
    #             continue
    #         else:
    #             del_sql = 'delect from ip_table where ip_addr="{0}" and ip_port="{1}" and http_type="{2}"'.format(
    #                 ip_list[i]['ip_addr'], ip_list[i]['ip_port'], ip_list[i]['http_type'])
    #             mysql.delete(del_sql)


if __name__ == "__main__":
    ip = GetIP()
    active_ip_list = ip.test_ip_and_get()
    mysql = MyPymysqlPool("notdbMysql")
    for ip in active_ip_list:
        j = eval(json.loads(ip))
        query_sql = 'select count(*) from ip_table where ip_addr="{0}" and ip_port="{1}" and http_type="{2}"'.format(
            j['ip_addr'], j['ip_port'], j['http_type'])
        result = mysql.getAll(query_sql)
        if result[0]['count(*)'] != 0:
            continue
        else:
            insert_sql = "insert into ip_table (ip_addr, ip_port, server_addr, anonymous, http_type, speed,conn_time, " \
                         "alive_time, validate_time) " \
                         "value ('{0}', '{1}', '{2}', '{3}', '{4}', {5}, {6}, {7}, '{8}')".format(j['ip_addr'],
                                                                                                  j['ip_port']
                                                                                                  , j['server_addr'],
                                                                                                  j['anonymous'],
                                                                                                  j['http_type'],
                                                                                                  j['speed'],
                                                                                                  j['conn_time']
                                                                                                  , j['alive_time'],
                                                                                                  j['validate_time'])
            result = mysql.insert(insert_sql)

    # time.sleep(1000)
    # sqlAll = "select * from ip_table;"
    # result = mysql.getAll(sqlAll)
    # ip.test_ip_and_delect(result)
    mysql.dispose()
