from src.ReceiptProcessor import app
import re

def testProcessReceipt(morningReceiptData, purchaseTimeIncludedData, simpleReceipt, targetReceipt, errorReceipt):
    with app.test_client() as client:
        # Bad Request - No Request Body
        res = client.post('/receipts/process')
        assert res.status == '400 BAD REQUEST'
        assert res.text == "The receipt is invalid."
        # Bad Request - Request Body doesn't match json schema
        # See error-receipt in Examples (Missing Purchase Time)
        res = client.post('/receipts/process', json = errorReceipt)
        assert res.status == '400 BAD REQUEST'
        assert res.text == "The receipt is invalid."

        #Happy Path with Given Test Cases
        res = client.post('/receipts/process', json = morningReceiptData)
        assert res.status == '200 OK'
        assert re.match(r"^\S+$", res.json['id'])

        res = client.post('/receipts/process', json = simpleReceipt)
        assert res.status == '200 OK'
        assert re.match(r"^\S+$", res.json['id'])

        res = client.post('/receipts/process', json = targetReceipt)
        assert res.status == '200 OK'
        assert re.match(r"^\S+$", res.json['id'])

        res = client.post('/receipts/process', json = purchaseTimeIncludedData)
        assert res.status == '200 OK'
        assert re.match(r"^\S+$", res.json['id'])


def testGetReceipt(morningReceiptData, purchaseTimeIncludedData, simpleReceipt, targetReceipt):
    with app.test_client() as client:
        # Not Found - No receipts were processed
        res = client.get(f'/receipts/1/points')
        assert res.status == '404 NOT FOUND'
        assert res.text == "No receipt found for that ID."

        #Happy Path Tests with Given Test Cases
        id = client.post('/receipts/process', json = morningReceiptData).json['id']
        res = client.get(f'/receipts/{id}/points')
        assert res.status == '200 OK'
        assert res.json["points"] == 15

        id = client.post('/receipts/process', json = purchaseTimeIncludedData).json['id']
        res = client.get(f'/receipts/{id}/points')
        assert res.status == '200 OK'
        assert res.json["points"] == 109

        id = client.post('/receipts/process', json = simpleReceipt).json['id']
        res = client.get(f'/receipts/{id}/points')
        assert res.status == '200 OK'
        assert res.json["points"] == 31

        id = client.post('/receipts/process', json = targetReceipt).json['id']
        res = client.get(f'/receipts/{id}/points')
        assert res.status == '200 OK'
        assert res.json["points"] == 28