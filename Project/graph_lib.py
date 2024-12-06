from matplotlib import pyplot as plt
import numpy as np

# temperature, humidity, pressure = []
#
# print(temperature)
# print(humidity)
# print(pressure)

# data = {
#     "temperature": [values],
#     "humidity": [values],
#     "pressure": [values],
# }

def moving_average(windowSize:int, x:list) -> list:
    x_smoothed = []
    for i in range(0,len(x)-windowSize):
        x_section = x[i:i+windowSize]
        x_average = sum(x_section)/windowSize
        x_smoothed.append(x_average)
    return x_smoothed

def quad(a, b, c, x):
    return a * x ** 2 + b * x + c

def plot_quad_model(value):
    x = [i for i in range(len(value))]
    a,b,c = np.polyfit(x,value,2)
    x_model = [min(x),max(x)]
    y_model = [quad(a,b,c,min(x)),quad(a,b,c,max(x))]
    plt.plot(x_model,y_model)
    return ("quadratic model plotted successfully")

def plot_avg(v1,v2):
    avg = []
    if len(v1)>len(v2):
        for i in range(len(v2)):
            avg.append((v1[i]+v2[i])/2)
    else:
        for i in range(len(v1)):
            avg.append((v1[i]+v2[i])/2)
    return avg


# mean, standard deviation, minimum, maximum, and median
def calc_statistics(values):
    stats = {
        "mean": np.mean(values),
        "std_dev": np.std(values),
        "min": np.min(values),
        "max": np.max(values),
        "median": np.median(values),
    }
    return stats


def plot_data(subplot,x:list,y:list, ylabel,yunits):
    subplot.plot(x,y,color = "#c7d9e5")
    subplot.set_title(ylabel)
    subplot.set_xlabel("Time (min)")
    subplot.set_ylabel(ylabel+yunits)
    subplot.legend()
    return("data plotted successfully")
