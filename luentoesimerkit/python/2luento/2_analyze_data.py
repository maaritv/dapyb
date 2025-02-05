import pandas as pd
from collections import Counter
from datetime import datetime
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
import csv

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

def get_most_popular_category(df, start_date_str, end_date_str):
    """
    Laskee suosituimman kirjakategorian koko aikavälillä.
    """
    start_date=pd.to_datetime(start_date_str)
    end_date=pd.to_datetime(end_date_str)

    period_loans = (pd.to_datetime(df["loanDate"]) >= start_date) & (pd.to_datetime(df["loanDate"]) <= end_date)

    filtered_df = df[period_loans]

    # Laske kategorioiden määrä
    category_counts = filtered_df["bookCat"].value_counts()
    print(category_counts)
    print(category_counts.idxmax())
    return category_counts.idxmax()


##Käytä perustietotyyppejä palautusarvoissa.
def get_new_loans_count(df, start_date_str, end_date_str):
    """
    Laskee uusien lainojen määrän annetulla ajanjaksolla.
    """
    print(f"Loans between: {start_date_str} and {end_date_str}")
    start_date=pd.to_datetime(start_date_str)
    end_date=pd.to_datetime(end_date_str)

    new_loans_mask = (pd.to_datetime(df["loanDate"]) >= start_date) & (pd.to_datetime(df["loanDate"]) <= end_date)
    filtered_df = df[new_loans_mask]
    return int(filtered_df["bookCat"].count())

def get_late_loans_count(df):
    """
    Laskee myöhästyneiden lainojen määrän.
    """
    late_loans_mask = pd.to_datetime(df["returnDate"]) > (pd.to_datetime(df["loanDate"]) + pd.Timedelta(days=31)) 
    #print(late_loans_mask)
    return int(late_loans_mask.sum())

def get_lost_books_count(df):
    """
    Laskee hukassa olevien kirjojen määrän. Kirja on 
    hukassa, kun sen paluupäivämäärä on tyhjä ja kirja on ollut lainassa yli 
    60 pv.
    """
    lost_books_mask = ((datetime.now() - pd.to_datetime(df["loanDate"])).dt.days>60) & (df["returnDate"].isna())
    return int(lost_books_mask.sum())

def get_average_loan_duration_of_month(df, start_date_str, end_date_str):
    """
    Laskee lainojen keskimääräisen keston päivinä.
    """
    start_date=pd.to_datetime(start_date_str)
    end_date=pd.to_datetime(end_date_str)

    new_loans_mask = (pd.to_datetime(df["loanDate"]) >= start_date) & (pd.to_datetime(df["loanDate"]) <= end_date)
    month_df = df[new_loans_mask]
    
    loan_durations_mask = (pd.to_datetime(month_df["returnDate"]) - pd.to_datetime(month_df["loanDate"])).dt.days
    print(loan_durations_mask)
    loan_durations_mask = loan_durations_mask.dropna()
    return float(loan_durations_mask.mean())

def get_change_percentage(previous_loans_count, current_loans_count):
    """
    Laskee lainauksen prosentuaalisen muutoksen.
    """
    print(f"Current loans {current_loans_count} vs previous loans {previous_loans_count}")
    if previous_loans_count == 0:
        return float('inf') if current_loans_count > 0 else 0
    return float((current_loans_count - previous_loans_count) / previous_loans_count) * 100

def minusOneMonth(start_date_str):
    start_date = pd.to_datetime(start_date_str, format='%Y-%m-%d')
    
    # Vähennetään yksi kuukausi, mutta ei aseteta päivää kuukauden ensimmäiseksi
    last_month = start_date - pd.DateOffset(months=1)
    
    # Palautetaan päivämäärä merkkijonona
    return last_month.strftime('%Y-%m-%d')

##Tunnuslukutaulukon sisältö.
def calculate_library_monthly_metrics(file_path, start_date_str, end_date_str):
    """
    Laskee kaikki tunnusluvut annetun datan perusteella.
    """
    df = prepare_data(file_path)
    most_popular_category = get_most_popular_category(df, start_date_str, end_date_str)
    new_loans_count = get_new_loans_count(df, start_date_str, end_date_str)
    print("Uusia lainoja ", new_loans_count)
    late_loans_count = get_late_loans_count(df)
    print("Myöhästyneitä lainoja ", late_loans_count)
    lost_books_count = get_lost_books_count(df)
    print("Hukattuja lainoja ", lost_books_count)
    average_loan_duration = get_average_loan_duration_of_month(df, start_date_str, end_date_str)
    print("Keskimääräinen laina-aika ", average_loan_duration)
    last_month_start_str=minusOneMonth(start_date_str)
    last_month_end_str = minusOneMonth(end_date_str)
    previous_loans_count=get_new_loans_count(df, last_month_start_str, last_month_end_str)
    loan_change_percentage = get_change_percentage(previous_loans_count, new_loans_count)
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


##Lasketaan, montako lainausta oli tehty eri kategorioiden kirjoille.
"""
   Aggregation column on sarake, jonka mukaan data librarydata.csv -tiedostossa
   halutaan ryhmitellä. Jos se on bookCat, SQL:nä se vastaisi:
   select bookCat, count(loanId) as value from librarydata GROUP BY bookCat 
"""
def create_category_data_for_barchart(data_file, aggregation_column):
    df = prepare_data(data_file)
    category_counts = df[aggregation_column].value_counts()
    #['Lastenkirjat', 'Dekkarit', 'Tietokirjat']
    categories = category_counts.index.tolist()
    #[3, 6,9]
    values = category_counts.values.tolist()
    #print("Kategoriat:", categories)
    #print("Lukumäärät:", values)
    """['Lastenkirjat', 'Dekkarit', 'Tietokirjat']
       [3, 6, 9] """
    datatable = [categories, values]
    df = pd.DataFrame(datatable)
    print(df)
    # Muutetaan sarakkeet riveiksi ja päinvastoin
    #transpoosilla ennen muuttamista  taulukoksi.
    """
       Lastenkirjat  6
       Tietokirjat   5
       Dekkarit      s1
    """
    df_transposed = df.transpose()  # or df.transpose()
    print(df_transposed) 
    table = [df_transposed.columns.tolist()] + df_transposed.values.tolist()
    #Muutetaan Pandas-dataframe matriisiksi
    table[0] = ['bookCat', 'value']
    return table

def create_category_data_for_piechart(data_file, aggregation_column):
    df = prepare_data(data_file)
    category_counts = df[aggregation_column].value_counts()

    # Compute percentages
    category_percentages = (category_counts / category_counts.sum()) * 100

    # Convert to DataFrame
    category_percentages_df = category_percentages.reset_index()
    category_percentages_df.columns = [aggregation_column, 'percentage']

    # Print result
    print(category_percentages_df)
    table = [category_percentages_df.columns.tolist()] + category_percentages_df.values.tolist()
    #Muutetaan Pandas-dataframe matriisiksi
    return table


def save_category_data_to_csv(category_data, csv_filename):

    # Luodaan CSV-tiedosto
    ##cateogory_data = [['Category', 'Value'],
    ##    ['Omakotitalot', 53],
    ##    ['Rivitalot', 24],
    ##    ['Luhtitalot', 10],
    ##    ['Kerrostalot', 6]]

    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(category_data)

    print(f"CSV-tiedosto '{csv_filename}' luotu.")

# Esimerkki edellisen periodin lainauksista
file_path="librarydata.csv"
start_date_str="2024-01-01"
end_date_str="2024-01-31"

# Lasketaan tunnusluvut
metrics = calculate_library_monthly_metrics(file_path, start_date_str, end_date_str)
saveResultToFile(metrics)


book_categories_and_loan_counts = create_category_data_for_barchart("librarydata.csv", 'bookCat')
save_category_data_to_csv(book_categories_and_loan_counts, "bookcats_output.csv")

shares = create_category_data_for_piechart("librarydata.csv", "bookCat")
save_category_data_to_csv(shares, "bookcats_shares_output.csv")
