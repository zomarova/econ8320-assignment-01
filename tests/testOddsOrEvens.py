import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-oddsOrEvens" in j:
            exec("".join(i['source']))


class testCases(unittest.TestCase):
    def testVolume(self):
        test = [-1*((x%2+1)*2-3)*x for x in range(50)]

        self.assertTrue(all([float(test[i])==float(oddsOrEvens[i]) for i in range(50)]), "You didn't get your list quite right. Make sure odd numbers are negative and even numbers are positive.")

