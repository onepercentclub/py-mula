from unittest import TestCase

from mula.adapters import MulaAdapter


class MulaAdapterTestCase(TestCase):
    def test_is_string(self):
        adapter = MulaAdapter(
            client_id='test_client_id',
            client_secret='test_client_secret',
            client_code='test_client_code',
            service_code='test_service_code'
        )
        self.assertEqual(adapter.client_code, 'test_client_code')
