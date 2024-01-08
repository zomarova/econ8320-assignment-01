import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-sphereOrCube" in j:
            exec("".join(i['source']))


class testCases(unittest.TestCase):
    def testVolume(self):
        self.assertTrue(sphereOrCube, "Your comparison did not arrive at the correct BOOLEAN value")