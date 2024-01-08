import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-receipt" in j:
            exec("".join(i['source']))


class testCases(unittest.TestCase):
    def testName(self):
        self.assertTrue(isinstance(receipt['name'], str), "The value that matches the 'name' key should be a string.")
    def testItems(self):
        self.assertTrue(isinstance(receipt['items'], list), "The value that matches the 'items' key should be a list.")
    def testDiscount(self):
        self.assertTrue(isinstance(receipt['discount'], bool), "The value that matches the 'discount' key should be a bool.")
    def testPrice(self):
        self.assertTrue(isinstance(receipt['price'], int)|isinstance(receipt['price'], float), "The value that matches the 'price' key should be a float.")

