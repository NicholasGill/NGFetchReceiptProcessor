import re

def testProcessReceipt(testApp, morningReceiptData, purchaseTimeIncludedData, simpleReceipt, targetReceipt, errorReceipt):
    # testApp is created in conftest.py
    with testApp.test_client() as client:
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


def testGetReceipt(testApp, setUpGetReceipt):
    # testApp is created in conftest.py
    # setUpGetReceipt needs to be passed for the "DB" to get populated with data
    # The mock data can be found in conftest.py setUpGetReceipt method
    with testApp.test_client() as client:
        # Not Found - No receipts were processed
        res = client.get(f'/receipts/1/points')
        assert res.status == '404 NOT FOUND'
        assert res.text == "No receipt found for that ID."

        #Happy Path Tests with Given Test Cases
        res = client.get(f'/receipts/2/points')
        assert res.status == '200 OK'
        assert res.json["points"] == 15

        res = client.get(f'/receipts/3/points')
        assert res.status == '200 OK'
        assert res.json["points"] == 109

        res = client.get(f'/receipts/4/points')
        assert res.status == '200 OK'
        assert res.json["points"] == 31

        res = client.get(f'/receipts/5/points')
        assert res.status == '200 OK'
        assert res.json["points"] == 28