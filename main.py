import matplotlib.pyplot as plt
import numpy as np
from scipy import stats as st
'''
age = list(np.random.normal(10, 0.05, size=200))
speed = list(np.random.normal(100, 80, size=200))
'''
age = [5,7,8,7,2,17,2,9,4,11,12,9,6]
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
print(age)
print(speed)
plt.xlabel('age of car')
plt.ylabel('speed of Car')
slope, intercept, r, p, std_err = st.linregress(age, speed)


def model(x):
    return slope * x + intercept


new_speed = list(map(model, age))
print(r)
speed_predict = model(20)
print(speed_predict)
plt.scatter(20, speed_predict, color='red')
plt.scatter(age, speed)
plt.scatter(age, new_speed)
plt.show()
