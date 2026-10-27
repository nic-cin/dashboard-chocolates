"""Métricas, faixas de cacau e resumo por país."""

import data

COCOA_BANDS = ["mild", "semisweet", "dark"]


def calculate_average(chocolates, field):
    total = 0
    for chocolate in chocolates:
        total += chocolate[field]
    return total / len(chocolates)


def group_ratings(chocolates, field):
    """{"Peru": [3.5, 3.0, ...], ...}"""
    groups = {}
    for chocolate in chocolates:
        key = chocolate[field]
        if key in groups:
            groups[key].append(chocolate["rating"])
        else:
            groups[key] = [chocolate["rating"]]
    return groups


def find_best_origin(chocolates, minimum=20):
    """Origem com maior nota média entre as que têm pelo menos `minimum` avaliações."""
    best_origin = None
    best_average = 0
    for origin, ratings in group_ratings(chocolates, "origin").items():
        average = sum(ratings) / len(ratings)
        if origin != "Blend" and len(ratings) >= minimum and average > best_average:
            best_origin = origin
            best_average = average
    return best_origin, best_average


def classify_cocoa(cocoa):
    if cocoa < 70:
        return COCOA_BANDS[0]
    elif cocoa < 80:
        return COCOA_BANDS[1]
    else:
        return COCOA_BANDS[2]


def average_rating_by_band(chocolates):
    """Funcionalidade extra: nota média de cada faixa de cacau."""
    ratings_by_band = {}
    for band in COCOA_BANDS:
        ratings_by_band[band] = []
    for chocolate in chocolates:
        band = classify_cocoa(chocolate["cocoa"])
        ratings_by_band[band].append(chocolate["rating"])

    averages = {}
    for band, ratings in ratings_by_band.items():
        averages[band] = sum(ratings) / len(ratings)
    return averages


def summarize_countries(chocolates):
    """Uma linha por país com região, total de avaliações e nota média, para o mapa."""
    countries = {}
    for origin, ratings in group_ratings(chocolates, "origin").items():
        code = data.find_country_code(origin)
        if code is None:
            continue
        if code in countries:
            countries[code]["ratings"] += ratings
        else:
            countries[code] = {"origin": origin, "region": data.find_region(origin), "ratings": ratings}

    summary = []
    for code, country in countries.items():
        summary.append({
            "code": code,
            "country": country["origin"],
            "region": country["region"],
            "reviews": len(country["ratings"]),
            "rating": round(sum(country["ratings"]) / len(country["ratings"]), 2),
        })
    return summary
