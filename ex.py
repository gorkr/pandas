from pandas import Series,DataFrame
import pandas as pd
import xlrd

path = "1.xlsx"
xls = pd.ExcelFile("1.xlsx")
f1 = DataFrame(pd.read_excel("1.xlsx"))

num = 1

f2 = DataFrame()


result=[]

book = xlrd.open_workbook("1.xlsx")
for sheet in book.sheets():
    df = pd.read_excel("1.xlsx", sheet.name)
    data = pd.DataFrame(df)

    try:
        #print(data.ix[:,[sheet.name,"Unnamed: 10"]])
        if(num in [2,19]):
            f4=pd.DataFrame(data.iloc[:, [0, 11]])
        elif(num in [3]):
            f3=data.iloc[:, [0, 8]]
            f4=pd.DataFrame(f3)
        elif (num in [10]):
            f3=data.iloc[:, [0, 6]]
            f4 = pd.DataFrame(f3)
        elif(num in [5]):
            f3=data.iloc[:, [0, 4]]
            f4 = pd.DataFrame(f3)
        elif(num <= 11 and num!=8 and num!=4):
            f3=data.iloc[:, [0, 9]]
            f4 = pd.DataFrame(f3)
        else:
            f3=data.iloc[:,[0,10]]
            f4 = pd.DataFrame(f3)
        f4.columns=["country",sheet.name]
        f4.drop(labels=None,axis=0, index=0, columns=None, inplace=True)
    except:
        print("None")

    num+=1
    if(num!=2):
        result.append(f4)


for i in result[:-1]:

    f4 = pd.merge(f4,i,on="country")


#print(f4)

json_data = f4.to_json(orient='index')

print(json_data)