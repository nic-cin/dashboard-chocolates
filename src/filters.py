"""Busca e filtros da tabela."""


def list_regions(chocolates):
    regions = []
    for chocolate in chocolates:
        if chocolate["region"] not in regions:
            regions.append(chocolate["region"])
    regions.sort()
    return regions


def list_flavors(chocolates):
    flavors = []
    for chocolate in chocolates:
        for flavor in chocolate["flavors"]:
            if flavor not in flavors:
                flavors.append(flavor)
    flavors.sort()
    return flavors


def search_by_name(chocolates, search):
    search = search.lower().strip()
    found = []
    for chocolate in chocolates:
        if search in chocolate["bar"].lower() or search in chocolate["maker"].lower():
            found.append(chocolate)
    return found


def filter_by_region(chocolates, region):
    if region == "all":
        return chocolates

    result = []
    for chocolate in chocolates:
        if chocolate["region"] == region:
            result.append(chocolate)
    return result


def filter_by_flavors(chocolates, flavors):
    """Funcionalidade extra: mantém só os chocolates que têm todos os sabores escolhidos."""
    result = []
    for chocolate in chocolates:
        has_all = True
        for flavor in flavors:
            if flavor not in chocolate["flavors"]:
                has_all = False
        if has_all:
            result.append(chocolate)
    return result
