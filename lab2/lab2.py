import csv
from datetime import datetime
import numpy as np
from matplotlib import figure
from matplotlib import pyplot as plt
%matplotlib inline

filepath = 'net.csv'

sum_bytes = 0
k_traffic = 0.5
bytes_arr = []
date_time = []
list_d_t = []

#открытие файла и обработка данных в нем
with open(filepath, newline='') as file: 
    reader = csv.DictReader(file, delimiter=',') 
    for row in reader:
        bytes_arr.append(row['ibyt'])
        bytes_arr = bytes_arr[:4823]
        date_time.append(row['ts'])
        date_time = date_time[:4823]
    for byte in bytes_arr:
        bytes_arr = [int(byte) for byte in bytes_arr]
    for b in range(len(bytes_arr)):    
        sum_bytes += bytes_arr[b]
        b += 1       
    for t in range(len(date_time)):
        date_time[t] = datetime.strptime(date_time[t], '%Y-%m-%d %H:%M:%S')
        list_d_t.append(date_time[t])
        
#тарификация    
Q = sum_bytes / 10**6
X = round(Q * k_traffic, 2)
print('Стоимость услуг: ' + str(X) + ' рублей')

#построение графика    
dict_t_b = dict(zip(list_d_t, bytes_arr))
lx = list(dict_t_b.keys())
lx.sort()
for i in lx:
    d[i] = dict_t_b[i]
ly = list(d.values())
for l in ly:
    l = l / 10**6
x = np.array(lx)
y = np.array(ly)
plt.figure(figsize=(16,10), dpi= 80)
plt.title('График зависимости объёма трафика от времени', fontsize=12)
plt.xlabel("День, время", fontsize=12)
plt.ylabel("Объём трафика, байт*10^-7", fontsize=12)
plt.plot(x, y)
plt.show()