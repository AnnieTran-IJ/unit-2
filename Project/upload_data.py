import csv
import requests

# API Configuration
ip = "192.168.4.137"
user = {"username": "A_square", "password": "Ann&Annie"}


def login():
    try:
        answer = requests.post(f'http://{ip}/login', json=user)
        answer.raise_for_status()  # Raise an exception if the request fails
        cookie = answer.json()["access_token"]
        auth = {"Authorization": f"Bearer {cookie}"}
        print("Login successful.")
        return auth
    except Exception as e:
        print(f"Failed to log in: {e}")
        return None


def upload_data_from_csv(csv_file, sensor_ids, ip):
    try:
        with open(csv_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                timestamp = row["timestamp"]  # Get the timestamp
                for field, sensor_id in sensor_ids.items():
                    value = row.get(field)  # Get the value for the sensor
                    if value and value.lower() != "nan":
                        try:
                            # Convert the value to float
                            value = float(value)

                            # Log in for every request
                            auth = login()
                            if not auth:
                                print("Skipping data upload due to failed login.")
                                continue

                            # Prepare the record for upload
                            new_record = {
                                "sensor_id": sensor_id,
                                "value": value
                            }

                            # API endpoint
                            url = f"http://{ip}/reading/new"

                            # Post the data to the API
                            response = requests.post(url, json=new_record, headers=auth)

                            # Check response
                            if response.status_code == 200:
                                try:
                                    response_data = response.json()
                                    print(f"Successfully uploaded {field} value {value} to sensor ID {sensor_id} at {timestamp}.")
                                    print(f"Server response: {response_data}")
                                except ValueError:
                                    print(f"Upload succeeded, but unable to parse response for {field} value {value} at {timestamp}.")
                            else:
                                print(f"Failed to upload {field} value {value} to sensor ID {sensor_id}. Server response: {response.text}")

                        except ValueError as ve:
                            print(f"Invalid value for {field}: {value}. Error: {ve}")
                        except Exception as e:
                            print(f"Error posting {field} data: {e}")
    except FileNotFoundError:
        print(f"File {csv_file} not found.")
    except Exception as e:
        print(f"Error uploading data from CSV: {e}")


sensor_ids = {
    "DHT_temperature": 185,
    "DHT_humidity": 186,
    "BME_temperature": 187,
    "BME_pressure": 197,
    "BME_humidity": 188,
}

# Upload data, logging in before each data upload
upload_data_from_csv(csv_file="collected_data.csv", sensor_ids=sensor_ids, ip=ip)
