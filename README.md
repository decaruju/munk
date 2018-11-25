# munk
Munk is a database back-end whose interface is a REST API configured via YAML

# Helping guide
1. fork the repo 
2. Create a branch named like the feature code (e.g. munk-2)
3. Code the feature
4. Write a PR to this repo

- Make sure your features are unit-tested
- Follow PEP8 (except 80 char lines)
- Make sure your code is idiomatic python

# Todo
## munk-1 Type-checking
When inserting data, munk should cast the data to the required type, and raise an error when the cast fails.
Accepted types are: int, float, decimal(arbitrary size), boolean, str, datetime.
## munk-2 Indexes
A field you be indexable, and give constant-time lookup using the keyword `index: true` in the YAML.
Indexes are stored in a new field in the db.json file under 'index'.
## munk-3 Reference type
A field should be able to have a reference type, referencing another object using the following syntax:
```
---
User:
  name:
    type: str
    required: true
    index: true
  orders:
    type: reference Order 

Order:
  date:
    type: datetime
  products:
    type: reference Product 
  buyer:
    type: reference User 

Product:
  name:
    type: str
...
```
## munk-4 Rest API
The database should be accessible using a rest-like API.
Calls to /model?param1=value1&param2=value2 you return elements of model 1 satisfying
## munk-5 100% coverage
The entire codebase should be tested.
Write unit-tests using pytest.
