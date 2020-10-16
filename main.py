import pandas as pd
import os, csv, json, time
from progressBarCustom import ProgressBarCustom
from processData import Data

csvFile = './intel_gen_2.csv'
jsonFile = './intel_gen_2.json'

def removeFile():
    index = 2
    for i in range(9):
        try:
            # os.remove(jsonFile)
            os.remove(f"./intel_gen_{index}.csv")
        except Exception as e:
            print(e)
        index+=1
        


def csvToJson():
    # try:
    #     os.remove(f"./intel_gen_2.json")
    # except Exception as e:
    #     print(e)\
    index = 2
    for i in range(9):
        try:
            df = pd.read_csv (f'./edit/intel_gen_{index}.csv')
            dfJson = df.to_json(f'./jsonClean/intel_gen_{index}.json', orient='table')
        except Exception as e:
            print(e)
        index+=1
    # jsonClean = JSON.parse(JSON.stringify(arr).replace(/\s(?=\w+":)/g, ""));
    
def csvToJson2():
    csvfile = open(csvFile, 'r')
    jsonfile = open(jsonFile, 'w')

    fieldnames = ("FirstName","LastName","IDNumber","Message")
    reader = csv.DictReader( csvfile)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

def csvEditProcess():
    with open('./edit/intel_gen_2.csv') as fh:
        header = [h.strip() for h in fh.next().split(',')]
        reader = csv.DictReader(fh, fieldnames=header)
        df = pd(reader)
        df.to_csv(csvFile)
        
def lower_keys(obj):
    if isinstance(obj, str):
        return obj.lower()
    elif isinstance(obj, list):
        return [lower_keys(elem) for elem in obj]
    elif isinstance(obj, dict):
        return {key.lower(): lower_keys(value) for key, value in obj.items()}
    else:
        return obj
    
def removeFile():
    try:
        os.remove('./jsonClean/intel_gen_2.json')
        # os.remove('./intel_gen_2.json')
        # os.remove('./intel_gen_2edit.json')
    except Exception as e:
        print(e)
# aList=[]
# with open(self.filename, 'r') as f:
#     reader = csv.reader(f, skipinitialspace=False,delimiter=',', quoting=csv.QUOTE_NONE)
#     for row in reader:
#         aList.append(row)
#     return(aList)
removeFile()
time.sleep(1)
csvToJson()
# df = pd.read_csv('./edit/intel_gen_2.csv')
# lower_keys(df).to_json(jsonFile)
# dfJs = pd.read_json('./intel_gen_2.json')
# lower_keys(dfJs).to_json('./intel_gen_2edit.json')
# print(lower_keys(dfJs))
# lower_keys(df).to_csv(csvFile)
# csvEditProcess()
# removeFile()
# dt = Data()
# dt.getCompleteData()
# csvToJson2()




# print(len(dfs))
# print(dfs[3]) #! 2nd gen
# print(dfs[9]) #! 3rd gen
# print(dfs[2]) #! 4th gen
#skip #! 5rd gen
# print(dfs[2]) #! 6th gen
# print(dfs[1]) #! 7th gen
# print(dfs[1]) #! 8th gen
# print(dfs[4]) #! 9th gen
# print(dfs[1]) #! 10th gen
    
# print(dfs[0])