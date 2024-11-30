import csv
import requests

ip = "192.168.4.137"
user = {"username": "A_square", "password": "Ann&Annie"}


try:
    answer = requests.post(f'http://{ip}/login', json=user)
    cookie = answer.json()["access_token"]
    auth = {"Authorization": f"Bearer {cookie}"}
    print("Login successful.")
except Exception as e:
    print(f"Failed to connect to API: {e}")
    auth = None

def upload_data_from_csv(csv_file, sensor_ids, ip, auth):
    try:
        with open(csv_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                timestamp = row["timestamp"]
                for field, sensor_id in sensor_ids.items():
                    value = row.get(field)
                    if value is not None and value != "nan" and value != "":
                        try:
                            payload = {"value": float(value)}  # Convert to float for posting
                            url = f"http://{ip}/sensor/{sensor_id}/data"

                            # Post data to the API
                            response = requests.post(url, json=payload, headers=auth)

                            # Log response
                            if response.status_code == 200:
                                print(f"Successfully uploaded {field} value {value} to sensor ID {sensor_id} at {timestamp}")
                            else:
                                print(f"Failed to upload {field} value {value} to sensor ID {sensor_id}. Error: {response.text}")
                        except Exception as e:
                            print(f"Error posting {field} data: {e}")
    except Exception as e:
        print(f"Error uploading data from CSV: {e}")

# Sensor IDs mapped to the CSV column names
sensor_ids = {
    "DHT_temperature": 185,
    "DHT_humidity": 186,
    "BME_temperature": 187,
    "BME_pressure": 197,
    "BME_humidity": 188,
}

if auth:
    upload_data_from_csv(csv_file="collected_data.csv", sensor_ids=sensor_ids, ip=ip, auth=auth)
