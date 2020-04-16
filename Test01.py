# libraries to import
import pandas
import requests

# import variables
from Variables01 import normalizationFactor

# printing
print('Hello')
print(normalizationFactor)

r = requests.get('https://www.python.org')
print(r.status_code)

