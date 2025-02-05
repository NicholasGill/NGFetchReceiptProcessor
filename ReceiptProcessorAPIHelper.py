import uuid
import re
import math
from datetime import datetime

def generateIDasString():
    return str(uuid.uuid4())

def calculateReceiptPoints(receipt: dict[str, str | list]):
    totalPoints = 0
    totalPoints += pointsFromName(receipt["retailer"])
    totalPoints += pointsFromTotalPrice(receipt["total"])
    totalPoints += pointsFromItems(receipt["items"])
    totalPoints += pointsFromDate(receipt["purchaseDate"])
    totalPoints += pointsFromTime(receipt["purchaseTime"])
    return totalPoints

def pointsFromName(retailerName: str):
    return len(re.findall('[A-zA-Z0-9]', retailerName))

def pointsFromTotalPrice(totalPrice: int):
    points = 0
    cents = int(totalPrice[-2:])
    if cents == 0:
        points += 50
    if cents % 25 == 0:
        points += 25
    return points

def pointsFromItems(items: list):
    points = 0
    points += (len(items) // 2) * 5
    for item in items:
        shortDescription = item["shortDescription"]
        price = float(item["price"])
        if len(shortDescription.strip()) % 3 == 0:
            points += math.ceil(price * 0.2)
    return points

def pointsFromDate(purchaseDate: str):
    points = 0
    if datetime.strptime(purchaseDate, "%Y-%m-%d").day % 2 == 1:
        points += 6
    return points

def pointsFromTime(purchaseTime: str):
    points = 0
    colonIndex = purchaseTime.index(":")
    timeAsInt = int(purchaseTime[:colonIndex] + purchaseTime[colonIndex + 1:])
    if timeAsInt > 1400 and timeAsInt < 1600:
        points += 10
    return points