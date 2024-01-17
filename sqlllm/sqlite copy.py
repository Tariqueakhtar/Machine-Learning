# Import module 
import sqlite3 
  
# Connecting to sqlite 
conn = sqlite3.connect('test.db') 
  
# Creating a cursor object using the  
# cursor() method 
cursor = conn.cursor() 

# Drop the table if it already exists
cursor.execute("DROP TABLE IF EXISTS PARCEL;")
 
# Creating table 
table ="""CREATE TABLE PARCEL(ID VARCHAR(255), SHIPPER_COUNTRY VARCHAR(255), 
CONSIGNEE_COUNTRY VARCHAR(255));"""
cursor.execute(table) 
  
# Queries to INSERT records. 
cursor.execute('''INSERT INTO PARCEL VALUES ('1', 'US', 'UAE')''') 
cursor.execute('''INSERT INTO PARCEL VALUES ('2', 'US', 'KSA')''') 
cursor.execute('''INSERT INTO PARCEL VALUES ('3', 'UK', 'KUWAIT')''') 
cursor.execute('''INSERT INTO PARCEL VALUES ('4', 'UK', 'KSA')''') 
cursor.execute('''INSERT INTO PARCEL VALUES ('5', 'UK', 'UAE')''') 
cursor.execute('''INSERT INTO PARCEL VALUES ('6', 'UK', 'UAE')''')   
cursor.execute('''INSERT INTO PARCEL VALUES ('7', 'UK', 'UAE')''') 
cursor.execute('''INSERT INTO PARCEL VALUES ('8', 'USU', 'KUWAIT')''') 
cursor.execute('''INSERT INTO PARCEL VALUES ('9', 'US', 'KUWAIT')''') 
cursor.execute('''INSERT INTO PARCEL VALUES ('10', 'US', 'KUWAIT')''') 
cursor.execute('''INSERT INTO PARCEL VALUES ('11', 'US', 'UAE')''') 

# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM PARCEL''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
conn.commit() 
  
# Closing the connection 
conn.close()