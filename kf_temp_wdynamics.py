import numpy as np
import matplotlib.pyplot as plt

#centralized KF to estimate temp, with process noise, temp increasing

q = 0.15 #process noise variance
sd = 0.1 #standard deviation of measurements
true_temps = [50.505, 50.994, 51.493, 52.001, 52.506, 52.998, 53.521, 54.005, 54.5, 54.997]
measurements = [50.486, 50.963, 51.597, 52.001, 52.518, 53.05, 53.438, 53.858, 54.465, 55.114]

#initialize
x = 10 #guess for temp
estimate_error = 100 
P = estimate_error**2 #variance of estimate

#for plotting:
estimates = []
kalman_gains = []
variance = []

#iterate
for i in range(len(measurements)):
    #predict
    P = P + q

    #measure
    z = measurements[i]
    r = sd**2

    #update
    k = P/(P+r)
    x = x + k*(z-x)
    P = (1-k)*P

    #for plotting:
    estimates.append(x)
    kalman_gains.append(k)
    variance.append(P)

#plotting
xaxis = list(range(1,11))
#plt.plot(kalman_gains, label = "kalman gain")
ci = np.sqrt(variance)
plt.plot(xaxis, estimates, label = "estimates")
plt.plot(xaxis, measurements, label = "measurements")
plt.plot(xaxis, true_temps, label = "true temps")
plt.fill_between(xaxis, estimates - ci, estimates + ci, color = "b", alpha = 0.1)
plt.legend() 
plt.show()