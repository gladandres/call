import json
import os
from datetime import datetime 
from model_pewee import Call, Tariff, get_tariff

PATH = f"D:\JSON" #каталог с json -ами


tariff = get_tariff()

files = os.listdir(PATH)
files_json = filter(lambda x: x.endswith('.json'),files)
list_files_json_del = []
for file_json in files_json:
    
    with open(PATH +'\\' + file_json) as f:
        template = json.load(f)
        
        phone_in = template['Phone_In']
        phone_out = template['Phone_Out']
        start_time = datetime.fromtimestamp(int(template['Start']))
        finish_time = datetime.fromtimestamp(int(template['Finish']))
        price = tariff[template['Type']]
        delta = (finish_time - start_time).seconds
        cost =  price * (delta//60)         # поминутный целочисленный интервал начисления 
        try:
            call = Call.create(phone_in=phone_in, phone_out=phone_out, start_call=start_time, finish_call=finish_time, cost=cost) 
            list_files_json_del.append(file_json)  # лист файлов на удаление
        except:
            print('ошибка сохранения данных')
        finally:
            f.close()

for file in list_files_json_del:
    os.remove(PATH +'\\' + file)
