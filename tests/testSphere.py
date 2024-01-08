import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-sphere" in j:
            exec("".join(i['source']))


class testCases(unittest.TestCase):
    def testVolume(self):
        self.assertTrue(round((4/3) * 3.141593 * 8 ** 3, 2)-round(vol, 2)<0.1, "Are you sure you calculated the volume of the sphere correctly?")