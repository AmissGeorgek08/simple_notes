import json
d =  {
    'sales':{
        'employees': ['Smith', 'Johns'],
        'manager': 'Johns',
        'head': 'Smith'
    },
    'development':{
        'employees': ['Jackson', 'Swift', 'Robbinson'],
        'manager': 'Swift',
        'head': 'Robbinson'
    }
 }

with open('file.json', 'w') as file:
    json.dump(d,file)