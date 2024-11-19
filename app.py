import time
import requests

try:
    response = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    generate = response.json()
    print('I will tell you something amazing if you wait...')
    time.sleep(5)
    print('Are your ready to hear my secret ? :-)')
    time.sleep(5)
    print('Wait...')
    time.sleep(5)
    print('Make a promise')
    time.sleep(5)
    print('You worth it :-)')
    time.sleep(5)
    print('...')
    print(generate['insult'])
    print('...')
    print('Sorry for bothering you!!! ;-D')

except:
    print("No surprise for you today. ;-)")

