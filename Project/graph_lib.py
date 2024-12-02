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


def plot_data(data: dict, ylabel: str):
    for key, values in data.items():
        plt.plot(values, label=key)
    plt.title("Data Plot")
    plt.xlabel("Time")
    plt.ylabel(ylabel)
    plt.legend()
    return("data plotted successfully")
