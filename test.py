import unittest
import datetime

class PayloadCheck(unittest.TestCase):
    def temperature_test(self):
        for i in range(11):
            temperature = read_temperature(i)
            self.assertTrue(25 <= temperature <= 35)

    def timestamp_test(self):
        self.assertTrue(isinstance(read_timestamp, str))

def read_temperature(index: int):
    temperature = [i for i in range(25, 36)]
    print(temperature)
    return temperature[index]

def read_timestamp():
    return datetime.now().isoformat()


if __name__ == '__main__':
    unittest.main()
