import pandas as pd
import json
fields = {}

df = pd.read_excel('fields.xlsx')
#Mode category, sprite-name(@2x).png
for index,row in df.iterrows():
    if row['Mode'] not in fields:
        fields[row['Mode']] = {}
    if row['category'] not in fields[row['Mode']]:
        fields[row['Mode']][row['category']] = {}

    fields[row['Mode']][row['category']][row['sprite-name(@2x).png']] = {}

print(fields)
with open('fields.json', 'w') as f:
    f.write(json.dumps(fields))
