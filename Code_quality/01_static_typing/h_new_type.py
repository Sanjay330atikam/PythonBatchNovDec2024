"""
Purpose:
Use the NewType() helper function to create 
distinc types:
    We can create our own customized data types for different uses
"""
from typing import NewType
userID = NewType("userID",int)
some_id = userID(524313)

print(f"type(some_id):{type(some_id)}")
print("some_id :",some_id)

"""
) $ python h_new_type.py
type(someid):<class 'int'>
some id : 524313
"""