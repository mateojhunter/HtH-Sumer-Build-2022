import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

admission_prediction_data = pandas.read_csv("admission_data.csv")

print(admission_prediction_data)