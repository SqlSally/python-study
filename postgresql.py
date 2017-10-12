
import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="192.168.0.18", port="5432")

cur = conn.cursor()
cur.execute("""select * from almanac.hexagram""")
rows = cur.fetchall()
print("\nRows: \n")
for row in rows:
    print("   ", row[1])