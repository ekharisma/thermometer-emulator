from datetime import datetime

def get_time():
    return datetime.now().isoformat()

def get_temperature_value(index:int):
    temperature_list = [i for i in range(25, 35)]
    return temperature_list[index]