#Esboço da IA, precisa ser refatorada com todos os sensores e logica.
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt


humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
sunlight = ctrl.Antecedent(np.arange(0, 101, 1), 'sunlight')

watering = ctrl.Consequent(np.arange(0, 101, 1), 'watering')

humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['medium'] = fuzz.trimf(humidity.universe, [0, 50, 100])
humidity['high'] = fuzz.trimf(humidity.universe, [50, 100, 100])

temperature['low'] = fuzz.trimf(temperature.universe, [0, 0, 20])
temperature['medium'] = fuzz.trimf(temperature.universe, [0, 20, 40])
temperature['high'] = fuzz.trimf(temperature.universe, [20, 40, 40])

sunlight['low'] = fuzz.trimf(sunlight.universe, [0, 0, 50])
sunlight['medium'] = fuzz.trimf(sunlight.universe, [0, 50, 100])
sunlight['high'] = fuzz.trimf(sunlight.universe, [50, 100, 100])

watering['no'] = fuzz.trimf(watering.universe, [0, 0, 50])
watering['yes'] = fuzz.trimf(watering.universe, [0, 50, 100])

rule1 = ctrl.Rule(humidity['low'] & temperature['high'] & sunlight['high'], watering['yes'])
rule2 = ctrl.Rule(humidity['medium'] & temperature['medium'] & sunlight['medium'], watering['no'])
rule3 = ctrl.Rule(humidity['high'] | temperature['low'], watering['no'])

watering_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
watering_sim = ctrl.ControlSystemSimulation(watering_ctrl)

def decide_watering(humidity_value, temperature_value, sunlight_value):
    watering_sim.input['humidity'] = humidity_value
    watering_sim.input['temperature'] = temperature_value
    watering_sim.input['sunlight'] = sunlight_value
    watering_sim.compute()
    return watering_sim.output['watering']

humidity_value = 40
temperature_value = 30
sunlight_value = 60

decision = decide_watering(humidity_value, temperature_value, sunlight_value)
print(f'Decisão de regar (0 a 100): {decision:.2f}')

#humidity.view()
#temperature.view()
#sunlight.view()
#watering.view()
#plt.show()
