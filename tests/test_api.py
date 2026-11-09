from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'

def test_predict():
    payload = {
        'Warehouse_block':'A','Mode_of_Shipment':'Flight','Customer_care_calls':4,
        'Customer_rating':3,'Cost_of_the_Product':200,'Prior_purchases':3,
        'Product_importance':'medium','Gender':'M','Discount_offered':10,'Weight_in_gms':2500
    }
    r = client.post('/predict', json=payload)
    assert r.status_code == 200
    assert 'prediction' in r.json()
