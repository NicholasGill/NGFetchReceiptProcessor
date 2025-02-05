from flask import Flask, request
import ReceiptProcessorAPIHelper


app = Flask(__name__)
receiptIDMap = {}

@app.post("/receipts/process")
def processReceipts():
    id = ReceiptProcessorAPIHelper.generateIDasString()
    receiptIDMap[id] = request.get_json()
    print(receiptIDMap[id])
    return id

@app.get("/receipts/<string:id>/points")
def getReceiptPointsId():
    #TODO
    return None

