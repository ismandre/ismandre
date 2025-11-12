from datetime import date

with open("README.md", "w") as f:
  f.write(f"## Hello, today is {date.today()} ☀️\n")
  f.write("![Header](./my_example.svg")
