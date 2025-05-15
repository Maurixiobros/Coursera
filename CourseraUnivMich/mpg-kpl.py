#1 milla = 1609.344 metros.
#1 galón = 3.785411784 litros.

def liters_100km_to_miles_gallon(liters):
    km_per_liter = 100 / liters
    miles_per_km = 0.621371
    miles_per_liter = km_per_liter * miles_per_km
    gallons_per_liter = 0.264172
    miles_per_gallon = miles_per_liter / gallons_per_liter
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles):
    gallons_per_mile = 1 / miles
    liters_per_gallon = 3.785411784
    liters_per_km = gallons_per_mile * liters_per_gallon / 100
    liters_per_100km = 1 / liters_per_km
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

