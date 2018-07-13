# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 1)

    def test_get_valid_products(self):
        response = self.client.get("/api/v1/products/2")
        #print(response.json)
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_products(self):
        response = self.client.get("/api/v1/products/244")
        #print(response.status_code)
        self.assertEqual(response.status_code, 404)

    def test_delete_invalid_products(self):
        response = self.client.delete("/api/v1/products/244")
        #print(response.status_code)
        self.assertEqual(response.status_code, 404)

    def test_delete_valid_products(self):
        response = self.client.delete("/api/v1/products/1")
        #print(response.status_code)
        self.assertEqual(response.status_code, 204)

    def test_create_valid_products(self):
        response = self.client.post("/api/v1/products",data=dict(id=5,name='Toto'))
        #print(response.status_code)
        self.assertEqual(response.status_code, 201)
