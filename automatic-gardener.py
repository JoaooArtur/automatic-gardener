import json
import http.client

print('Loading function')

def respond(response):
    send_sms(response)
    return {
        'statusCode': '200',
        'body': json.dumps(response),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def send_sms(response):
    conn = http.client.HTTPSConnection("m3mjz6.api.infobip.com")
    payload = json.dumps({
        "messages": [
            {
                "destinations": [{"to":"5547992002712"}],
                "from": "29175",
                "text": response
            }
        ]
    })
    headers = {
        'Authorization': 'App ${API-KEY}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    conn.request("POST", "/sms/2/text/advanced", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def lambda_handler(event, context):
    print(event)
    payload = json.loads(event['body'])
    print(payload)
    
    return handle_function_automatic_gardener(payload)
def triangular_membership(value, a, b, c):
    """Calcula a função de pertinência triangular."""
    if value < a or value > c:
        return 0
    elif a <= value < b:
        return (value - a) / (b - a)
    elif b <= value <= c:
        return (c - value) / (c - b)
    else:
        return 0

def handle_function_automatic_gardener(payload):
    humidity_value = int(payload.get('key1', 0))
    temperature_value = int(payload.get('key2', 0))
    sunlight_value = int(payload.get('key3', 0))

    humidity_low = triangular_membership(humidity_value, 0, 20, 50)
    humidity_medium = triangular_membership(humidity_value, 20, 50, 80)
    humidity_high = triangular_membership(humidity_value, 50, 100, 100)

    temperature_low = triangular_membership(temperature_value, 0, 10, 20)
    temperature_medium = triangular_membership(temperature_value, 10, 25, 35)
    temperature_high = triangular_membership(temperature_value, 25, 40, 50)

    sunlight_low = triangular_membership(sunlight_value, 0, 20, 50)
    sunlight_medium = triangular_membership(sunlight_value, 20, 50, 80)
    sunlight_high = triangular_membership(sunlight_value, 50, 100, 100)

    print(f'Humidity Low: {humidity_low}, Medium: {humidity_medium}, High: {humidity_high}')
    print(f'Temperature Low: {temperature_low}, Medium: {temperature_medium}, High: {temperature_high}')
    print(f'Sunlight Low: {sunlight_low}, Medium: {sunlight_medium}, High: {sunlight_high}')

    rules = {
        'watering_yes_1': min(humidity_low, temperature_high, sunlight_high),
        'watering_yes_2': min(humidity_low, sunlight_low, temperature_medium),
        'watering_no_1': min(humidity_high, sunlight_medium, temperature_low),
        'watering_no_2': min(humidity_medium, sunlight_low, temperature_low),
        'watering_no_3': max(humidity_high, sunlight_low)
    }

    defuzzification_values = {
        'watering_yes': max(rules['watering_yes_1'], rules['watering_yes_2']),
        'watering_no': max(rules['watering_no_1'], rules['watering_no_2'], rules['watering_no_3'])
    }

    numerator = (defuzzification_values['watering_yes'] * 1 + defuzzification_values['watering_no'] * 0)
    denominator = (defuzzification_values['watering_yes'] + defuzzification_values['watering_no'])
    centroid = numerator / denominator if denominator != 0 else 0

    print(f'Rules: {rules}')
    print(f'Watering Yes: {defuzzification_values["watering_yes"]}, Watering No: {defuzzification_values["watering_no"]}')
    print(f'Centroid: {centroid}')

    watering_decision = centroid * 100
    return respond(f'Decisão de regar (0 a 100): {watering_decision:.2f}')

