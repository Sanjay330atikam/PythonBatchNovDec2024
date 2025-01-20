"""
Purpoese: Comma Seperated Values(CSV)
          writing(creating) a CSV, like unstructured data
"""

with open("my_file.csv",'w')as file:
    file.write('sno,name,age,desgination\n')
    file.write('1,sam,24,MMAfighter\n')
    file.write('2,sanju,25,crickter')
    file.write('3,giibs,32,keeper\n')
    file.write('4,flair,45,wrestler\n')

    file.flush()
    file.close()