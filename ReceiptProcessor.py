from flask import Flask, request
import ReceiptProcessorAPIHelper, ReceiptValidator, ReceiptReturnClasses, ErrorResponses
from werkzeug.exceptions import abort
from dataclasses import asdict

app = Flask(__name__)
receiptIDMap = {}

@app.post("/receipts/process")
def processReceipts():
    receiptJson = request.get_json(silent=True)
    if receiptJson is None:
        abort(ErrorResponses.invalidReceiptError())
    errors = ReceiptValidator.Receipt().validate(receiptJson)
    if errors:
        abort(ErrorResponses.invalidReceiptError())
    id = ReceiptProcessorAPIHelper.generateIDasString()
    receiptIDMap[id] = receiptJson
    return asdict(ReceiptReturnClasses.ReceiptID(id))

@app.get("/receipts/<string:id>/points")
def getReceiptPointsId(id):
    if receiptIDMap.get(id) is None:
        abort(ErrorResponses.notFoundReceiptError())
    points = ReceiptProcessorAPIHelper.calculateReceiptPoints(receiptIDMap[id])
    return asdict(ReceiptReturnClasses.Point(points))