
import unittest
from unittest.mock import patch
import requests

BASE_URL = "http://your-factory-api-url.com" 

class TestEmployeeEndpoints(unittest.TestCase):

    @patch('requests.get')
    def test_get_all_employees_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]

        response = requests.get(f"{BASE_URL}/employees")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    @patch('requests.get')
    def test_get_all_employees_api_error(self, mock_get):
        mock_get.return_value.status_code = 500

        response = requests.get(f"{BASE_URL}/employees")

        with self.assertRaises(requests.exceptions.RequestException):
            response.raise_for_status() 

    def test_get_employee_by_id(self):
        pass # You need to implement this test

    def test_create_new_employee(self):
        pass # You need to implement this test

if __name__ == '__main__':
    unittest.main()