#Authon Ivor
from host import models
import json,datetime
start = datetime.datetime.now() + datetime.timedelta(days=-5)
yes_time = start.strftime("%Y-%m-%d")

def insert(request):
    with open('D:\pythonProjects\oldboy\project\host_management\host\\a.txt','r') as f:
        data = json.load(f)
        for car_info in data.get('data').get('result'):
            car_license_num = car_info.get('carnum')
            car_total_operation_mileage = car_info.get('totalmileage')
            car_total_operation_time1 = car_info.get('totaltime')
            car_total_operation_time2 = car_info.get('totaltimef')
            car_average_speed =  car_info.get('avgspeed')
            print(car_license_num,car_total_operation_mileage,car_total_operation_time2,car_average_speed)
            print(type(car_license_num))
            car_obj = models.CarOperationInfo.objects.create(car_license_num=car_license_num,
                                                               operation_time=start,
                                                               car_total_operation_mileage=car_total_operation_mileage,
                                                               car_total_operation_time=car_total_operation_time1,
                                                               car_total_operation_timef=car_total_operation_time2,
                                                               car_average_speed=car_average_speed)

def insert2(request):
    with open('D:\pythonProjects\oldboy\project\host_management\host\\b.txt','r') as f:
        data = json.load(f)
        for car_info in data.get('data').get('result'):
            car_license_num = car_info.get('carnum')
            car_mileage = car_info.get('mileage')
            car_standard_FC = car_info.get('oilrefer')
            car_actual_FC = car_info.get('oil')
            car_oil_total_num = car_info.get('oilcount_all')
            car_oil_total_fee = car_info.get('moneycount_all')
            car_oil_total_count = car_info.get('oilnum_all')
            print(car_mileage,car_standard_FC,car_actual_FC,car_oil_total_num,car_oil_total_fee,car_oil_total_count)
            car_obj = models.CarFuelConsumption.objects.create(car_license_num=car_license_num,
                                                               operation_time=start,
                                                               car_mileage=car_mileage,
                                                               car_standard_FC=car_standard_FC,
                                                               car_actual_FC=car_actual_FC,
                                                               car_oil_total_num=car_oil_total_num,
                                                               car_oil_total_fee=car_oil_total_fee,
                                                               car_oil_total_count=car_oil_total_count
                                                               )
