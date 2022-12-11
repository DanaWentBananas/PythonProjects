import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import functions as use


#Reading the file
# ***THE INPUT HAS TO BE IN CSV FORMAT AND HAS TO BE LOCATED IN THE DATA FOLDER***
f = use.readFile()

#Answering the questions
print(f.columns)
while True:
    print("Enter the name of the column that contains the date of each sale")
    date = input()
    try:
        f[date]
    except:
        print("column not found. Try again")
    else:
        break

print(f.columns)
while True:
    try:
        print("Enter the name of the column that contains the sales")
        sales = input()
        f[sales]
    except:
        print("column not found. Try again")
    else:
        break

print(f.columns)
while True:
    try:
        print("Enter the name of the column that contains the product/category that was sold")
        product = input()
        f[product]
    except:
        print("column not found. Try again")
    else:
        break

print(f.columns)
while True:
    try:
        print("Enter the name of the column that contains the name of the buyer")
        buyer= input()
    except:
        print("column not found. Try again")
    else:
        break

print(f.columns)
while True:
    try:
        print("Enter the name of the column that contains the location of the buyer")
        location = input()
        f[location]
    except:
        print("column not found. Try again")
    else:
        break


while True:
    print("1. Sales by month")
    print("2. Top 10 products by sales")
    print("3. Top 10 countries by sales")
    print("4. Top 3 customers by amount of purchases")
    print("5. Exit")
    ans = input("Choose a number: ")

    if ans=="1":
        #Sales by month
        f[date] = pd.to_datetime(f[date]) #Convert to datetime
        f[date] = f[date].apply(use.convertDate)
        f[sales] = use.convertSales(f[sales])
        salesByMonth = f.groupby(date).sum()[sales].reset_index()

        plt.figure(figsize=(15,6))
        plt.plot(salesByMonth[date], salesByMonth[sales])
        plt.xticks(rotation='vertical',size=8)
        plt.show()

    elif ans=="2":
        #top 10 products
        f[sales] = use.convertSales(f[sales])
        productSales = f.groupby(product).sum()[sales].reset_index()
        productSales = productSales.sort_values(sales,ascending=False)
        print(productSales)
        plt.figure(figsize=(10,5))
        plt.pie(productSales[sales][:10], labels=productSales[product][:10], autopct='%.2f')
        plt.show()
    
    elif ans=="3":
        #top 10 countries
        f[sales] = use.convertSales(f[sales])
        countrySales = f.groupby(location).sum()[sales].reset_index()
        countrySales = countrySales.sort_values(sales,ascending=False)
        print(countrySales)
        plt.figure(figsize=(10,5))
        sns.barplot(data=countrySales[:10], x=location,y=sales)
        plt.xticks(rotation=20,size=8)
        plt.show()

    elif ans=="4":
        #top 3 customers
        customerCount = f[buyer].value_counts().reset_index()
        plt.figure(figsize=(10,5))
        sns.barplot(data=customerCount[:3], x="index",y=buyer).set(xlabel='Buyers', ylabel='Purchases count')
        plt.xticks(size=8)
        plt.show()
    
    elif ans=="5":
        break

    else:
        print("Try Again")