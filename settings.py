from datetime import datetime, timedelta

URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'
PINCODE = '201301'
CURRENT_DATE = datetime.now()
DATE = (CURRENT_DATE + timedelta(1)).strftime('%d-%m-%Y')
FREQUENCY = 1
MIN_AGE = 18
VACCINE = ['COVAXIN', 'COVISHIELD']
HEADERS = {
            'Accept-Language': 'hi_IN', 
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51', 
            'Media-type': 'application/json'
        }

URL = URL.format(PINCODE, DATE)