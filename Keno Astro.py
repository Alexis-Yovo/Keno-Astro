import random
from datetime import datetime

def get_zodiac_sign(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Verseau"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Poissons"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Bélier"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taureau"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gémeaux"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Lion"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Vierge"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Balance"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpion"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittaire"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorne"

def generate_keno_grid(seed):
    random.seed(seed)
    numbers = random.sample(range(1, 71), 20)
    return numbers

current_date = datetime.now()
current_day = current_date.day
current_month = current_date.month

zodiac_sign = get_zodiac_sign(current_day, current_month)
print(f"Signe astrologique du jour: {zodiac_sign}")

birth_date = "04-01-2000"
birth_day, birth_month, birth_year = map(int, birth_date.split('-'))

seed = f"{birth_day}{birth_month}{birth_year}"

numbers = generate_keno_grid(seed)
print(f"Numéros: {numbers}")
