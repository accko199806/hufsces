import os

IP_ADDR = "192.168.1.210"

db_host = IP_ADDR
db_name = 'iot'
db_user = 'acckolee'
db_password = '9806'

def setHost(host):
    global db_host
    db_host = host
