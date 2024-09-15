import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2)), "Stock price incorrect"


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2)), "Stock price incorrect"


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatioPriceBEqualPriceA(self):

    self.assertEqual(getRatio(120.2, 120.2), 1, "Stock ratio should be 1")

  def test_getRatio_calculateRatioPriceBGreaterThanPriceA(self):

    self.assertEqual(getRatio(100.0, 200.0), 0.5, "Stock ratio should be 0.5")

  def test_getRatio_calculateRatioPriceAGreaterThanPriceB(self):

    self.assertEqual(getRatio(200.0, 100.0), 2, "Stock ratio should be 2")
  
  def test_getRatio_calculateRatioPriceAIsZero(self):

    self.assertEqual(getRatio(0, 120.4), 0, "Stock ratio should 0")
  
  def test_getRatio_calculateRatioPriceBIsZero(self):

    self.assertEqual(getRatio(135.3, 0),  None, "Stock ratio should be None")

if __name__ == '__main__':
    unittest.main()
