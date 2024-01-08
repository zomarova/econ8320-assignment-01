import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-madLib" in j:
            exec("".join(i['source']))
            
class testCases(unittest.TestCase):
    def testVolume(self):
        test = ("__1__" not in myMadLib) & ("__2__" not in myMadLib) & ("__3__" not in myMadLib) & ("__4__" not in myMadLib) & ("__5__" not in myMadLib) & ("__6__" not in myMadLib)

        self.assertTrue(test, "Did you replace ALL of the numbers? You can daisy-chain replace statements. :)")