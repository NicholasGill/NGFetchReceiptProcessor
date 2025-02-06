from src.ReceiptProcessorAPIHelper import generateIDasString, calculateReceiptPoints, pointsFromName, pointsFromTotalPrice, pointsFromItems, pointsFromDate, pointsFromTime
import json
# Unit tests for the Helper methods in ReceiptProcessor

# Parent Method for calculating total score of a receipt
def testCalculateReceiptPoints():
    with open('tests/examples/purchaseTimeIncluded.json', 'r') as f:
        Receipt = json.load(f)
    assert calculateReceiptPoints(Receipt) == 109

# Child Methods for calcualting parts of the total score by field, see Rules for the different cases and scores
def testPointsFromName():
    #Testing different capitalizations and numbers
    assert pointsFromName("TARGET") == 6
    assert pointsFromName("target") == 6
    assert pointsFromName("TaRgEt123") == 9
    
def testPointsFromTotalPrice():
    # 00 Case
    assert pointsFromTotalPrice("11.00") == 75
    # 25 Multiple Case
    assert pointsFromTotalPrice("11.25") == 25
    # Not 00 and Not 25 Multiple
    assert pointsFromTotalPrice("11.11") == 0

def testPointsFromItems():
    oddLenItems = [{"shortDescription": "     Emils Cheese Pizza","price": "12.25"}]
    evenLenItems = [{"shortDescription": "Pepsi", "price": "1.25"}, {"shortDescription": "Aqua", "price": "1.40"}]
    assert pointsFromItems(oddLenItems) == 3
    assert pointsFromItems(evenLenItems) == 5

def testPointsFromDate():
    # Even and Odd Dates
    assert pointsFromDate('2025-02-05') == 6
    assert pointsFromDate('2025-01-06') == 0

def testPointsFromTime():
    assert pointsFromTime('09:30') == 0
    #Between 14:00 (2pm) and 16:00 (4pm)
    assert pointsFromTime('15:10') == 10