"""Textos do app. Para outro idioma, crie locales/en.py com as mesmas chaves e troque LANGUAGE."""

from locales import pt_br

LANGUAGES = {"pt_br": pt_br.STRINGS}
LANGUAGE = "pt_br"


def t(key, **values):
    """t("found", count=10) -> "Chocolates encontrados: 10\""""
    return LANGUAGES[LANGUAGE][key].format(**values)
