import paho.mqtt.client as mqtt
import time
from datetime import datetime
from datetime import timedelta
import random

import dbconfig
from dbhelper import DBHelper

import mqconfig

DB_HOST = dbconfig.IP_ADDR
DB = DBHelper(DB_HOST)

MQ_HOST = mqconfig.mq_host
MQ_TITLE = mqconfig.mq_title


count = 0
sample_count = 0
sample_freq = 10 # count of data in 1 sec.
record_freq = 1 # count of data to record in 1 sec.
sample_max = sample_freq / record_freq

sum_temp = 0.0
sum_cpuuse = 0.0
sum_memuse = 0.0

cpu_use = 7.2
mem_use = 34.4

BUF_MAX = record_freq
rec_buf = []

def pushData2DB(tim, dat):
    global count
    try:    
        #print("{:d} {},{:.4f}".format(count, tim.strftime('%Y-%m-%d %H:%M:%S'), dat))
        DB.insertStatusRec(tim, dat)
        
    except Exception as e:
        print ("Exception", e)

def on_connect(client, userdata, flags, rc):
    try:    
        print("Connect result: {}".format(mqtt.connack_string(rc)))
        client.connected_flag = True
        client.subscribe(MQ_TITLE, qos=1)
        
    except Exception as e:
        print ("Exception", e)

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed with QoS: {}".format(granted_qos[0]))

def on_message(client, userdata, msg):
    global count
    global sample_count
    global sum_temp, sum_cpuuse, sum_memuse
    global sample_max
    
    try:    
        count +=1
        payload_string = msg.payload.decode('utf-8')
        #print("{:d} Topic: {}. Payload: {}".format(count, msg.topic, payload_string))
    
        row_data = payload_string.split(",")
        #print(row_data)

        rec_time = datetime.strptime(row_data[0], "%Y-%m-%d %H:%M:%S.%f")
        sub_temp = float(row_data[1])
        sub_cpuuse = float(row_data[2])
        sub_memtotal = float(row_data[3])
        sub_memuse = float(row_data[4])
    
        sample_count += 1
        sum_temp += sub_temp
        sum_cpuuse += sub_cpuuse
        sum_memuse += sub_memuse
         
        if sample_count >= sample_max:  # 10 >= sample_max
            avg_temp = sum_temp / sample_count  # CPU Temp Avg
            str_temp = '{:.1f}'.format(avg_temp)  # to String Temp Avg
            avg_cpuuse = sum_cpuuse / sample_count  # CPU Used Avg
            str_cpuuse = '{:.1f}'.format(avg_cpuuse)  # to String CPU Used
            str_memtotal = '{:.1f}'.format(sub_memtotal)  # to String Memory Total
            avg_memuse = sum_memuse / sample_count  # Memory Used Total
            str_memuse = '{:.1f}'.format(avg_memuse)  # to String Memory Used

            # Memory Total is always constant, so do not average.
            str_data = '%s,%s,%s,%s' %(str_temp, str_cpuuse, str_memtotal, str_memuse)
            print(count, sample_count, rec_time, str_data)
            pushData2DB(rec_time, str_data)
            sample_count = 0
            sum_temp = 0
            sum_cpuuse = 0
            sum_memuse = 0
    
    except Exception as e:
        print ("Exception", e)

if __name__ == "__main__":
    print ("get client")
    client = mqtt.Client("SUB_CPU_TEMP_2_DB")
    client.username_pw_set(mqconfig.mq_user, password=mqconfig.mq_password)
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    print ("Try to connect {} ".format(MQ_HOST))
    client.connect(MQ_HOST, 1883, 120)
    print ("connected {} ".format(MQ_HOST))
    client.loop_forever()

