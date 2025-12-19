import csv
import platform
import os
from datetime import datetime
HEADERS = [
	"timestamp",
	"system",
	"release",
	"machine",
	"processor"
]

DATA_FILE = "data/system_data.csv"

def collect_system_data():
	row = [ 
		datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
		platform.system(),
		platform.release(),
		platform.machine(),
		platform.processor()
	]
	return row

def save_to_csv(row):
	os.makedirs("data", exist_ok=True)

	file_exists = os.path.isfile(DATA_FILE)

	with open (DATA_FILE, mode="a", newline="") as file:
		writer = csv.writer(file)

		if not file_exists:
			writer.writerow(HEADERS)

		writer.writerow(row)

if __name__ == "__main__":
 data = collect_system_data()
 save_to_csv(data)
 print("Dados Coletados e salvos com sucesso.")

