import random
import json

class SensorDataModel:
    def __init__(self, sgid, temperature, humidity, CO2):
        self.sgid = sgid
        self.temperature = temperature
        self.humidity = humidity
        self.CO2 = CO2

    def to_json(self):
        return json.dumps({
            "sgid": self.sgid,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "CO2": self.CO2
        })

def generate_random_sensor_data():
    sgid = random.choice(['SENSOR_1', 'SENSOR_2'])

    return SensorDataModel(
        sgid=sgid,
        temperature=random.uniform(-20.0, 50.0),
        humidity=random.uniform(0, 100),
        CO2=random.uniform(300, 800)
    )