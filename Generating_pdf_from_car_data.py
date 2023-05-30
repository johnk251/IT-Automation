import json
import os
import locale
import sys
import reports
import emails
def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  max_sales = {"total_sales": 0}
  car_years = {}
  total_sales_in_year =0
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    if item["total_sales"] > max_sales["total_sales"]:
            max_sales = item
   
        # Track car years and their counts
    car_year = item["car"]["car_year"]
    car_years[car_year] = car_years.get(car_year, 0) + 1
    
    # Find the most popular car year
  most_popular_year = max(car_years, key=car_years.get)
  for item in data:
      if item["car"]["car_year"]==most_popular_year:
            total_sales_in_year+=item["total_sales"]
  

  summary = [
        "The {} had the most sales: {}".format(
            format_car(max_sales["car"]), max_sales["total_sales"]),
        "The most popular year was {} with {} sales.".format(
            most_popular_year, total_sales_in_year),
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
    ]
    

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  home_dir=os.path.expanduser("~")
  data_path=home_dir+"/data/car_sales.json"
  data = load_data(data_path)
  summary = process_data(data)
  formatted_summary = "<br\>".join(summary)
  
  print(formatted_summary)
  reports.generate("/tmp/cars.pdf", "Cars Sales Report",formatted_summary, cars_dict_to_table(data))

  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  body = formatted_summary

  message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
  emails.send(message)
if __name__ == "__main__":
  main(sys.argv)