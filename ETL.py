import urllib.request, json, hashlib, time, pandas as pd, sqlite3 as sql

def hash(l):
    m = hashlib.sha1()
    m.update(l.encode('utf-8'))
    r=m.hexdigest()
    languagesSH1_list.append(r)

def create_DB():
    conn = sql.connect("database.db")
    conn.commit()
    conn.close()

def create_table():
    conn = sql.connect("database.db")
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE data (
            max_data real,
            min_data real,
            avg_data real,
            total_data real
        )"""
    )
    conn.commit()
    conn.close()

def insert_row(maximun, minimun,average, totall):
    conn = sql.connect("database.db")
    cursor=conn.cursor()
    query="INSERT INTO data VALUES ({},{},{},{})".format(maximun, minimun,average, totall)
    cursor.execute(query)
    conn.commit()
    conn.close()

url="https://restcountries.com/v3.1/subregion/central"
with urllib.request.urlopen(url) as response:
    s=response.read()
    data=json.loads(s)

region_list=[]
city_name_list=[]
languages_list=[]
languagesSH1_list=[]
time_list=[]

for d in range(len(data)):
    region=data[d]['region']
    city_name=data[d]['name']['common']
    language=data[d]['languages']
    if len(language)>1:
        for languages in language.values():
            region2=region
            city_name2=city_name
            region_list.append(region2)
            city_name_list.append(city_name2)
            languages_list.append(languages)
            hash(languages)
    else:
        for languages in language.values():
            region_list.append(region)
            city_name_list.append(city_name)
            languages_list.append(languages)
            hash(languages)
    
start=time.time()
df = pd.DataFrame()
df['Region']=region_list
df['City Name']=city_name_list
df['Language']=languagesSH1_list
end=time.time()
execution_time=end-start
short_time=round(execution_time,3)

for exec_time in region_list:
    time_list.append(short_time)

#time_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
df['Time']=time_list

max=list(df.max())
min=list(df.min())
avg=df['Time'].mean()
total=df['Time'].sum()

create_DB()
create_table()
insert_row(max[3],min[3],avg,total)

json_file = df.to_json(r'C:\Users\user\Desktop\export.json',orient='records')