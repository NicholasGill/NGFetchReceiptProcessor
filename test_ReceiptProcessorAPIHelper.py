import ReceiptProcessorAPIHelper
import json

def testGenerateIDasString():
    ReceiptProcessorAPIHelper.generateIDasString()

def testCalculateReceiptPoints():
    with open('ExampleReceipt.json', 'r') as f:
        Receipt = json.load(f)
    assert ReceiptProcessorAPIHelper.calculateReceiptPoints(Receipt) == 109

def testPointsFromName():
    assert ReceiptProcessorAPIHelper.pointsFromName("TARGET") == 6
    assert ReceiptProcessorAPIHelper.pointsFromName("target") == 6
    assert ReceiptProcessorAPIHelper.pointsFromName("TaRgEt123") == 9
    
def testPointsFromTotalPrice():
    assert ReceiptProcessorAPIHelper.pointsFromTotalPrice("11.00") == 75
    assert ReceiptProcessorAPIHelper.pointsFromTotalPrice("11.25") == 25
    assert ReceiptProcessorAPIHelper.pointsFromTotalPrice("11.11") == 0

def testPointsFromItems():
    oddLenItems = [{"shortDescription": "     Emils Cheese Pizza","price": "12.25"}]
    evenLenItems = [{"shortDescription": "Pepsi", "price": "1.25"}, {"shortDescription": "Dasani", "price": "1.40"}]
    assert ReceiptProcessorAPIHelper.pointsFromItems(oddLenItems) == 3
    assert ReceiptProcessorAPIHelper.pointsFromItems(evenLenItems) == 6

def testPointsFromDate():
    assert ReceiptProcessorAPIHelper.pointsFromDate('2025-02-05') == 6
    assert ReceiptProcessorAPIHelper.pointsFromDate('2025-01-06') == 0

def testPointsFromTime():
    assert ReceiptProcessorAPIHelper.pointsFromTime('09:30') == 0
    assert ReceiptProcessorAPIHelper.pointsFromTime('15:10') == 10