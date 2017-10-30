#!/usr/bin/python3

import exam

# Task 1.1
country_data = exam.read_country_data("./data/countries.dat")
#print(country_data["Denmark"])

# Task 1.2
dk_center = exam.find_center(country_data["Denmark"])
nk_center = exam.find_center(country_data["North Korea"])

print(dk_center)
print(nk_center)
