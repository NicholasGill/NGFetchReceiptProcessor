from flask import Flask, request
import ReceiptProcessorAPIHelper


app = Flask(__name__)
receiptIDMap = {}

@app.post("/receipts/process")
def processReceipts():
    id = ReceiptProcessorAPIHelper.generateIDasString()
    receiptIDMap[id] = request.get_json()
    print(receiptIDMap[id])
    return {"id": id}

@app.get("/receipts/<string:id>/points")
def getReceiptPointsId(id):
    #TODO
    print(id)
    points = ReceiptProcessorAPIHelper.calculateReceiptPoints(receiptIDMap[id])
    return {"points": points}
     

