from typing import Optional
from fastapi import FastAPI, HTTPException
from  database import  engine
import json


conn=engine.connect()


app = FastAPI()

##########API Function with parameters ########
@app.get("/api")
async def get(date: Optional[str] = None,date_to: Optional[str]=None,
    os: Optional[str] = None,country: Optional[str]=None):


   if date and date_to and os  :
      try:

            rows=conn.execute(f"select sum(installs) as 'installs' ,date,os  from test.sampledataset where date between '{date}' and '{date_to}' and os='{os}' group by date order by date asc")
            ### Mapping rows with column names with dictionary #####
            r = [dict(( rows.cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in rows.cursor.fetchall()]
            print(r)

            return {
               "code":0,
               "msg":"Success",
               "headers": {"Content-Type": "application/json"},
                "body": json.dumps(r, indent=4, sort_keys=True, default=str,ensure_ascii=False)

             }
      except Exception as err:
               raise HTTPException(400, "failed to do something")

   if date and country:

       try:

           rows=conn.execute(
               f"select  revenue,os,date  from test.sampledataset  where date= '{date}' and country='{country}'  group by os order by revenue desc")
           ### Mapping rows with column names with dictionary #####
           r = [dict((rows.cursor.description[i][0], value) \
                     for i, value in enumerate(row)) for row in rows.cursor.fetchall()]
           print(r)

           return {
               "code": 0,
               "msg": "Success",
               "headers": {"Content-Type": "application/json"},
               "body": json.dumps(r, indent=4, sort_keys=True, default=str, ensure_ascii=False)

           }
       except Exception as err:
           raise HTTPException(400, "failed to do something")

   if country :

       try:

           rows=conn.execute(
               f"select (spend / installs) as 'cpi',spend,channel from test.sampledataset  where   country='{country}'  group by channel order by cpi desc")
           ### Mapping rows with column names with dictionary #####
           r = [dict((rows.cursor.description[i][0], value) \
                     for i, value in enumerate(row)) for row in rows.cursor.fetchall()]
           print(r)

           return {
               "code": 0,
               "msg": "Success",
               "headers": {"Content-Type": "application/json"},
               "body": json.dumps(r, indent=4, sort_keys=True, default=str, ensure_ascii=False)

           }
       except Exception as err:
           raise HTTPException(400, "failed to do something")


   if date :

      try:
            rows=conn.execute(f"select channel, country, sum(impressions) as impressions, sum(clicks) as clicks from test.sampledataset where date < '{date}' group by channel, country order by clicks desc")
        ### Mapping rows with column names with dictionary #####
            r = [dict(( rows.cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in rows.cursor.fetchall()]

            return {
               "code":0,
               "msg":"Success",
               "headers": {"Content-Type": "application/json"},
               "body": json.dumps(r, indent=4, sort_keys=True, default=str,ensure_ascii=False)

             }
      except Exception as err:
               raise HTTPException(400, "failed to do something")

#no params
@app.get("/")
async def get():

    try:
        rows = conn.execute("SELECT * FROM test.sampledataset  limit 50;")
        r = [dict((rows.cursor.description[i][0], value) \
                  for i, value in enumerate(row)) for row in rows.cursor.fetchall()]

        return {
            "code": 0,
            "msg": "Success",
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(r, indent=4, sort_keys=True, default=str, ensure_ascii=False)
        }
    except Exception as err:
        raise HTTPException(400, "failed to do something")




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8081)







	

	