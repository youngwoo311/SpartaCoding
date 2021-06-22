a = 2
b = 3

print(a+b)

first_name = 'youngwoo'
last_name = 'lee'

print(first_name + last_name)
print(first_name + str(a))

a_list = ['사과', '배', '감']

print(a_list[2])

a_list.append('수박')
print(a_list)

a_dict = {'name' : 'bob', 'age' : 27}
print(a_dict['name'])

a_dict['height'] = 180
print(a_dict)

def sum(num1, num2):
    return num1 + num2

result = sum(2,3)
print(result)

def is_adult(age):
    if age > 20:
        print('성인입니다')
    else:
        print('청소년입니다')

is_adult(30)
is_adult(15)

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for ff in fruits:
    if ff == '배':
        count += 1
print(count)

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    if person['age'] < 20:
        print(person)
    print(person['name'], person['age'])

import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

print(rjson)
print(rjson['RealtimeCityAir']['row'][0]['NO2'])

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    gu_name = gu['MSRSTE_NM']
    gu_mise = gu['IDEX_MVL']

    if (gu_mise > 30) :
        print(gu_name, gu_mise)

 