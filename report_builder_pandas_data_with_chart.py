import os
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from jinja2 import Environment, FileSystemLoader


# Load data into a Pandas dataframe
data = pd.DataFrame([
        {'name': 'John Doe', 'age': 32, 'occupation': 'Engineer'},
        {'name': 'Jane Smith', 'age': 27, 'occupation': 'Designer'},
        {'name': 'Bob Johnson', 'age': 45, 'occupation': 'Manager'},
    ])

# Create a bar chart using Matplotlib
fig, ax = plt.subplots()
data.plot(kind='bar', x='name', y='age', ax=ax)
ax.set_xlabel('Name')
ax.set_ylabel('Age')
ax.set_title('Sample Chart')

# Save the chart to a PNG file in memory
png_output = BytesIO()
fig.savefig(png_output, format='png')
png_output.seek(0)
png_base64 = str(base64.b64encode(png_output.getvalue())).replace(r"b'", '').rstrip("'")

# Initialize Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
env.filters['b64decode'] = base64.b64decode
template = env.get_template('templates/report_template_with_chart_hpcss.html')

# Convert dataframe to a list of dictionaries
data_dict = data.to_dict(orient='records')

# Define report data
report_data = {
    'title': 'Sample Report',
    'subtitle': 'This is a sample report generated using Jinja2 and Matplotlib',
    'chart': png_base64, 
    'data': data_dict
}

# Render the template with the report data
html_output = template.render(report_data)

# Save the output to a file
with open('output/report_template_with_chart.html', 'w') as f:
    f.write(html_output)


# Convert the HTML to a PDF using wkhtmltopdf
os.system('wkhtmltopdf -O landscape -s letter output/report_template_with_chart.html output/report_template_with_chart.pdf')
