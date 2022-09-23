# FastAPI-Django
FastAPI and  GUI Django 



#The first thing to do is to clone the repository:
git@github.com:rehsan-akturk/FastAPI-Django.git

#Create you virtualenv and install the packages
pip install -r requirements.txt


#database connection
Enter the database connection information in main py 
try:
    conn = psycopg2.connect(
    database='xxxxxx', user='xxxxxx', password='xxxxx', host='xxxxx', port= 'xxxx')

    cursor = conn.cursor()
    print ("Connected!\n")
except:
    print ("UnConnected!\n")
	



#Run the FastAPI main.py .
uvicorn main:app --reload


#Run the application.
note=runserver port 8080
python manage.py runserver



#html home pages



#html filter home pages




