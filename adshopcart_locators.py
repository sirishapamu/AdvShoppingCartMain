from faker import Faker

fake = Faker(locale='en_CA')
adshopcart_url = 'https://advantageonlineshopping.com/#/'
adshopcart_create_account_url = 'https://advantageonlineshopping.com/#/register'
adshopcart_myaccount_url = 'https://advantageonlineshopping.com/#/myAccount'
adshopcart_myorders_url = 'https://advantageonlineshopping.com/#/MyOrders'
adshopcart_speakers_url = 'https://advantageonlineshopping.com/#/category/Speakers/4'
adshopcart_tablets_url = 'https://advantageonlineshopping.com/#/category/Tablets/3'
adshopcart_laptops_url = 'https://advantageonlineshopping.com/#/category/Laptops/1'
adshopcart_mice_url = 'https://advantageonlineshopping.com/#/category/Mice/5'
adshopcart_headphones_url = 'https://advantageonlineshopping.com/#/category/Headphones/2'


old_username = fake.user_name()
new_username = old_username[0:14]
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
description = fake.sentence(nb_words=25)
