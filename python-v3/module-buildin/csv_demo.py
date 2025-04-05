import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))

import csv

from pkg.record import Record

file_path = 'files/record.csv'

def csv_to_objects(file_path):
    objects_list = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            obj = Record(**row)
            objects_list.append(obj)
    return objects_list

""" csv转对象 """
def _demo01():
    records = csv_to_objects(file_path)
    for record in records:
        print(str(record))

_demo01()
