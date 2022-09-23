# FastAPI-Sqlalchemy
FastAPI Sqlalchemy



# The first thing to do is to clone the repository:
git @github.com:rehsan-akturk/FastAPI-Django.git

# Create you virtualenv and install the packages
pip install -r requirements.txt


# database connection
Enter the database connection information in main py 

![image](https://user-images.githubusercontent.com/63419567/191960520-ceea04eb-8344-4589-a07a-61866f3cd7c2.png)




# Run the FastAPI main.py .


uvicorn main:app --reload

![image](https://user-images.githubusercontent.com/63419567/191960630-dceff03e-8996-40a9-97a3-ff0f7b007090.png)



# Requests with Parameters


1.Show the number of impressions and clicks that occurred before the 1st of June 2017,
broken down by channel and country, sorted by clicks in descending order. Hint:

http://127.0.0.1:8081/api?date=2017-06-01"


2.Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order

http://127.0.0.1:8081/api?date=2017-05-01&date_to=2017-05-31&os=ios

3.Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

http://127.0.0.1:8081/api?date=2017-06-01&country=us


4.Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order.
Please think carefully which is an appropriate aggregate function for CPI.


http://127.0.0.1:8081/api?country=ca


















