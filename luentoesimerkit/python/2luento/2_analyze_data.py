import pandas as pd
from collections import Counter
from datetime import datetime
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Lasketaan kirjaston lainausdatasta tilastollisia 
# tunnuslukuja. Tämä on osa data-analyysivaihetta.
# talletetaan lasketut tunnusluvut json-tiedostoon
# josta sen sisältö voidaan lukea ja luoda 
# taulu PDF-tiedostoon.

def prepare_data(file_path):
    """
    Valmistelee syötteen DataFrame-muotoon.
    """
    df = pd.read_csv(file_path, sep=',')
    return df

def get_most_popular_category(df):
    """
    Laskee suosituimman kirjakategorian annetulla ajanjaksolla.
    """
    category_counts = df["bookCat"].value_counts()
    return category_counts.idxmax()


##Käytä perustietotyyppejä palautusarvoissa.
def get_new_loans_count(df, start_date_str, end_date_str):
    """
    Laskee uusien lainojen määrän annetulla ajanjaksolla.
    """
    print(f"Loans between: {start_date_str} and {end_date_str}")
    start_date=pd.to_datetime(start_date_str)
    end_date=pd.to_datetime(end_date_str)

    mask = (pd.to_datetime(df["loanDate"]) >= start_date) & (pd.to_datetime(df["loanDate"]) <= pd.to_datetime(end_date))
    return int(mask.sum())

def get_late_loans_count(df):
    """
    Laskee myöhästyneiden lainojen määrän.
    """
    late_loans = pd.to_datetime(df["returnDate"]) > (pd.to_datetime(df["loanDate"]) + pd.Timedelta(days=30)) 
    return int(late_loans.sum())

def get_lost_books_count(df):
    """
    Laskee hukassa olevien kirjojen määrän. Kirja on 
    hukassa, kun sen paluupäivämäärä on tyhjä ja kirja on ollut lainassa yli 
    60 pv.
    """
    lost_books = ((datetime.now() - pd.to_datetime(df["loanDate"])).dt.days>60) & (df["returnDate"].isna())
    return int(lost_books.sum())

def get_average_loan_duration(df):
    """
    Laskee lainojen keskimääräisen keston päivinä.
    """
    loan_durations = (pd.to_datetime(df["returnDate"]) - pd.to_datetime(df["loanDate"])).dt.days
    loan_durations = loan_durations.dropna()
    return float(loan_durations.mean())

def get_loan_change_percentage(previous_loans, current_loans):
    """
    Laskee lainauksen prosentuaalisen muutoksen.
    """
    print(f"Current loans {current_loans} vs previous loans {previous_loans}")
    if previous_loans == 0:
        return float('inf') if current_loans > 0 else 0
    return float((current_loans - previous_loans) / previous_loans) * 100

def minusOneMonth(start_date_str):
    start_date = pd.to_datetime(start_date_str, format='%Y-%m-%d')
    
    # Vähennetään yksi kuukausi, mutta ei aseteta päivää kuukauden ensimmäiseksi
    last_month = start_date - pd.DateOffset(months=1)
    
    # Palautetaan päivämäärä merkkijonona
    return last_month.strftime('%Y-%m-%d')


def calculate_library_metrics(file_path, start_date_str, end_date_str):
    """
    Laskee kaikki tunnusluvut annetun datan perusteella.
    """
    df = prepare_data(file_path)
    most_popular_category = get_most_popular_category(df)
    new_loans_count = get_new_loans_count(df, start_date_str, end_date_str)
    print("Uusia lainoja ", new_loans_count)
    late_loans_count = get_late_loans_count(df)
    print("Myöhästyneitä lainoja ", late_loans_count)
    lost_books_count = get_lost_books_count(df)
    print("Hukattuja lainoja ", lost_books_count)
    average_loan_duration = get_average_loan_duration(df)
    print("Keskimääräinen laina-aika ", average_loan_duration)
    last_month_start_str=minusOneMonth(start_date_str)
    last_month_end_str = minusOneMonth(end_date_str)
    previous_loans_count=get_new_loans_count(df, last_month_start_str, last_month_end_str)
    loan_change_percentage = get_loan_change_percentage(previous_loans_count, new_loans_count)
    print("Muutos lainamäärissä ", loan_change_percentage)

    ## Käytä tässä perustietotyyppejä. (string, float, int)
    return {
        "period": f"{start_date_str} - {end_date_str}",
        "most_popular_book_category": most_popular_category,
        "loan_change_percent": loan_change_percentage,
        "new_loans_qty": new_loans_count,
        "late_loans_qty": late_loans_count,
        "lost_books_qty": lost_books_count,
        "average_loan_duration_days": average_loan_duration
    }

def saveResultToFile(metrics):
    with open("metrics.json", "w") as file:
        json.dump(metrics, file, indent=4)

# Esimerkki edellisen periodin lainauksista
previous_loans_count = 12
file_path="librarydata.csv"
start_date_str="2024-01-01"
end_date_str="2024-01-31"

# Lasketaan tunnusluvut
metrics = calculate_library_metrics(file_path, start_date_str, end_date_str)
saveResultToFile(metrics)

