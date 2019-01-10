# pymula

Python adapter for Cellulant Mula API version 2.0

To install: `pip install pymula`

For all calls you first have to initiate the adapter with your credentials
You can find your credentials overhere: https://beep2.cellulant.com:9212/checkout/v2/portal/#/home

```
adapter = MulaAdapter(<client id>, <client secret>, <service code>)
```

To start a payment:

```
response = adapter.checkout_request(
  msisdn='2547123456789',
  transaction_id='123',
  account_number='12456768',
  amount=500,
  currency_code='KES',
  country_code='KE',
  description='Donation for school books',
  due_date='2018-11-14 14:20:00',
  callback_url='https://next-economy.com/payment_update',
  customer_first_name='Barack',
  customer_last_name='Obama',
  customer_email='barack@obama.co.ke'
)
```

This will return the Mula response as a Python object.
First you need the `checkoutRequestID` to use for subsequent calls.
From `paymentOptions` you can select the one you want to use e.g. M-Pesa then you pick the `payerModeID` and use that to do a charge request:

```
response = adapter.charge_request(
  msisdn='2547123456789'.
  transaction_id='123,
  checkout_request_id='234567',
  amount='500,
  currency_code='KES',
  country_code='KE',
  payer_mode_id=1,
  language_code='en'
)
```

To check the status of a payment:

```
response = adapter.request_status(
  transaction_id=payment.reference,
  checkout_request_id=payment.remote_reference
)
```

Thanks to Daniel Mbugua for helping out with the Mula API.


###### Tests

Running tests

```
python setup.py test
```

