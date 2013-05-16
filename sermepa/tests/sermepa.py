import unittest
from sermepa import Client


class TestSermepaClient(unittest.TestCase):

    def test_sample(self):
        SANDBOX = True
        SERMEPA_MERCHANT_URL = 'http://www.zikzakmedia.com'
        SERMEPA_MERCHANT_NAME = "Zikzakmedia SL"
        SERMEPA_MERCHANT_CODE = '000000000'
        SERMEPA_SECRET_KEY = '123456'
        SERMEPA_TERMINAL = 1
        SERMEPA_CURRENCY = 978
        SERMEPA_TRANS_TYPE = 0

        values = {
            'Ds_Merchant_Amount': 10.0,
            'Ds_Merchant_Currency': 978,
            'Ds_Merchant_Order': 'SO001',
            'Ds_Merchant_ProductDescription': 'ZZSaas services',
            'Ds_Merchant_Titular': SERMEPA_MERCHANT_NAME,
            'Ds_Merchant_MerchantCode': SERMEPA_MERCHANT_CODE,
            'Ds_Merchant_MerchantURL': SERMEPA_MERCHANT_URL,
            'Ds_Merchant_UrlOK': 'http://www.zzsaas.com/sermepa/confirm',
            'Ds_Merchant_UrlKO': 'http://www.zzsaas.com/sermepa/cancel',
            'Ds_Merchant_MerchantName': SERMEPA_MERCHANT_NAME,
            'Ds_Merchant_Terminal': SERMEPA_TERMINAL,
            'Ds_Merchant_SumTotal': 10.0,
            'Ds_Merchant_TransactionType': SERMEPA_TRANS_TYPE,
        }

        serpayment = Client(business_code=SERMEPA_MERCHANT_CODE, priv_key=SERMEPA_SECRET_KEY, sandbox=SANDBOX)
        sermepa_data = serpayment.get_pay_form_data(values)

        signature = '8A20806C19A5C1D4E25CF26A24F19265CD32F9DE'
        self.assertEqual(sermepa_data['Ds_Merchant_MerchantSignature'], signature)

if __name__ == '__main__':
    unittest.main()
