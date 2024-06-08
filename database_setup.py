import psycopg2
print(psycopg2.__version__)

import pandas as pd
from sqlalchemy import create_engine

# Load the Excel file
excel_file = '../Data/TimeOnTaskDB.xlsx'
xls = pd.ExcelFile(excel_file)

# Database connection string (replace with your actual database URL from Heroku)
DATABASE_URL = 'postgresql+psycopg2://u72i36cquau9il:p29a2bcf69a7c7a76082326531763f159d129a7e01d7676a640670ad89fd3c057@c1i13pt05ja4ag.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d425jp822bjtft'

# Create a connection to the Heroku Postgres database
engine = create_engine(DATABASE_URL)

# Iterate over each sheet in the Excel file and write it to the Heroku Postgres database
for sheet_name in xls.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    df.to_sql(sheet_name, engine, index=False, if_exists='replace')
