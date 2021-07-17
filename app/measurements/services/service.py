from app import db
from app.measurements.models import Measurement
from werkzeug.exceptions import NotFound


class MeasurementService:
    @staticmethod
    def get_by_id(id):
        measurement = db.session.query(Measurement).\
            filter(Measurement.id == id).\
            one_or_none()

        if not measurement:
            raise NotFound(description=f"Measurement with id {id} not found")

        return measurement

    @staticmethod
    def get_all():
        measurements = db.session.query(Measurement)

        return measurements.all()

    @staticmethod
    def get_all_paginated(data):
        return db.session.query(Measurement).paginate(
            page=data['page'],
            per_page=data['per_page'])

    @staticmethod
    def get_latest():
        measurement = db.session.query(Measurement).\
            order_by(Measurement.id.desc()).\
            first()

        if not measurement:
            raise NotFound(description=f"No measurement found")

        return measurement

    @staticmethod
    def create(post_data):
        measurement = Measurement(pollution=post_data['pollution'],
                                  temperature=post_data['temperature'],
                                  humidity=post_data['humidity'])
        db.session.add(measurement)
        db.session.commit()

        return measurement

    def patch(self, id, patch_data):
        measurement = self.get_by_id(id=id)

        if 'pollution' in patch_data:
            measurement.pollution = patch_data['pollution']
        if 'temperature' in patch_data:
            measurement.temperature = patch_data['temperature']
        if 'humidity' in patch_data:
            measurement.humidity = patch_data['humidity']

        db.session.commit()

        return measurement
