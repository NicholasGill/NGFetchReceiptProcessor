from flask import Flask, request
import ReceiptProcessorAPIHelper, ReceiptValidator, ReceiptReturnClasses, ErrorResponses
from werkzeug.exceptions import abort
from flask_marshmallow import Marshmallow
from dataclasses import asdict

app = Flask(__name__)
ma = Marshmallow(app)
receiptIDMap = {}

@app.post("/receipts/process")
def processReceipts():
    receiptJson = request.get_json(silent=True)
    if receiptJson is None:
        abort(ErrorResponses.invalidReceiptErr("The receipt is invalid."))
    errors = ReceiptValidator.Receipt().validate(receiptJson)
    if errors:
        abort(ErrorResponses.invalidReceiptErr("The receipt is invalid."))
    id = ReceiptProcessorAPIHelper.generateIDasString()
    receiptIDMap[id] = receiptJson
    return asdict(ReceiptReturnClasses.ID(id))

@app.get("/receipts/<string:id>/points")
def getReceiptPointsId(id):
    if receiptIDMap.get(id) is None:
        abort(ErrorResponses.notFoundReceiptErr("No receipt found for that ID."))
    points = ReceiptProcessorAPIHelper.calculateReceiptPoints(receiptIDMap[id])
    return asdict(ReceiptReturnClasses.Point(points))