# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import pandas

data = pandas.read_csv('gapminder.csv')

print (len(data), len(data.columns))


data['oilperperson'] = data['oilperperson'].convert_objects(convert_numeric=True);
data['relectricperperson'] = data['relectricperperson'].convert_objects(convert_numeric=True);
data['urbanrate'] = data['urbanrate'].convert_objects(convert_numeric=True);

data['urbanrate']=pd.cut(data['urbanrate'],[0,10,20,30,40,50,60,70,80,90,100]);
data['relectricperperson']=pd.cut(data['relectricperperson'],[0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]);
data['oilperperson']=pd.cut(data['oilperperson'],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]);


print(" *** Oil consumption per person *** \n")
c1 = data['oilperperson'].value_counts(sort=False);
print (c1)

print("Oil consumption per person(Normalized)\n")
p1 = data['oilperperson'].value_counts(sort=False, normalize = True);
print (p1)

print(" *** Electicity consumption per person ***\n ")
c2 = data['relectricperperson'].value_counts(sort=False);
print (c2)

print("Electicity consumption per person(Normalized)\n")
p2 = data['relectricperperson'].value_counts(sort=False, normalize = True);
print (p2)

print(" *** Urban Rate ***\n")
c3 = data['urbanrate'].value_counts(sort=False);
print (c3)

print("Urban Rate(Normalized)\n")
p3 = data['urbanrate'].value_counts(sort=False, normalize = True);
print (p3)


