import os
import pandas as pd
from jinja2 import Environment, FileSystemLoader


# Load data into a Pandas dataframe
data = pd.DataFrame([
        {'name': 'John Doe', 'age': 32, 'occupation': 'Engineer'},
        {'name': 'Jane Smith', 'age': 27, 'occupation': 'Designer'},
        {'name': 'Bob Johnson', 'age': 45, 'occupation': 'Manager'},
    ])

# Convert dataframe to a list of dictionaries
data_dict = data.to_dict(orient='records')

# Initialize Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templates/report_template.html')

# Define report data
report_data = {
    'title': 'Sample Report',
    'subtitle': 'This is a sample report generated using Jinja2 and Pandas',
    'data': data_dict
}

# Render the template with the report data
html_output = template.render(report_data)

# Save the output to a file
with open('output/sample_pandas_report.html', 'w') as f:
    f.write(html_output)

# Convert the HTML to a PDF using wkhtmltopdf
os.system('wkhtmltopdf -O landscape -s letter output/sample_pandas_report.html output/sample_pandas_report.pdf')
