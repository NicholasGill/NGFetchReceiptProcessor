import uuid
import re

def generateIDasString():
    return str(uuid.uuid4())

def calculateReceiptPoints(receipt: dict[str, str | list]):
    #TODO
    totalPoints = 0
    totalPoints += calculateRetailersPointsFromName(receipt["retailer"])
    totalPoints += calculateRetailersPointsFromTotal(receipt["total"])
    return totalPoints


#These could go into a different file

def calculateRetailersPointsFromName(retailerName: str):
    return len(re.findall('[A-zA-Z0-9]', retailerName))

def calculateRetailersPointsFromTotal(totalPrice: int):
    points = 0
    cents = int(totalPrice[-2:])
    if cents == '00':
        points += 50
    if cents % 25 == 0:
        points += 25
    return points