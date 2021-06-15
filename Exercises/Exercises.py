import random
import statistics
random.seed(0)
salaries = [round(random.random()*1000000, -3)for _ in range(100)]

# print(salaries)
x = statistics.mean(salaries)
print("mean is :", x)
y = statistics.median(salaries)
print("median is :", y)
z = statistics.mode(salaries)
print("mode is :", z)
a = statistics.stdev(salaries)
print("std deviation is :", a)
j = [5, 10, 15]
k = statistics.stdev(j)
print("std dev is:", k)
b = statistics.variance(salaries)
print("variance is:", b)
e = range(j)
for n in e:
    print("range is:", n)
