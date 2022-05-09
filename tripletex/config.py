import os
import settings

base_url = 'https://tripletex.no/v2'
consumer_token = os.getenv(key='WOOCOMMERCE_URL')
employee_token = 'eyJ0b2tlbklkIjo5NjA0ODksInRva2VuIjoiZjhiNjEyYzEtYzM1NC00OTBmLThmMTYtNzI3ZGM1ZjAwM2I1In0='


base_url = 'https://tripletex.no/v2'
consumer_token = os.getenv(key=settings.TRIPLETEX_CONSUMER_TOKEN)
employee_token = os.getenv(key=settings.TRIPLETEX_EMPLOYEE_TOKEN)

expiration_date = '2025-01-01'

class Config():
    def __init__(self):
        self.base_url = base_url
        self.consumer_token = consumer_token
        self.employee_token = employee_token
        self.expiration_date = expiration_date