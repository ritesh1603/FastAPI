import unittest
from fastapi.testclient import TestClient
from main import app  

class FastAPITests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Hello": "World"})

    def test_read_item(self):
        response = self.client.get("/items/1?q=example")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_id": 1, "q": "example"})

    def test_update_item(self):
        item_data = {"name": "Test Item", "price": 10.5, "is_offer": True}
        response = self.client.put("/items/1", json=item_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_name": "Test Item", "item_id": 1})

if __name__ == "__main__":
    unittest.main()
