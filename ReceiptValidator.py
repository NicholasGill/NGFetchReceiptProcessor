from marshmallow import Schema, fields, validate

class Item(Schema):
    shortDescription = fields.Str(validate=validate.Regexp("^[\w\s-]+$"), required=True)
    price = fields.Str(validate=validate.Regexp("^\d+\.\d{2}$"), required=True)

class Receipt(Schema):
    retailer = fields.Str(validate=validate.Regexp("^[\w\s\-&]+$"), required=True)
    purchaseDate = fields.Date(required=True)
    purchaseTime = fields.String(validate=validate.Regexp("^\d{2}:\d{2}$"), required=True)
    items = fields.List(fields.Nested(Item), required=True)
    total = fields.Str(validate=validate.Regexp("^\d+\.\d{2}$"), required=True)