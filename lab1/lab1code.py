import csv
filepath = 'data.csv'
out_call = [] #исходящие звонки
sms_count = []
call_dur=[]
k_call = 2
k_sms = 1
sms_free = 10
def read_csv_to_lists(filepath)
with open(filepath, newline='') as file: #считывание файла
    reader = csv.reader(file, delimiter=',') #получение доступа к файлу
    for row in reader: #row - все данные, взятые из reader
        out_call.append(row[1]) #добавление в список out_call элементов столбца с индексом 1, то есть столбца msisdn_originin_call.append(row[2])
        call_dur.append(row[3]) #добавление в список call_dur элементов столбца с индексом 3, то есть столбца call_duration
        sms_count.append(row[4]) #добавление в список sms_count элементов столбца с индексом 4, то есть столбца sms_number
    index = list.index(out_call, '915783624') #поиск индекса элемента в списке
    T = call_dur[index] #запись элемента с индексом index в переменную duration
    T = float(T)
    N = sms_count[index] #запись элемента с индексом index в переменную sms
    N = int(N)
X = T * k_call
if N <= sms_free:
    k_sms = 0
elif N > sms_free:
    k_sms = 1
    Y = (N - sms_free) * k1
Z = X + Y
print('Итоговая стоимость за все услуги: ' + str(Z) + ' рублей')
