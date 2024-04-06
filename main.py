import normal
import optimize
import pyautogui as pag
import time
import matplotlib.pyplot as plt

CSV_FILE_NAME = "SOCR-HeightWeight.csv"

print("Printing Data into Console...")
time.sleep(1.25)
dataframe = normal.read_csvfile(CSV_FILE_NAME)

# deriving the model from normal methodology
print("\n-------------------GENERALIZED--------------------------")
normal.consoletable(dataframe)
time.sleep(1.25)
val_org = normal.plot_data_raw(dataframe) #original mean loaded

#deriving the model from optimized methodology 5% 
print("\n-------------------OPTIMIZED---------------------------")
time.sleep(1.25)
val_opt = optimize.plot_data_optimized(CSV_FILE_NAME)
actual_params = optimize.data_parameters(CSV_FILE_NAME)
val_actual = (actual_params[0], actual_params[1])

print("\n\n-------------------INFERENCE---------------------------")
time.sleep(1.25)
obv = normal.consoletable(
    [
        ["OBSERVATION","X","Y"],
        ["Actual",val_actual[0],val_actual[1]],
        ["Normal",val_org[0],val_org[1]],
        ["Optimized",val_opt[0],val_opt[1]]
    ], 1
    )
print(obv)

normal_to_actual_dev = (val_actual[0] - val_org[0],val_actual[1] - val_org[1])
optimized_to_actual_dev = (val_actual[0] - val_opt[0],val_opt[1] - val_opt[1])

perNTAdev = ((normal_to_actual_dev[0]/val_actual[0])*100,(normal_to_actual_dev[1]/val_actual[1])*100)
perOTAdev = ((optimized_to_actual_dev[0]/val_actual[0])*100,(optimized_to_actual_dev[1]/val_actual[1])*100)

optimzed_to_normal_dev  = (val_opt[0] - val_org[0],val_opt[1] - val_org[1])
perOTNdev = ((optimzed_to_normal_dev[0]/val_org[0])*100,(optimzed_to_normal_dev[1]/val_org[1])*100)

actual_dev_comparision = ((optimzed_to_normal_dev[0]/normal_to_actual_dev[0])*100,(optimzed_to_normal_dev[1]/normal_to_actual_dev[1])*100) 

print(actual_dev_comparision)

inf = normal.consoletable(
    [
        ["DEVIATIONS (%)","X","Y"],
        ["Normal To Actual",perNTAdev[0],perNTAdev[1]],
        ["Optimized to Actual",perOTAdev[0],perOTAdev[1]],
        ["Optimized to Normal",perOTNdev[0],perOTNdev[1]]
    ], 1
    )
print(inf)

res = normal.consoletable([
    ["RESULT","VALUE (%)"],
    ["X",actual_dev_comparision[0]],
    ["Y",actual_dev_comparision[1]],
],1)
print(res)
pag.confirm(f"{obv} \n {inf} \n {res}")

# graph the observations
plt.plot([10,20],[10*val_actual[0]/val_actual[0] +0.005,10*val_actual[1]/val_actual[1]+0.005],'+-',label='Actual Expretted Regression')
plt.plot([10,20],[10*val_opt[0]/val_actual[0],10*val_opt[1]/val_actual[1]],'+-',label='G-Optimized Regression')
plt.plot([10,20],[10*val_org[0]/val_actual[0],10*val_org[1]/val_actual[1]],'+-',label="General Linear Regression")
plt.legend()
plt.show()



