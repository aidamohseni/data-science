# this is to test how we can import a csv file
# written by aida.science
import pandas


def get_input():
    print(
        "Please Choose a method to import your CSV file.\n Please enter ""csv"" to use csv library and ""numpy"" to use it.\n")
    choice = input()
    checkinput(choice.lower())


def get_source_type():
    temp= True
    while temp:
        choice = input("if you want to load data from web please write ""url"" else please write""local""\n").lower()
        if choice != "local"  and choice!="url":
            temp == True
        else: temp = False
    return choice


def import_csv():
    import urllib.request as urllib2
    import csv
    import codecs
    import pandas as pd

    print("runnig csv import...\n")
    source_type = get_source_type()
    if source_type == "url":
        url = 'https://raw.githubusercontent.com/aidascience/datasets/main/iris.csv'
        ifile = urllib2.urlopen(url)
        cr = csv.reader(codecs.iterdecode(ifile, 'utf-8'),delimiter=',')
        array_result = []
        for row in cr:
            array_result.append(row)
        print(array_result)
        print("###############################")
        df = pd.DataFrame(array_result[1:], columns= array_result[0])
        print(df.head(5))



def import_numpy():
    print("runnig numpy import...\n")
    source_type = get_source_type().lower()


def checkinput(input_choice):
    if input_choice == "csv":
        import_csv()
    elif input_choice == "numpy":
        import_numpy()
    else:
        get_input()


if __name__ == "__main__":
    get_input()





