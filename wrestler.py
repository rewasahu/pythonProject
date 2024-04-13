hall_of_fame=[
  {
    'name':'Undertaker',
    'finisher':'Tombstone Pile Driver',
    'experience': 30,
    'aka': 'American Badass and Phenom'  
  },
  {
    'name':'John Cena',
    'finisher':'Attitude Adjustment',
    'experience': 20,
    'aka': 'HLR'  
  },
]

def add_items_in_empty_dictionary(naam:str,smack:str,year:int,aaka):
    empty_dict={}
    empty_dict['name']=naam
    empty_dict['finisher']=smack
    empty_dict['experience']=year
    empty_dict['aka']=aaka
    hall_of_fame.append(empty_dict)

end=False
while not end:
    name=input("wrestler name?")
    finisher=input('finisher name?')
    year_of_wrestling=int(input("from how many years he is wrestling?"))
    aka=input("also known as?")
    add_items_in_empty_dictionary(name,finisher,year_of_wrestling,aka)
    if input("want to add more?\nType 'Y' or 'N': ").lower()=='n':
        end=True
   
# for n in range(0,len(hall_of_fame)):
#   print(hall_of_fame[n]['name'])
for n in hall_of_fame:
  print(n['name'])

