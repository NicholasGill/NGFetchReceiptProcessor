from src.ReceiptProcessor import app, receiptIDMap
import pytest
import json

#Set up for API tests
@pytest.fixture()
def testApp():
    app.config.update({
        "TESTING": True,
    })
    return app

@pytest.fixture()
def morningReceiptData():
    with open('tests/testcases/morning-receipt.json', 'r') as f:
        morningReceipt = json.load(f)
    return morningReceipt

@pytest.fixture()
def purchaseTimeIncludedData():
    with open('tests/testcases/purchaseTimeIncluded.json', 'r') as f:
        purchaseTimeReceipt = json.load(f)
    return purchaseTimeReceipt

@pytest.fixture()
def simpleReceipt():
    with open('tests/testcases/simple-receipt.json') as f:
        simpleReceipt = json.load(f)
    return simpleReceipt

@pytest.fixture()
def targetReceipt():
    with open('tests/testcases/target-receipt.json') as f:
        targetReceipt = json.load(f)
    return targetReceipt

@pytest.fixture()
def errorReceipt():
    with open('tests/testcases/error-receipt.json') as f:
        errorReceipt = json.load(f)
    return errorReceipt

@pytest.fixture()
def setUpGetReceipt(morningReceiptData, purchaseTimeIncludedData, simpleReceipt, targetReceipt):
    receiptIDMap['2'] = morningReceiptData
    receiptIDMap['3'] = purchaseTimeIncludedData
    receiptIDMap['4'] = simpleReceipt
    receiptIDMap['5'] = targetReceipt