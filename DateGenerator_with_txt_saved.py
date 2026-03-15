# Version beta.2
## check with google colab


import pandas as pd
from datetime import datetime
import calendar

# Function get the last day of month
def Get_last_day_of_month(year, month):
    return calendar.monthrange(year, month)[1]

# Days in french dictionnary
days_french = {
    0: ('Monday', 1),
    1: ('Tuesday', 2),
    2: ('Wednesday', 3),
    3: ('Thursday', 4),
    4: ('Friday', 5),
    5: ('Saturday', 6),
}


# Days in french dictionnary
days_french = {
    0: ('Lundi', 1),
    1: ('Mardi', 2),
    2: ('Mercredi', 3),
    3: ('Jeudi', 4),
    4: ('Vendredi', 5),
    5: ('Samedi', 6),
}

# Function who translate the months in french
def months_frs_translate(code):
    mois = {
        '01': 'Janvier',
        '02': 'Février',
        '03': 'Mars',
        '04': 'Avril',
        '05': 'Mai',
        '06': 'Juin',
        '07': 'Juillet',
        '08': 'Août',
        '09': 'Septembre',
        '10': 'Octobre',
        '11': 'Novembre',
        '12': 'Décembre'
    }
    return mois[code]


# Days in malagasy dictionnary
days_malagasy = {
    0: ('Alatsinainy', 1),
    1: ('Talata', 2),
    2: ('Alarobia', 3),
    3: ('Alakamisy', 4),
    4: ('Zoma', 5),
    5: ('Sabotsy', 6),
}

# Function who translate the months in malagasy
def months_mlg_translate(kaody):
    volana = {
        '01': 'Janoary',
        '02': 'Febroary',
        '03': 'Martsa',
        '04': 'Aprily',
        '05': 'May',
        '06': 'Jona',
        '07': 'Jolay',
        '08': 'Aogositra',
        '09': 'Septambra',
        '10': 'Oktobra',
        '11': 'Novambra',
        '12': 'Desambra'
    }
    return volana[kaody]

# Function to get a integer between the minimum value and the maximum value
def Acquire_number_value(name,begin_end, val_min =0, val_max=0):
    while True:
        try:
            number_enter = int(input(f"Enter the {begin_end} {name} : "))
            if number_enter in range(val_min, val_max + 1):
                return number_enter
            else:
                print(f"SORRY, but '{number_enter}' is not in between of {val_min} and {val_max}.")
        except ValueError:
            print(f"Please enter an integer value between {val_min} and {val_max} (natural integer number)!!")


# To separe the weeks by lines
def Weeks_separation(day_number, file):
    if day_number in (1, 7):  #same as: day_name in ("Alatsinainy"; "Lundi"):
        with open(file, "a") as f:
            f.write(" \n \n")
 
    else:
        pass


# Function to save the results in a txt file
def Save_result():
    while True:
        try:
            print("\n \n \n")
            result = Acquire_number_value('6-> Fahano ny ondriko_MLG \n 7-> Exit \n \n','\n 1-> Tournage Mofonaina \n 2-> Traduction_FRS \n 3-> Traduction_ENG \n 4-> Mofonaina_FRS \n 5-> Mofonaina_ANG \n',1,7)
    
            if result in {2, 3}:
                # Generate the list of days for Lundi to Samedi
                language_days = [(date.strftime('%-d') + ' ' + months_frs_translate(date.strftime('%m')) + ' ' + date.strftime('%Y'), days_french[date.weekday()]) for date in date_range if date.weekday() < 6]
            elif result == 7:
                print("See you next time!! GOD bless you!! ......")
                break
            else:
                # Generate the list of days for Alatsinainy to Sabosty
                language_days = [(date.strftime('%-d') + ' ' + months_mlg_translate(date.strftime('%m')) + ' ' + date.strftime('%Y'), days_malagasy[date.weekday()]) for date in date_range if date.weekday() < 6]
    
            print("\n \n There are: \n \n\n ")



                    ###################################################################
                    ##### modifify some of them to make your date generator ###########
                    ##################################################################

            # Save the final results
            for date, (day_name, day_number) in language_days:
                if result == 1:

                    # output here example: 2 Mardi 17 March 2026
                    with open("1_Tournage Mofonaina_date.txt", "a") as f:
                        f.write(f"{day_number} {day_name} {date}\n")
                        Weeks_separation(day_number, "1_Tournage Mofonaina_date.txt")

                # output here example: 2 Mardi 17 March 2026_FRS
                elif result == 2:
                    with open("2_Traduction_FRS_date.txt", "a") as f:
                        f.write(f"{day_number} {day_name} {date}_FRS\n")
                        Weeks_separation(day_number, "2_Traduction_FRS_date.txt")

                # output here example: 8 Mardi 17 March 2026_ENG
                elif result == 3:
                    with open("3_Traduction_ENG_date.txt", "a") as f:
                        f.write(f"{day_number + 6} {day_name} {date}_ENG\n")
                        Weeks_separation(day_number, "3_Traduction_ENG_date.txt")

                # output here example: MOFONAINA Talata 17 Martsa 2026_Français
                elif result == 4:
                    with open("4_Mofonaina_FRS_date.txt", "a") as f:
                        f.write(f"MOFONAINA {day_number} {day_name} {date}_Français\n")
                        Weeks_separation(day_number, "4_Mofonaina_FRS_date.txt")

                # output here example: MOFONAINA Talata 17 Martsa 2026_English
                elif result == 5:
                    with open("5_Mofonaina_ANG_date.txt", "a") as f:
                        f.write(f"MOFONAINA {day_number} {day_name} {date}_English\n")
                        Weeks_separation(day_number, "5_Mofonaina_ANG_date.txt")

                # output here example: FAHANO NY ONDRIKELIKO!_Talata 17 Martsa 2026
                elif result == 6:
                    with open("6_Fahano ny ondriko_MLG_date.txt", "a") as f:
                        f.write(f"FAHANO NY ONDRIKELIKO!_{day_number} {day_name} {date}\n")
                        Weeks_separation(day_number, "6_Fahano ny ondriko_MLG_date.txt")
                
            print("File saved.")
                

        except ValueError:
            print("Please enter an integer value between 1 and 6 !!...")


print("STARTING : \n")
year_start = Acquire_number_value('year','START',2020,2200)
month_start = Acquire_number_value('month','START',1,12)

last_day_in_month_S = Get_last_day_of_month(year_start, month_start)
day_start = Acquire_number_value('day','START',1, last_day_in_month_S)
print(f"Done, we start in {year_start} / {month_start} / {day_start} (Y/M/D)")


print("\n \n ENDING :\n")
year_end = Acquire_number_value('year','END',year_start,2200)
month_end = Acquire_number_value('month','END',month_start,12)

last_day_in_month_E = Get_last_day_of_month(year_end, month_end)

# Some check if the month end is same as month start
if month_end == month_start:
    day_end = Acquire_number_value('day','END',day_start,last_day_in_month_E)
else:
    day_end = Acquire_number_value('day','END',1,last_day_in_month_E)
print(f"Done, we stop in {year_end} / {month_end} / {day_end} (Y/M/D) \n \n")

start = datetime(year_start, month_start, day_start)  
end = datetime(year_end, month_end, day_end)

# Create a date range for the year start
date_range = pd.date_range(start, end)

Save_result()

def __main__():
    print("Hello World")



if __name__ == '__main__':
    pass





### GOD IS GOOD, ALL THE TIME; AND ALL THE TIME, GOD IS GOOD  ###
            ### Régie Vidéo Zoara Fanantenana Ambohipo 2026 ###
