import requests


class MulaAdapter(object):

    SANDBOX_DOMAIN = 'https://beep2.cellulant.com:9212/checkout/v2/custom'
    LIVE_DOMAIN = 'https://checkout.cellulant.com/checkout/v2/custom'

    AUTH_PATH = '/oauth/token'
    INITIATE_REQUEST_PATH = '/requests/initiate'
    CHARGE_REQUEST_PATH = '/requests/charge'

    def __init__(self, client_id, client_secret, service_code):

        self.client_id = client_id
        self.client_secret = client_secret
        self.service_code = service_code
        self.domain = self.SANDBOX_DOMAIN

    def get_access_token(self):
        url  = "{}{}".format(self.domain, self.AUTH_PATH)

        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }

        response = requests.post(url, payload)
        return response.json().access_token

    def get_payment_options(self):

        path = self.PAYMENT_OPTIONS_PATH.format(
            client_code=self.client_code,
            country='KE',
            languange='en'
        )
        url = "{}{}".format(self.domain, path)
        token = self.get_access_token()
        response = requests.get(url, auth="Bearer {}".format(token))
        print response

    def checkout_request(self,
                         msisdn,
                         transaction_id,
                         account_number,
                         amount,
                         currency_code='KES',
                         country_code='KE',
                         description='',
                         due_date=None,
                         callback_url='',
                         customer_first_name='',
                         customer_last_name='',
                         customer_email='nomen@example.com'):

        payload = {
            "merchantTransactionID": transaction_id,
            "accountNumber": account_number,
            "customerFirstName": customer_first_name,
            "customerLastName": customer_last_name,
            "MSISDN": msisdn,
            "customerEmail": customer_email,
            "requestAmount": amount,
            "currencyCode": currency_code,
            "serviceCode": self.service_code,
            "dueDate": due_date,
            "requestDescription": description,
            "countryCode": country_code,
            "paymentWebhookUrl": callback_url
        }

        url = "{}{}".format(self.domain, self.INITIATE_PAYMENT_PATH)
        token = self.get_access_token()
        response = requests.post(url, payload, auth="Bearer {}".format(token))
        return response.json()

    def charge_request(self,
                       msisdn,
                       transaction_id,
                       checkout_request_id,
                       amount,
                       currency_code='KES',
                       country_code='KE',
                       payer_mode_id=4,
                       language_code='en'):

        payload = {
            "merchantTransactionID": transaction_id,
            "checkoutRequestID": checkout_request_id,
            "chargeMsisdn": msisdn,
            "chargeAmount": amount,
            "currencyCode": currency_code,
            "payerModeID": payer_mode_id,
            "languageCode": language_code,
            "countryCode": country_code
        }

        url = "{}{}".format(self.domain, self.INITIATE_PAYMENT_PATH)
        token = self.get_access_token()
        response = requests.post(url, payload, auth="Bearer {}".format(token))
        return response.json()
