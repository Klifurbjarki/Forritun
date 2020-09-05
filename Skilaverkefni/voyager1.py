numer_of_days_str=input("Number of days after 9/25/09: ")

Distance_from_sun_day0 = 16637000000
Speed_mph = 38241
numer_of_days_int = int(numer_of_days_str)
KM_to_mile = 1.609344
miles_to_AU = 92955877
Distance_gaind_miles = numer_of_days_int*24*Speed_mph
Distance_total_miles =Distance_from_sun_day0+Distance_gaind_miles
Distance_total_KM = round(Distance_total_miles*KM_to_mile)
Distance_total_AU = round(Distance_total_miles/miles_to_AU)

print("Miles from the sun:",Distance_total_miles)
print("Kilometers from the sun:",Distance_total_KM)
print("AU from the sun:",Distance_total_AU)

