from marshmallow import Schema, fields
from app.measurements.constants import PAGE, PER_PAGE


class MeasurementPostRequestSchema(Schema):
    pollution = fields.Float(required=True)
    temperature = fields.Float(required=True)
    humidity = fields.Float(required=True)


class MeasurementPatchRequestSchema(Schema):
    pollution = fields.Float(required=False)
    temperature = fields.Float(required=False)
    humidity = fields.Float(required=False)


class MeasurementResponseSchema(Schema):
    id = fields.Integer()
    pollution = fields.Float()
    temperature = fields.Float()
    humidity = fields.Float()
    created = fields.DateTime()


class PaginationMetaSchema(Schema):
    page = fields.Integer(required=False, default=PAGE, missing=PAGE)
    per_page = fields.Integer(required=False, default=PER_PAGE,
                              missing=PER_PAGE)
    total = fields.Integer(required=False, default=0, missing=0)


class PaginationResultSchema(Schema):
    meta = fields.Method('get_meta')
    response = fields.Method('get_response')

    @staticmethod
    def get_meta(data):
        response = dict()
        response['page'] = data.page
        response['per_page'] = data.per_page
        response['total'] = data.total
        return PaginationMetaSchema().dump(response)

    @staticmethod
    def get_response(data):
        return MeasurementResponseSchema(many=True).dump(data.items)
