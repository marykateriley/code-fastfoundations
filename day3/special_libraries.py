import sys


def using_math_library():
    import math
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:  # real
        x1 = (-b + math.sqrt(discriminant)) / 2 / a
        x2 = (-b - math.sqrt(discriminant)) / 2 / a
    else:  # imaginary
        x1 = complex(-b / 2 / a, math.sqrt(-discriminant) / 2 / a)
        x2 = complex(-b / 2 / a, -math.sqrt(-discriminant) / 2 / a)
    print(f"{x1 = }")
    print(f"{x2 = }")


def using_cmath_library():
    import cmath
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    discriminant = b ** 2 - 4 * a * c
    x1 = (-b + cmath.sqrt(discriminant)) / 2 / a
    x2 = (-b - cmath.sqrt(discriminant)) / 2 / a
    print(f"{x1 = }")
    print(f"{x2 = }")

#TASK
def al_kashi(): ## WRONG ?? CEHCK SOLUTIONS
    import cmath
    a = float(input("a: "))
    b = float(input("b: "))
    y = float(input("y: "))
    c = cmath.sqrt(a ** 2 + b ** 2 - (2 * a * b * cmath.cos(y)))
    print(f"{c =}")
#al_kashi()

def using_shuffle():
    import random
    my_list = list(range(127, 349))
    random.shuffle(my_list) # do not assign my_list to a new variable, as it will just return None
    print(f"{my_list = }")
    another_list = ['A', 'B', 'C']
    for _ in range(10): # _ is a way of creating a variable that you don't need to use
        print(f"{random.choice(another_list) = }")
    print(f"{random.choices(another_list, k=10) = }")
#using_shuffle()


def using_datetime_library():
    import datetime
    from zoneinfo import ZoneInfo # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    print(datetime.datetime(2022, 4, 28, 11, 14, 32, 13432, ZoneInfo('Asia/Ashkhabad'))) # datetime
    print(datetime.date(2022, 4, 28)) # date
    print(datetime.time(14, 33, 7, 23422, ZoneInfo('Asia/Baku'))) # time
    datetime1 = datetime.datetime(2013, 9, 7, 8, 39, 58, 27389, ZoneInfo('Australia/Lindeman'))
    datetime2 = datetime.datetime.now(ZoneInfo('Europe/Kyiv'))
    print(f"{datetime2 - datetime1 = }") # timedelta
    print(f"{datetime.date.today() = }")

#TASK
def process_fao_data():
    import csv
    import statistics
    ghana_data = dict()
    ivory_coast_data = dict()
    with open("FAOSTAT_data_7-23-2022.csv") as f:
        fao_reader = csv.reader(f)
        for row in fao_reader:  # row is a list
            data = row[11]
            year = row[9]
            field = row[5]
            if row[3] == 'Ghana':
                if year not in ghana_data:
                    ghana_data[year] = dict()
                # the dictionary now exists for this year
                # ivory_coast_data[year][field] = data
                if field == 'Area harvested':
                    ghana_data[year]['Area harvested'] = data
                elif field == 'Yield':
                    ghana_data[year]['Yield'] = data
                elif field == 'Production':
                    ghana_data[year]['Production'] = data
            elif row[3] == "Côte d'Ivoire":
                if year not in ivory_coast_data:
                    ivory_coast_data[year] = dict()
                # the dictionary now exists for this year
                # ivory_coast_data[year][field] = data
                if field == 'Area harvested':
                    ivory_coast_data[year]['Area harvested'] = data
                elif field == 'Yield':
                    ivory_coast_data[year]['Yield'] = data
                elif field == 'Production':
                    ivory_coast_data[year]['Production'] = data
    # print(ivory_coast_data)
    # print(ghana_data)
    years = list()
    production_ivory_coast = list()
    with open('ivory_coast.txt', 'w') as f:
        for year, data in ivory_coast_data.items():
            print(f"{year}\t{data['Area harvested']}\t{data['Yield']}\t{data['Production']}", file=f)
            years.append(int(year))
            production_ivory_coast.append(int(data['Production']))

    production_ghana = list()
    with open('ghana.txt', 'w') as f:
        for year, data in ghana_data.items():
            print(f"{year}\t{data['Area harvested']}\t{data['Yield']}\t{data['Production']}", file=f)
            production_ghana.append(int(data['Production']))

    # linear regression
    slope_ic, intercept_ic = statistics.linear_regression(years, production_ivory_coast)
    slope_g, intercept_g = statistics.linear_regression(years, production_ghana)
    print(f"Ivory Coast: production = {slope_ic}*year + {intercept_ic}")
    print(f"Ghana      : production = {slope_g}* year  +  {intercept_g}")

    # predictions
    print(f"2030 Ivory Coast production: {slope_ic * 2030 + intercept_ic:>20,.4f} tonnes")
    print(f"2030 Ghana production:       {slope_g * 2030 + intercept_g:>20,.4f} tonnes")
process_fao_data()



def main():
    # using_math_library()
    # using_cmath_library()
    # using_datetime_library()
    return 0


if __name__ == '__main__':
    sys.exit(main())
