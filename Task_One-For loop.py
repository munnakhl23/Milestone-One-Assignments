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

for x in range(len(mobile_data['data'])):

    mobile_name = mobile_data['data'][x]['name']
    mobile_price = mobile_data['data'][x]['price']
    mobile_made_in = mobile_data['data'][x]['made']
    currency_conversion = float(mobile_price.strip("USD")) * float(mobile_data['exchnage_rate'])

    print(f'{mobile_name} is made in {mobile_made_in}. The price is {mobile_price} which is almost equal to {currency_conversion} BDT ')