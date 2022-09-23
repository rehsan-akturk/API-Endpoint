import requests




# requests with parameters
# 1.Show the number of impressions and clicks that occurred before the 1st of June 2017,
# broken down by channel and country, sorted by clicks in descending order. Hint:

url = "http://127.0.0.1:8081/api?date=2017-06-01"
res = requests.get(url)
print(res)

#2.Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order

url = "http://127.0.0.1:8081/api?date=2017-05-01&date_to=2017-05-31&os=ios"
res = requests.get(url)
print(res)


#3.Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

url = "http://127.0.0.1:8081/api?date=2017-06-01&country=us"
res = requests.get(url)
print(res)


#4.Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order.
# Please think carefully which is an appropriate aggregate function for CPI.

url = "http://127.0.0.1:8081/api?country=ca"
res = requests.get(url)
print(res)


#no parameters
url = "http://127.0.0.1:8081/"
res = requests.get(url)
print(res)
