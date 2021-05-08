import json
import requests
import settings

class SlotFinderException(Exception):
    def __init__(self, message):
        super().__init__(message)

class SlotFinder:
    def __init__(self):
        self._url = settings.URL
        self._vaccines = settings.VACCINE
        self._min_age = settings.MIN_AGE
        self._headers = settings.HEADERS
        self._interval = settings.FREQUENCY
        self._date = settings.DATE

    @property
    def interval(self):
        return self._interval

    def parse_data(self, data):
        result = []
        for idx, item in enumerate(data):
            vaccine = item['vaccine']
            slots = item['slots']
            capacity = item['available_capacity']
            fee = item['fee_type']
            name = item['name']
            min_age = item['min_age_limit']
            address = item['address']
            block = item['block_name']

            if min_age == self._min_age and vaccine in self._vaccines:
                result.append({
                    'Vaccine': vaccine,
                    'Slots': slots,
                    'Name': name,
                    'Address': address,
                    'Block': block,
                    'Fees': fee,
                    'Vaccine Capacity': capacity
                })

        return result

    def find_slots(self):
        try:
            print("Searching for Date : {}".format(self._date))
            response = requests.get(self._url, headers = self._headers)
            if response.status_code == 200:
                data = response.json()
                result = self.parse_data(data['sessions'])
                return result
            else:
                raise SlotFinderException(response.status_code)
        except Exception as ex:
            raise SlotFinderException('Error Occured. {}'.format(ex))