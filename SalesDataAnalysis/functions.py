import pandas as pd

def convertDate(date):
    return date.strftime('%Y-%m')

def convertSales(sales):
    if not pd.api.types.is_numeric_dtype(sales):
        return sales.str.replace(',', '').astype(int)
    else:
        return sales

def readFile():
    while True:
        ans = input("Enter the csv file name that contains the sales information")
        try:
            f = pd.read_csv('./data/'+ans, encoding='Latin-1')
        except:
            print("Try again")
        else:
            print(f.head())
            ans = input("Is this your data? (y/n) ").lower()
            if ans=='y':
                break
            else:
                continue
    return f
