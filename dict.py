countries = {
    "VN": "Vietnam",
    "JP": "Japan"
}

print(countries["VN"])
countries["US"] = "America"
countries["CN"] = "China"
print(countries)

for key in countries:
    print(countries[key])

print(countries.get("US"))