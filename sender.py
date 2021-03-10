import requests
from pyzabbix import ZabbixMetric, ZabbixSender


def main():

    url = 'http://web:5000/metrics'
    response = requests.get(url)
    metric = response.text.split()[-1]
    forsend = []
    m = ZabbixMetric('DevTest', 'Metric', metric)
    forsend.append(m)
    zbx = ZabbixSender('zabbix-server')
    zbx.send(forsend)


if __name__ == '__main__':
    main()
