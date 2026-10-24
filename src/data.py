"""Leitura e conversão do CSV de chocolates."""

import csv
from pathlib import Path

from texts import t

CHOCOLATES_PATH = Path(__file__).parent.parent / "chocolates.csv"

# Região de cada país de origem do cacau, com o código ISO usado pelo mapa.
# As chaves são ids; o nome que aparece na tela está em locales/pt_br.py
REGIONS = {
    "south_america": {
        "Venezuela": "VEN", "Peru": "PER", "Ecuador": "ECU", "Bolivia": "BOL",
        "Colombia": "COL", "Brazil": "BRA", "Suriname": "SUR",
    },
    "central_america": {
        "Dominican Republic": "DOM", "Nicaragua": "NIC", "Belize": "BLZ", "Guatemala": "GTM",
        "Mexico": "MEX", "Costa Rica": "CRI", "Trinidad": "TTO", "Tobago": "TTO", "Haiti": "HTI",
        "Honduras": "HND", "Jamaica": "JAM", "Grenada": "GRD", "Cuba": "CUB", "St. Lucia": "LCA",
        "Panama": "PAN", "Puerto Rico": "PRI", "El Salvador": "SLV", "Martinique": "MTQ",
        "St.Vincent-Grenadines": "VCT",
    },
    "north_america": {"U.S.A.": "USA"},
    "africa": {
        "Madagascar": "MDG", "Tanzania": "TZA", "Ghana": "GHA", "Uganda": "UGA", "Sao Tome": "STP",
        "Sao Tome & Principe": "STP", "Principe": "STP", "Congo": "COG", "DR Congo": "COD",
        "Ivory Coast": "CIV", "Sierra Leone": "SLE", "Togo": "TGO", "Liberia": "LBR",
        "Nigeria": "NGA", "Cameroon": "CMR", "Gabon": "GAB",
    },
    "asia": {
        "Vietnam": "VNM", "India": "IND", "Philippines": "PHL", "Indonesia": "IDN", "Sumatra": "IDN",
        "Sulawesi": "IDN", "Malaysia": "MYS", "Thailand": "THA", "Sri Lanka": "LKA",
        "Taiwan": "TWN", "Burma": "MMR", "China": "CHN",
    },
    "oceania": {
        "Papua New Guinea": "PNG", "Fiji": "FJI", "Vanuatu": "VUT", "Solomon Islands": "SLB",
        "Australia": "AUS", "Samoa": "WSM",
    },
}


def read_chocolates():
    rows = []
    try:
        with open(CHOCOLATES_PATH, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print(t("file_not_found"))
    except Exception as error:
        print(t("read_error"), error)

    return rows


def convert_cocoa(cocoa):
    """"76%" -> 76.0"""
    return float(cocoa.replace("%", ""))


def convert_flavors(characteristics):
    """"rich cocoa, fatty" -> ["rich cocoa", "fatty"]"""
    flavors = []
    for flavor in characteristics.split(","):
        if flavor.strip() != "":
            flavors.append(flavor.strip().lower())
    return flavors


def find_region(origin):
    if origin == "Blend":
        return "blend"
    for region, countries in REGIONS.items():
        if origin in countries:
            return region
    return "other"


def find_country_code(origin):
    for countries in REGIONS.values():
        if origin in countries:
            return countries[origin]
    return None


def prepare_chocolates(rows):
    chocolates = []
    for row in rows:
        chocolate = {
            "bar": row["barra"],
            "maker": row["fabricante"],
            "origin": row["origem_cacau"],
            "region": find_region(row["origem_cacau"]),
            "cocoa": convert_cocoa(row["cacau"]),
            "flavors": convert_flavors(row["caracteristicas"]),
            "rating": float(row["nota"]),
        }
        chocolates.append(chocolate)

    return chocolates


def load_chocolates():
    return prepare_chocolates(read_chocolates())


if __name__ == "__main__":
    chocolates = load_chocolates()
    print(f"{len(chocolates)} chocolates carregados")
    print("Primeiro chocolate:", chocolates[0])
