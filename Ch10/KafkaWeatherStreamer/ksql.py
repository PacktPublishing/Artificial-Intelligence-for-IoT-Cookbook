import ksql 
client = KSQLAPI('http://localhost:8088')
query = client.query('select * from table1')
for item in query: print(item)