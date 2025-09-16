from math import *
v1 = int(input("Скорость первой черепахи "))
v2 = int(input("Скорость второй черепахи "))
g = int(input("фора первой черепахи "))
t = g/(v2-v1)
hours = int(t)
minuts = (t - int(t))*60
minn = int(minuts)
sek = (minuts - minn)*60
sekk = floor(sek)
print(hours)
print(minn)
print(sekk)