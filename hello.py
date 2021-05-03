import datetime
from collections import deque
from typing import List, Deque

import redis

from redisolar.dao.base import MetricDaoBase
from redisolar.dao.redis.base import RedisDaoBase
from redisolar.models import Measurement
from redisolar.models import MeterReading
from redisolar.models import MetricUnit
from redisolar.schema import MeasurementSchema

#l = ["a", "b"]
#print(f"list : {l}")

#site_id, value, unit, time = 1, 14, 'whU', datetime.datetime(2020, 10, 20, 18, 11, 12)
#m=Measurement(site_id, value, unit, time)
#print(f"{m}")

# testing list comprehension
print([letter for letter in "human" if letter >= 'h'])

# testing dict comprehension
fruits=dict()
fruits['apple'] = "green"
fruits.update({'orange': 'yellow', 'kiwi': 'green', 'guava': 'green', 'grape': 'red'})
print({fruit_type for (fruit_type,color) in fruits.items() if color == 'green'})
#print({fruit_type:color for (fruit_type, color) in fruits.items()})

# test set comprehension
students=set(('justin', 'chris', 'issac', 'kai', 'chris'))
print(students)
#print(type(students))
print({student for student in students if 'c' in student})

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(f"{dict(x)} is of type {type(x)}")

t=set(["asb","bad"])
print(f"{type(t)} -> {t}")