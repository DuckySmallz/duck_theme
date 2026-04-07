import os
import json

def get_temp():
    try:
        # Execute the nvidia-smi command to get GPU temperature
        temps = os.popen("nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader").read().strip()
        output = {"temp": f'{temps}', "icons": "°C "}
        return json.dumps(output)
    except Exception as e:
        return 1
print(get_temp())
