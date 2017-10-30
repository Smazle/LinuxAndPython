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


# Task 2.1
globe_map_nk = exam.draw_globe_map(nk_center)
exam.plt.savefig("globe_map_nk.png")

# Task 2.2
globe_map_nk_highlighted = exam.highlight_region(globe_map_nk, country_data["North Korea"])
exam.plt.savefig("globe_map_nk_highlighted.png")
