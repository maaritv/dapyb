import pandas as pd
from collections import Counter
from datetime import datetime
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta


def prepare_data(file_path):
    """
    Valmistelee syötteen DataFrame-muotoon.
    """
    df = pd.read_csv(file_path, sep=';')
    return df

def saveResultToFile(metrics):
    with open("metrics.json", "w") as file:
        json.dump(metrics, file, indent=4)

def calculateAverage(df, month_name):
    print(month_name)
    monthly_temperatures = pd.to_numeric(df[month_name])
    #print(monthly_temperatures)
    return float(monthly_temperatures.mean())

def calculateStandardError(df, month_name):
    #monthly_temperatures = pd.to_numeric(df[month])
    monthly_temperatures = df[month_name]
    return float(monthly_temperatures.std())

def findMax(df, month_name):
    #monthly_temperatures = pd.to_numeric(df[month])
    monthly_temperatures = df[month_name]
    return float(monthly_temperatures.max())



def calculate_temperature_metrics(file_path):
    """
    Laskee kaikki tunnusluvut annetun datan perusteella.
    """
    df = prepare_data(file_path)
    #print("Dataframe", df.head(), df.sum())

    column_names=list(df.columns)
    json_structure=[]
        
    for i in range(0, len(column_names)):
        column_data = df.iloc[:, i]
        column_name=column_names[i]
        print(f"Sarake {column_name}:\n{column_data}\n")
        mean = calculateAverage(df,column_name)
        stderr=calculateStandardError(df,column_name)
        maxval=findMax(df,column_name)
        json = {
            "month": column_name,
            "mean": mean,
            "stderr": stderr,
            "max": maxval,
        }
        json_structure.append(json)
    return json_structure
    

def saveResultToFile(metrics):
    with open("metrics.json", "w") as file:
        json.dump(metrics, file, indent=4)

# Esimerkki edellisen periodin lainauksista
file_path="temperaturedata.csv"

# Lasketaan tunnusluvut
metrics = calculate_temperature_metrics(file_path)
saveResultToFile(metrics)

