# Dict in a List
# DO NOT modify the travel_log directly, only through foo.
#
def add_new_country(log, country, visit_times, list_of_cities):
    log.append({"country": country, "visits": visit_times, "cities": list_of_cities})
    return log


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]

add_new_country(travel_log, "Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
