import unittest
from selenium import webdriver
import requests

class FastAPITests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and added to PATH
        cls.base_url = "http://127.0.0.1:8000"  # Adjust based on where the FastAPI app is running

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_read_root(self):
        response = requests.get(f"{self.base_url}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Hello": "World"})

    def test_read_item(self):
        response = requests.get(f"{self.base_url}/items/1?q=example")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_id": 1, "q": "example"})

    def test_update_item(self):
        item_data = {"name": "Test Item", "price": 10.5, "is_offer": True}
        response = requests.put(f"{self.base_url}/items/1", json=item_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_name": "Test Item", "item_id": 1})

if __name__ == "__main__":
    unittest.main()
