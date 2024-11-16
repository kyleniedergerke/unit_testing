import unittest
from datetime import datetime

def ticker_test(symbol):
    if len(symbol) > 7 or len(symbol) < 1:
        return False
    if not symbol.isupper():
        return False
    if not symbol.isalpha():
        return False
    return True

def chart_test(types):
    charts = {"1", "2"}
    return types in charts

def time_series_test(times):
    time_series = {"1", "2", "3", "4"}
    return times in time_series

def date_test(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        return False
    return True

class Validation(unittest.TestCase):

    def test_1(self):
        self.assertTrue(ticker_test("KO"))
        self.assertFalse(ticker_test("ko"))  

    def test_2(self):
        self.assertTrue(chart_test("1" or "2"))
        self.assertFalse(chart_test("A" or "3"))  

    def test_3(self):
        self.assertTrue(time_series_test("1" or "4"))
        self.assertFalse(time_series_test("A" or "0" or "5"))  


    def test_4_5(self):
        self.assertTrue(date_test("2003-07-11" or "2024-11-15"))
        self.assertFalse(date_test("07-11-2003" or "2024/11/15")) 

if __name__ == "__main__":
    unittest.main()
