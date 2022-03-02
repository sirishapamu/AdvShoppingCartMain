from faker import Faker

fake = Faker(locale='en_CA')
adshopcart_url = 'https://advantageonlineshopping.com/#/'
adshopcart_create_account_url = 'https://advantageonlineshopping.com/#/register'
adshopcart_myaccount_url = 'https://advantageonlineshopping.com/#/myAccount'
adshopcart_myorders_url = 'https://advantageonlineshopping.com/#/MyOrders'


new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
phone = fake.phone_number()
city = fake.city()
address = fake.street_address()
province = fake.province_abbr()
postal_code = fake.postalcode()

