#!/usr/bin/env python3
import run
import reportlab
import datetime

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

#directory_path ='/supplier-data/descriptions'

# Process text files in the directory
#dict_data =run.process_directory(directory_path)


def fruit_dict_to_table(dict_data):
  table_data = [["name", "weight"]]
  for item in dict_data:
      table_data.append([item["name"], str(item["weight"]) + " lbs"])
  return table_data




def generate(filename, title, table_data):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)

    report_title = Paragraph(title, styles["h1"])

    empty_line = Spacer(1, 20)

    elements = [report_title, empty_line]

    for row in table_data:
        name, weight = row
        name_paragraph = Paragraph(f"name: {name}", styles["BodyText"])
        weight_paragraph = Paragraph(f"weight: {weight}", styles["BodyText"])
        elements.append(name_paragraph)
        elements.append(weight_paragraph)
        elements.append(empty_line)

    report.build(elements)
 