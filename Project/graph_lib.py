from matplotlib import pyplot as plt
import numpy as np

# temperature, humidity, pressure = []
#
# print(temperature)
# print(humidity)
# print(pressure)

def plot_graphs(temperature,humidity,pressure):
    avg = []
    x_temp = [i for i in range(len(temperature))]
    x_hum = [i for i in range(len(humidity))]
    x_pre = [i for i in range(len(pressure))]


    a_t,b_t,c_t = np.polyfit(x_temp,temperature,2)
    a_h,b_h,c_h = np.polyfit(x_hum,humidity,2)
    a_p,b_p,c_p = np.polyfit(x_pre,pressure,2)

    def quad(a,b,c,x):
        return a*x**2 + b*x + c

    quad_hum = quad(a_h,b_h,c_h,x_hum)
    quad_pre = quad(a_h,b_h,c_h,x_pre)

    xt_model = [min(x_temp),max(x_temp)]
    yt_model = quad(a_t,b_t,c_t,x_temp)
    xh_model = [min(x_hum),max(x_hum)]
    yh_model = quad(a_h,b_h,c_h,x_hum)
    xp_model = [min(x_pre),max(x_pre)]
    yp_model = quad(a_p,b_p,c_p,x_pre)

    plt.subplot(3,1,1)
    plt.plot(x_temp,temperature,color="blue")
    plt.plot(xt_model,yt_model, color = "green")

    plt.subplot(3,1,2)
    plt.plot(x_hum,humidity,color="blue")
    plt.plot(xh_model,yh_model, color = "green")

    plt.subplot(3,1,3)
    plt.plot(x_pre,pressure,color="blue")
    plt.plot(xp_model,yp_model, color = "green")
