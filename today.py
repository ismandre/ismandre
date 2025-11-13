import xml.etree.ElementTree as ET
from datetime import date
from dateutil.relativedelta import relativedelta

BIRTHDAY = date(year=1999, month=7, day=17)

today = date.today()
diff = relativedelta(today, BIRTHDAY)
months_text = "months" if diff.months > 1 else "month"
days_text = "days" if diff.days > 1 else "day"
uptime_text = f"{diff.years} years, {diff.months} {months_text}, {diff.days} {days_text}"
if diff.months == 0 and diff.days == 0:
    uptime_text += " 🥳"

input_file = "banner.svg"
output_file = "banner.svg"

ET.register_namespace("", "http://www.w3.org/2000/svg")

tree = ET.parse(input_file)
root = tree.getroot()

namespaces = {"svg": "http://www.w3.org/2000/svg"}
element = root.find(".//*[@id='age_data']", namespaces)

if element is not None:
    element.text = ": " + uptime_text
    tree.write(output_file, encoding="utf-8", xml_declaration=True)



input_file = "banner_light.svg"
output_file = "banner_light.svg"

ET.register_namespace("", "http://www.w3.org/2000/svg")

tree = ET.parse(input_file)
root = tree.getroot()

namespaces = {"svg": "http://www.w3.org/2000/svg"}
element = root.find(".//*[@id='age_data']", namespaces)

if element is not None:
    element.text = ": " + uptime_text
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
