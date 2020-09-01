import paho.mqtt.client as mqtt
import time
from datetime import datetime
import os
import re
import psutil

import mqconfig

MQ_HOST = mqconfig.mq_host
MQ_TITLE = mqconfig.mq_title

count = 0

def on_connect(client, userdata, flags, rc):
    print("Connect result: {}".format(mqtt.connack_string(rc)))
    client.connected_flag = True


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed with QoS: {}".format(granted_qos[0]))


def on_message(client, userdata, msg):
    global count
    count += 1
    payload_string = msg.payload.decode('utf-8')
    print("{:d} Topic: {}. Payload: {}".format(count, msg.topic, payload_string))


def pubTempData(client, freq=10, limit=100):
    sum_temp = 0.0
    sum_cpuuse = 0.0
    sum_memuse = 0.0
    delta = 1 / freq

    for i in range(limit * freq):
        ti = datetime.now()
        temp = os.popen("vcgencmd measure_temp").readline()

        cpu_temp = re.findall(r'\d+\.\d+', temp.rstrip())[0]
        cpu_used = psutil.cpu_percent(interval=None, percpu=False)
        memory_total = psutil.virtual_memory().total / 1048576  # MB
        memory_used = psutil.virtual_memory().used / 1048576  # MB

        sum_temp += float(cpu_temp)
        sum_cpuuse += float(cpu_used)
        sum_memuse += float(memory_used)

        date = ti.strftime("%Y-%m-%d %H:%M:%S.%f")

        row = "{:s},{:s},{},{:.1f},{:.1f}" \
            .format(date, cpu_temp, cpu_used, memory_total, memory_used)

        client.publish(MQ_TITLE, payload=row, qos=1)
        if i % freq == 0:
            str_temp = '{:.1f}'.format((sum_temp / 10))
            str_cpuuse = '{:.1f}'.format((sum_cpuuse / 10))
            str_memtotal = '{:.1f}'.format(float(memory_total))
            str_memuse = '{:.1f}'.format((sum_memuse / 10))
            str_time = '{:s}'.format(date)

            row2 = '%s,%s,%s,%s,%s' %(str_time, str_temp, str_cpuuse, str_memtotal, str_memuse)
            print(i, row2)

            sum_temp = 0.0
            sum_cpuuse = 0.0
            sum_memuse = 0.0

        time.sleep(delta)


if __name__ == "__main__":
    print("get client")
    client = mqtt.Client("CPU_TEMP_PUB01")
    client.username_pw_set(mqconfig.mq_user, password=mqconfig.mq_password)
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    print("Try to connect {} ".format(MQ_HOST))
    client.connect(MQ_HOST, port=1883, keepalive=120)
    print("connected {} ".format(MQ_HOST))
    client.loop_start()
    pubTempData(client)

    print("sleep end")
    client.loop_stop()
