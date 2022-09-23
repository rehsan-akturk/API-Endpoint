
from sqlalchemy import create_engine
import pandas as pd


############ connetion database ####################
username = 'root'
password = '12345'
host = 'localhost'
port = 3306
DB_NAME = 'test'

engine = create_engine(f"mysql://{username}:{password}@{host}:{port}")


with engine.connect() as conn:
    ############ create database ####################
    conn.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    ############ create table ####################
    conn.execute("CREATE TABLE  IF NOT EXISTS test.sampledataset (date date, channel  varchar(255), country varchar(255), os  varchar(255), impressions varchar(255),clicks  varchar(255), installs varchar(255),spend  varchar(255), revenue varchar(255)) ;")
    ############ read csv file and insert data ####################
    data=pd.read_csv('dataset.csv')
    df=pd.DataFrame(data)

    values=""
    for row in df.itertuples():

        values += "('{}','{}','{}','{}','{}','{}','{}','{}','{}'),".format(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])


    val=values[0:-1]
    ############ bulk insert ####################
    query=f"INSERT INTO test.sampledataset (date,channel,country,os,impressions,clicks,installs,spend,revenue) VALUES {val} "
    conn.execute (query)













   
    
    

