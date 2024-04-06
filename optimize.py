import matplotlib.pyplot as plt
import pandas as pd

def read_dataframe(filename):
    data = pd.read_csv(filename)
    return data

def data_parameters(filename):
    data = read_dataframe(filename)
    std_x = float(data.std()[1])
    std_y = float(data.std()[2])
    mean_x = float(data.mean()[1])
    mean_y = float(data.mean()[2])
    print("Model Parameters: ")
    print("Model Actual Standard Deviation:", std_x,std_y)
    print("Model Actual Mean:\t\t",mean_x,mean_y)
    return mean_x,mean_y,std_x,std_y
    
def define_range(param):
    # assuming parameters are mean1, mean2, std1, std2
    print("The Range should be u (+/-) 2s: ")
    x_range = (param[0] - 2*param[2], param[0] + 2*param[2])
    y_range = (param[1] - 2*param[3], param[1] + 2*param[3])
    return x_range,y_range
    
def plot_data_optimized(filename):
    table = read_dataframe(filename)
    x = table["Height(Inches)"]
    y = table["Weight(Pounds)"]
    print("original values:",x.shape, y.shape)
    range = define_range(data_parameters(filename))
    # filter x 
    new_table = table[(table["Height(Inches)"] > range[0][0]) & (table["Height(Inches)"] < range[0][1]) &
    (table["Weight(Pounds)"] > range[1][0]) & (table["Weight(Pounds)"] < range[1][1])]
    x_new = new_table["Height(Inches)"]
    y_new = new_table["Weight(Pounds)"]
    print("Filtered range:", x_new.shape, y_new.shape)
    plt.figure(figsize=(10,10))
    plt.scatter(x_new,y_new,label='Filtered Data Pnts')
    plt.plot(
        [x_new.min(),x_new.mean(),x_new.max()],
        [y_new.min(),y_new.mean(),y_new.max()],
        'r',label='Optimized Regr Line', linewidth=2
    )
    plt.xlim(x.min()-1, x.max()-1)
    plt.ylim(y.min()+2, y.max()+2)
    plt.ylabel('Height')
    plt.xlabel('Weight')
    plt.title("Height vs Weight Optimized Model")
    plt.legend()
    plt.show()
    print("Optimized Mean Found (X,Y):", (x_new.max() + x_new.min())/2,(y_new.max() + y_new.min())/2)
    return (x_new.max() + x_new.min())/2,(y_new.max() + y_new.min())/2
    
if __name__ == "__main__":
    plot_data_optimized("SOCR-HeightWeight.csv")