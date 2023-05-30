import reports
filename = "r.pdf"
title = "Fruit Report"

table_data = [
    ["Apple", "500 lbs"],
    ["Avocado", "200 lbs"]
]

if __name__ == "__main__":
    reports.generate(filename, title, table_data)
