"""Dashboard de Chocolates: app Streamlit."""

import plotly.express as px
import streamlit as st

import analysis
import data
import filters
from texts import t


def build_table(chocolates):
    table = []
    for chocolate in chocolates:
        row = {
            t("col_bar"): chocolate["bar"],
            t("col_maker"): chocolate["maker"],
            t("col_origin"): chocolate["origin"],
            t("col_region"): t("region_" + chocolate["region"]),
            t("col_cocoa"): f"{chocolate['cocoa']:.0f}%",
            t("col_band"): t("band_" + analysis.classify_cocoa(chocolate["cocoa"])),
            t("col_flavors"): ", ".join(chocolate["flavors"]),
            t("col_rating"): chocolate["rating"],
        }
        table.append(row)
    return table


def build_map(chocolates):
    countries = analysis.summarize_countries(chocolates)
    for country in countries:
        country["region"] = t("region_" + country["region"])

    world_map = px.choropleth(
        countries,
        locations="code",
        color="region",
        hover_name="country",
        hover_data={"code": False, "reviews": True, "rating": True},
        labels={"region": t("col_region"), "reviews": t("col_reviews"), "rating": t("metric_rating")},
    )
    world_map.update_geos(fitbounds="locations", showframe=False)
    world_map.update_layout(height=350, margin=dict(l=0, r=0, t=0, b=0))
    return world_map


def main():
    st.set_page_config(page_title=t("page_title"), page_icon="🍫", layout="wide")
    st.title(t("title"))

    chocolates = data.load_chocolates()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(t("metric_total"), len(chocolates))

    average_rating = analysis.calculate_average(chocolates, "rating")
    col2.metric(t("metric_rating"), f"{average_rating:.2f}")

    average_cocoa = analysis.calculate_average(chocolates, "cocoa")
    col3.metric(t("metric_cocoa"), f"{average_cocoa:.0f}%")

    best_origin, best_average = analysis.find_best_origin(chocolates)
    col4.metric(t("metric_best_origin"), best_origin)
    col4.caption(t("best_origin_caption", average=best_average))

    st.subheader(t("map_title"))
    st.plotly_chart(build_map(chocolates), config={"displayModeBar": False})

    st.subheader(t("bands_title"))
    band_cols = st.columns(3)
    averages = analysis.average_rating_by_band(chocolates)
    for col, band in zip(band_cols, analysis.COCOA_BANDS):
        col.metric(t("band_" + band), f"{averages[band]:.2f}")

    st.subheader(t("table_title"))
    col_search, col_region, col_flavors = st.columns(3)
    search = col_search.text_input(t("search_label"))
    region = col_region.selectbox(
        t("region_label"),
        ["all"] + filters.list_regions(chocolates),
        format_func=lambda region: t("region_" + region),
    )
    flavors = col_flavors.multiselect(
        t("flavors_label"),
        filters.list_flavors(chocolates),
        placeholder=t("flavors_placeholder"),
    )

    found = filters.filter_by_region(chocolates, region)
    found = filters.search_by_name(found, search)
    found = filters.filter_by_flavors(found, flavors)
    found.sort(key=lambda chocolate: chocolate["rating"], reverse=True)

    if len(found) == 0:
        st.warning(t("not_found"))
    else:
        st.write(t("found", count=len(found)))
        st.dataframe(build_table(found), hide_index=True)


if __name__ == "__main__":
    main()
