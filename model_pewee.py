from peewee import *
# нужно создать базу командой CREATE DATABASE bill;
db = MySQLDatabase('bill', user='root', password='password',
                         host='127.0.0.1', port=3306)

#db = SqliteDatabase('bill.db')
db.connect()
class Call(Model):
    phone_in = CharField(max_length = 15)
    phone_out = CharField(max_length = 15)
    start_call = DateTimeField()
    finish_call = DateTimeField()
    cost = IntegerField()

    class Meta:
        database = db 

class Tariff(Model):
    type_call = CharField(max_length = 10, unique = True)
    price = IntegerField()

    class Meta:
       database = db 

Call.create_table()
Tariff.create_table()

try:
    tariff_gsm = Tariff.create(type_call='GSM', price=10)
    tariff_cdma = Tariff.create(type_call='CDMA', price=15)
    tariff_lte = Tariff.create(type_call='LTE', price=20)
except:
    print(Exception)


def get_tariff():
    tariff_dic = dict()
    for tariff in Tariff.select():
        tariff_dic[str(tariff.type_call)]=int(tariff.price)
    return tariff_dic

def get_calls(number):
    query = Call.select().where((Call.phone_in==number)|(Call.phone_out==number))
    return get_in_bases(query)
   
def get_calls():
    query = Call.select()
    return get_in_bases(query)    

def get_in_bases(query):    
    list_calls_number = []
    for call in query: 
        dic_call = {'phone_in':call.phone_in, 'phone_out':call.phone_out,
                    'start':call.start_call.strftime("%Y-%m-%d %H:%M:%S"), 
                    'finish':call.finish_call.strftime("%Y-%m-%d %H:%M:%S"),
                    'cost':call.cost}
        list_calls_number.append(dic_call)
    return list_calls_number
