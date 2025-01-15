import pandas as pd

# Asenna ensin pandas-kirjasto: https://pandas.pydata.org/
# pip3 install pandas

# Data voidaan myös etsiä Internetistä ja käsitellä valmiiksi 
# sopivaan muotoon esim. Excelillä. 

data = {
    "loandId": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "bookId": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    "bookname": [
        "Lasten seikkailut", "Matematiikan alkeet", "Satujen maailma",
        "Historia lyhyesti", "Lasten tietosanakirja", "Maailman luonto",
        "Avainkoodin mysteeri", "Lasten iltasadut",
        "Prinsessa ruusunen","Pieni merenneito","Viisikko seikkailee","Neiti etsivä kohtaa kolmion"
    ],
    "bookCat": [
        "Lastenkirjat", "Tietokirjat", "Lastenkirjat", "Tietokirjat",
        "Lastenkirjat", "Tietokirjat", "Dekkarit", "Lastenkirjat", 
        "Lastenkirjat", "Tietokirjat", "Lastenkirjat", "Tietokirjat",
    ],
    "customerId": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1007, 1006, 1013, 1001],
    "loanDate": [
        "2024-01-02", "2024-01-05", "2024-01-07", "2024-01-10",
        "2024-01-12", "2024-01-15", "2024-01-18", "2024-01-20", 
        "2023-12-01", "2023-12-03", "2023-12-15", "2023-12-18" 
    ],
    "returnDate": [
        "2024-01-20", "2024-02-15", None, "2024-01-25", 
        None, "2024-02-02", "2024-02-01", None,
        "2024-01-01", "2023-12-16", "2024-01-03", "2023-12-29" 
    ]
}

# Tallennetaan CSV-tiedostoksi
df = pd.DataFrame(data)
file_path = "librarydata.csv"
df.to_csv(file_path, index=False, encoding="utf-8")

