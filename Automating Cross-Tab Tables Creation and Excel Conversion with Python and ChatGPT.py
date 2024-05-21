#!/usr/bin/env python
# coding: utf-8

# # Automating Cross-Tab Tables Creation and Excel Conversion with Python

# In this script demonstration, I'll show you how to automatically create cross-tab tables using Python and convert them into an Excel file. This process is particularly useful when you need to generate multiple individual worksheets with cross-tab tables efficiently.
# 

# # Scenario

# 
# Imagine your manager requires you to develop 20 individual Excel worksheets, each containing a cross-tab table, all within a single day. The traditional method involves creating pivot tables and individual worksheets manually in Excel. While feasible, this approach can be time-consuming and prone to errors, especially when reviewing all values, tables, and ensuring accurate labeling.
# 
# 

# # Solution

# To streamline this process, we can use Python to automate the creation of these cross-tab tables and the conversion into an Excel file. The first step involves using ChatGPT to input instructions for generating Python code that matches the desired table formatting.

# # Demo

# ## 1. Creating the Dataset
# 
# A dataset is created with 20 columns and 20 rows, resembling survey data. Each column represents a question, and each row represents a respondent's answers.

# In[2]:


import pandas as pd
import numpy as np

# Create a larger dataset with 20 columns and 20 rows
data = {
    'Where do you live in Boston?': np.random.choice(['Downtown', 'Back Bay', 'South End', 'Beacon Hill', 'North End'], 20),
    'How satisfied are you with the public transportation in your neighborhood?': np.random.choice(['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied'], 20),
    'How would you rate the safety in your neighborhood?': np.random.choice(['Very Safe', 'Safe', 'Neutral', 'Unsafe', 'Very Unsafe'], 20),
    'How would you describe the cleanliness in your neighborhood?': np.random.choice(['Very Clean', 'Clean', 'Neutral', 'Dirty', 'Very Dirty'], 20),
    'How would you rate the availability of amenities in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'How would you rate the quality of schools in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'How would you rate the affordability of housing in your neighborhood?': np.random.choice(['Very Affordable', 'Affordable', 'Neutral', 'Expensive', 'Very Expensive'], 20),
    'How would you rate the friendliness of neighbors in your neighborhood?': np.random.choice(['Very Friendly', 'Friendly', 'Neutral', 'Unfriendly', 'Very Unfriendly'], 20),
    'How satisfied are you with the green spaces in your neighborhood?': np.random.choice(['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied'], 20),
    'How would you rate the noise levels in your neighborhood?': np.random.choice(['Very Quiet', 'Quiet', 'Neutral', 'Noisy', 'Very Noisy'], 20),
    'How would you rate the overall quality of life in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'How would you rate the public services in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'How would you rate the condition of roads and sidewalks in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'How would you rate the availability of parking in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'How would you rate the access to healthcare in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'How would you rate the quality of internet services in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'How would you rate the variety of restaurants in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'How would you rate the variety of shops in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'How would you rate the availability of cultural activities in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'How would you rate the availability of recreational activities in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'How would you rate the public transportation costs in your neighborhood?': np.random.choice(['Very Affordable', 'Affordable', 'Neutral', 'Expensive', 'Very Expensive'], 20)
}

df = pd.DataFrame(data)



# In[3]:


df


# ## 2.Data Preparation:
# 
# - **Stripping Whitespace**: The code strips leading and trailing whitespace from column names using df.columns.str.strip(). This ensures column names are clean and free of extra spaces.
# 
# - **Storing Original Column Names**: The original column names are stored in original_columns for reference.
# 
# - **Sanitizing Column Names**: Punctuation is removed from column names, and they are truncated to 31 characters to make them suitable for Excel sheet names. This is done using df.columns.str.replace('[^\\s]', '', regex=True).str[:31].

# In[5]:


# Strip leading/trailing whitespace from column names
df.columns = df.columns.str.strip()

# Store original column names
original_columns = df.columns.copy()

# Remove punctuation from column names for Excel sheet names and truncate to 31 characters
sanitized_columns = df.columns.str.replace('[^\w\s]', '', regex=True).str[:31]


# ## 3. Create Crosstabs

# In[6]:


# Create a dictionary to store the crosstabs
crosstabs = {}

# Specify the constant column name
constant_column = 'Where do you live in Boston?'

# Iterate over each column in the DataFrame (excluding the constant column)
for column in df.columns:
    if column != constant_column:
        print(f"Processing column: {column}")

        # Create a crosstab for the current column against the constant column
        crosstab = pd.crosstab(index=df[column], columns=df[constant_column])

        # Calculate percentages for each cell based on the column total
        percentage_crosstab = crosstab.div(crosstab.sum(axis=0), axis=1) * 100

        # Round the percentage values
        percentage_crosstab = percentage_crosstab.round(2)

        # Add the '%' symbol to the percentage values
        percentage_crosstab = percentage_crosstab.applymap(lambda x: f'{x:.2f}%')

        # Rename the percentage columns
        percentage_crosstab = percentage_crosstab.rename(columns=lambda x: x + ' %')

        # Combine the original crosstab and the percentage crosstab
        combined_crosstab = pd.concat([crosstab, percentage_crosstab], axis=1)

        # Rearrange the columns so that each neighborhood column is followed by its percentage column
        ordered_columns = []
        for col in crosstab.columns:
            ordered_columns.append(col)
            ordered_columns.append(col + ' %')
        combined_crosstab = combined_crosstab[ordered_columns]

        # Store the combined crosstab in the dictionary
        crosstabs[column] = combined_crosstab


# In[ ]:


crosstabs[column] 


# ## 3. Writing to Excel

# In[13]:


import re

# Save the crosstabs to an Excel file
file_path = 'questions_crosstabs.xlsx'
with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
    for column, crosstab in crosstabs.items():
        # Sanitize the sheet name
        sheet_name = re.sub('[^\w\s]', '', column)[:31]
        # Write each crosstab to a separate sheet in the Excel file
        crosstab.to_excel(writer, sheet_name=sheet_name, startrow=4)  # start writing from the fifth row
        
        # Get the XlsxWriter workbook and worksheet objects
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]
        
        # Add some formats
        header_format = workbook.add_format({'bold': True, 'text_wrap': True, 'align': 'center', 'valign': 'top', 'bg_color': '#FFD580', 'border': 1})
        cell_format = workbook.add_format({'border': 1})
        
        # Write the original column name on the first row
        worksheet.write(0, 0, column, header_format)
        
        # Set the column width
        for col_num, value in enumerate(crosstab.columns):
            max_len = max(
                crosstab.index.astype(str).str.len().max(), 
                len(str(value))
            ) + 2
            worksheet.set_column(col_num + 1, col_num + 1, max_len)  # Columns are 0-indexed, so adding 1

        # Set the header format for the crosstab
        for col_num, value in enumerate(crosstab.columns):
            worksheet.write(4, col_num + 1, value, header_format)  # Writing headers with format
        
        for row_num, value in enumerate(crosstab.index):
            worksheet.write(row_num + 5, 0, value, header_format)  # Writing row headers with format

        # Write the data with the cell border format
        for row_num, row_data in enumerate(crosstab.values):
            for col_num, cell_data in enumerate(row_data):
                worksheet.write(row_num + 5, col_num + 1, cell_data, cell_format)  # Writing data with border format

print("Crosstabs have been saved to 'questions_crosstabs.xlsx'")


# # Benefits

# - Efficiency: Automates the creation of multiple cross-tab tables and their conversion to Excel, significantly reducing manual effort.
# 
# - Accuracy: Ensures consistent and error-free labeling and formatting of tables.
# 
# - Scalability: Can be easily adapted to handle larger datasets and more complex requirements.
# 
# By leveraging Python and the capabilities of ChatGPT, we can streamline our data analysis processes and focus on deriving insights rather than getting bogged down by repetitive tasks.
# 
