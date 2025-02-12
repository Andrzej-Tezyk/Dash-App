import pandas as pd
import random

def num_value_changer(x: float) -> float:
    return round(random.uniform(0.95, 1.05)*x, 5)

def clean_data() -> None:
    emisje_df["Emisja CO2"] = emisje_df["Emisja CO2"].apply(num_value_changer)       # zmiana wartości
    zakresy_df["Emisja CO2"] = zakresy_df["Emisja CO2"].apply(num_value_changer)
    spolki_df["Spółka nowa"] = spolki_df["Spółka"].apply(lambda x: "Spółka "+str(spolki_df.index[spolki_df[spolki_df["Spółka"] == x].index[0]] + 1))        # nie da się chyba prościej wyciągnąć indeksu dla danej wartości i czegoś z nim zrobić -> Spółka [nr_indeksu]
    spolki_dict = pd.Series(spolki_df["Spółka nowa"].values, index=spolki_df["Spółka"]).to_dict()       # tworzenie słownika do podmiany nazw spółek
    emisje_df["Spółka"].replace(spolki_dict, inplace=True)          # podmiana nazw spółek dla obu 
    zakresy_df["Spółka"].replace(spolki_dict, inplace=True)


input_data_path = r"C:/Users/andrei.tezhyk/Desktop/Dashboard_demo/Dash App/data/Dashbord_dane.xlsx"
na_values_list = ["", " ", "-", "nan", "NaN"]
emisje_df = pd.read_excel(input_data_path, sheet_name=0, na_values=na_values_list)
emisje_df.fillna(0, inplace=True) 
zakresy_df = pd.read_excel(input_data_path, sheet_name=1, na_values=na_values_list)
zakresy_df.fillna(0, inplace=True) 
spolki_df = pd.read_excel(input_data_path, sheet_name=2) 

emisje_df.columns = ["Spółka", "Kategoria Emisji", "Emisja CO2"]
zakresy_df.columns = ["Spółka", "Zakres", "Emisja CO2"]
print("\n", flush=True)       # żeby tekst się dobrze renderował od lewej strony, wszystko jedno jak długa była poprzednia linijka

#print(emisje_df)
clean_data()

print(emisje_df.to_string())
print(zakresy_df.to_string())

emisje_df.to_csv("data_emisje.csv")
zakresy_df.to_csv("data_zakresy.csv")