mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchnage_rate': 110.25
            }

i = 0
while i < len(mobile_data['data']):
    mobile_name = mobile_data['data'][i]['name']
    mobile_price = mobile_data['data'][i]['price']
    mobile_made_in = mobile_data['data'][i]['made']
    currency_conversion = float(mobile_price.strip("USD")) * float(mobile_data['exchnage_rate'])
    i += 1
    print(f'{mobile_name} is made in {mobile_made_in}. The price is {mobile_price} which is almost equal to {currency_conversion} BDT ')

statements = "i have tried many time to do this task through FOR Loop, but i couldn't"
suggestion = "So, please help me to sort it out for both task"
print(f" \n NOTE -  {statements.capitalize()}.{suggestion} ")

mentor = "MD. ABDUL AOUWAL"
pos = "THE HONOURABLE MENTOR OF THIS BATCH"
print("\n THANKS TO ",mentor.title(),"\n ", pos.lower() )


