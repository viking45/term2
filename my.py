import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame()
csv_file = "Covid cases in India.csv"


def made_by():
    """Project made by: Parth"""


def clear():
    for x in range(65):
        print()


def introduction():
    msg = 'Hello there'
    print(msg)
    wait = input('Press any key to continue.....')


def data_analysis_menu():
    df = pd.read_csv(csv_file)
    df1 = pd.DataFrame()
    while True:
        clear()
        print("1. Show whole dataframe\n")
        print("2. Show Columns\n")
        print("3. Show top rows\n")
        print("4. Show bottom rows\n")
        print("5. Show specific column\n")
        print("6. Show summary of dataframe\n")
        ch = int(input("Enter your choice"))
        if ch == 1:
            print(df)
            wait = input()
        if ch == 2:
            print(df.columns)
            wait = input()

        if ch == 3:
            n = int(input('Number of rows to be displayed'))
            print(df.head(n))
            wait = input()
        if ch == 4:
            n = int(input('umber of Rows to be displayed'))
            print(df.tail(n))
            wait = input()
        if ch == 5:
            print(df.columns)
            n = input('Name of column')
            print(df[n])
            wait = input()
        if ch == 6:
            print(df.describe())
            print("\n\n\nPress any key to continue....")
            wait = input()


def graph_menu():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\nGRAPH MENU ')
        print('_' * 100)
        print('1.  State vs Total Cases\n')
        print('2.  State vs Active Cases\n')
        print('3.  State vs Recovered Cases\n')
        print('4.  Exit (Move to main menu)\n')
        ch = int(input('Enter your choice:'))
        if ch == 1:
            x = df['Name of State / UT']
            y = df['Total Confirmed cases']
            plt.xticks(rotation='vertical')
            plt.xlabel('Name of State')
            plt.ylabel('No. of Total Cases')
            plt.title('State vs Number of Total cases in India')
            plt.grid(True)
            plt.plot(x, y)
            plt.show()

        if ch == 2:
            x = df['Name of State / UT']
            y = df['Active']
            plt.xticks(rotation='vertical')
            plt.xlabel('Name of State')
            plt.ylabel('No. of Active Cases')
            plt.title('State vs Number of Active cases in India')
            plt.grid(True)
            plt.plot(x, y)
            plt.show()

        if ch == 3:
            x = df['Name of State / UT']
            y = df['Cured/Discharged/Migrated']
            plt.xticks(rotation='vertical')
            plt.xlabel('Name of State')
            plt.ylabel('No. of Cases')
            plt.title('State vs Number of Recovered cases in India')
            plt.grid(True)
            plt.plot(x, y)
            plt.show()

        if ch == 4:
            break


def main_menu():
    clear()
    introduction()
    while True:
        clear()
        print('MAIN MENU ')
        print('_'*100)
        print()
        print('1.  Data Analysis Menu\n')
        print('2.  Graph Menu\n')
        print('3.  Exit\n')
        choice = int(input('Enter your choice :'))
        if choice == 1:
            data_analysis_menu()
            wait = input()
        if choice == 2:
            graph_menu()
            wait = input()
        if choice == 3:
            break


main_menu()
