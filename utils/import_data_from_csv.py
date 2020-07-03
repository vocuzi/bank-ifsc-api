# Import CSV to Default Django Database
# To run : 
# python manage.py shell < import_data_from_csv.py
import csv
from api.models import Bank

filename = "utils/bank_branches.csv"
fields, rows = [],[]

with open(filename) as file:
	f = csv.reader(file)
	fields = next(f)
	for row in f:
		rows.append(row)
	print(f"ROWS READ : {len(rows)}")

payload = []
for row in rows:
	df = Bank(
		ifsc=row[0],
		bank_id=row[1],
		branch=row[2],
		address=row[3],
		city=row[4],
		district=row[5],
		state=row[6],
		bank_name=row[7],
	)
	payload.append(df)

Bank.objects.bulk_create(payload)