from src.ReceiptProcessor import app
import pytest
import json

#Set up for API tests
@pytest.fixture()
def setUp():
    app.config.update({
        "TESTING": True,
    })

@pytest.fixture()
def morningReceiptData():
    with open('tests/examples/morning-receipt.json', 'r') as f:
        morningReceipt = json.load(f)
    return morningReceipt

@pytest.fixture()
def purchaseTimeIncludedData():
    with open('tests/examples/purchaseTimeIncluded.json', 'r') as f:
        purchaseTimeReceipt = json.load(f)
    return purchaseTimeReceipt

@pytest.fixture()
def simpleReceipt():
    with open('tests/examples/simple-receipt.json') as f:
        simpleReceipt = json.load(f)
    return simpleReceipt

@pytest.fixture()
def targetReceipt():
    with open('tests/examples/target-receipt.json') as f:
        targetReceipt = json.load(f)
    return targetReceipt

@pytest.fixture()
def errorReceipt():
    with open('tests/examples/error-receipt.json') as f:
        errorReceipt = json.load(f)
    return errorReceipt