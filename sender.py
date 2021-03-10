import requests
from pyzabbix import ZabbixMetric, ZabbixSender
import time

def main():
    while True:
        visit = open("/code/visit", "r").read()
        url = 'http://web:5000/metrics'
        response = requests.get(url)
        metric = response.text.split()[-1]
        amount = int(metric) - int(visit)
        forsend = []
        m = ZabbixMetric('DevTest', 'Metric', amount)
        forsend.append(m)
        zbx = ZabbixSender('zabbix-server')
        zbx.send(forsend)
        refresh_visit = open("/code/visit", "w")
        refresh_visit.write(metric)
        refresh_visit.close()
        time.sleep(1)


if __name__ == '__main__':
    main()
