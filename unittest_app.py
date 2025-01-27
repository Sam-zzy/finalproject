import unittest
from flask import Flask
from flask.testing import FlaskClient
from app import app
import numpy as np


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['DEBUG'] = False

    def test_predict_malignant(self):
        test_data = {
            'value1': 0.1, 'value2': 0.2, 'value3': 0.3, 'value4': 0.4, 'value5': 0.5,
            'value6': 0.6, 'value7': 0.7, 'value8': 0.8, 'value9': 0.9, 'value10': 1.0,
            'value11': 1.1, 'value12': 1.2, 'value13': 1.3, 'value14': 1.4, 'value15': 1.5,
            'value16': 1.6, 'value17': 1.7, 'value18': 1.8, 'value19': 1.9, 'value20': 2.0,
            'value21': 2.1, 'value22': 2.2, 'value23': 2.3, 'value24': 2.4, 'value25': 2.5,
            'value26': 2.6, 'value27': 2.7, 'value28': 2.8, 'value29': 2.9, 'value30': 3.0
        }

        response = self.client.post('/predict', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Malignant', response.data.decode())

    def test_predict_benign(self):
        test_data = {f'value{i}': 0.01 * i for i in range(1, 31)}

        response = self.client.post('/predict', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Benign', response.data.decode())

    def test_predict_no_data(self):
        form_data = {}
        response = self.client.post('/predict', data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ERROR', response.data)


if __name__ == '__main__':
    unittest.main()
