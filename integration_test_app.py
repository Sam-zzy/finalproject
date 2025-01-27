import unittest
from app import app
import json


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'home.html', response.data)

    def test_predict(self):
        form_data = {
            'value1': 5.1, 'value2': 3.5, 'value3': 1.4, 'value4': 0.2,
            'value5': 5.1, 'value6': 3.5, 'value7': 1.4, 'value8': 0.2,
            'value9': 5.1, 'value10': 3.5, 'value11': 1.4, 'value12': 0.2,
            'value13': 5.1, 'value14': 3.5, 'value15': 1.4, 'value16': 0.2,
            'value17': 5.1, 'value18': 3.5, 'value19': 1.4, 'value20': 0.2,
            'value21': 5.1, 'value22': 3.5, 'value23': 1.4, 'value24': 0.2,
            'value25': 5.1, 'value26': 3.5, 'value27': 1.4, 'value28': 0.2,
            'value29': 5.1, 'value30': 3.5
        }
        response = self.client.post('/predict', data=form_data)

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Malignant', response.data)
        self.assertIn(b'Benign', response.data)

    def test_predict_no_data(self):
        form_data = {}
        response = self.client.post('/predict', data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error', response.data)


if __name__ == '__main__':
    unittest.main()
