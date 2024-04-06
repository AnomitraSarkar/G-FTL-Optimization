import csv
from tabulate import tabulate
import matplotlib.pyplot as plt

def read_csvfile(filename):
    with open(filename, "r") as f:
        csv_reader = csv.reader(f)
        allrec = []
        for i in csv_reader:
            allrec.append(i)
        return allrec
    
def plot_data_raw(data):
    x = []    
    y = []
    for i in data[1:]:
        x.append(float(i[1]))   
        y.append(float(i[2]))  
    plt.figure(figsize=(10,10))
    plt.scatter(x,y,label='Data Pnts') 
    x_mean = sum(x)/len(x)
    y_mean = sum(y)/len(y)
    plt.plot(
        [min(x),x_mean,max(x)],
        [min(y),y_mean,max(y)],'r'
        ,label='Regr Line', linewidth=2
    )
    # plt.scatter
    plt.ylabel('Height')
    plt.xlabel('Weight')
    plt.title("Height vs Weight General Model")
    plt.legend()
    plt.xlim(min(x)-1,max(x)+1)
    plt.ylim(min(y)-2,max(y)+2)
    plt.show()
    print("Expected mean(X,Y):", x_mean,y_mean)
    print("Regression mean on Current values(X,Y):", (max(x)+min(x))/2,(max(y)+min(y))/2)
    return  (max(x)+min(x))/2,(max(y)+min(y))/2
    
  
def consoletable(data, MODE = 0):
    if MODE == 0:
        print(tabulate(data[1:],data[0],"fancy_grid"))
    else:
        return tabulate(data[1:],data[0],"fancy_grid")
    
    

if __name__ == "__main__":
    table = read_csvfile("SOCR-HeightWeight.csv")
    # consoletable(table)
    plot_data_raw(table)