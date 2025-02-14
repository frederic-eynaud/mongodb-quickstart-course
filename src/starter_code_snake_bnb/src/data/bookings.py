import mongoengine

class Booking(mongoengine.EmbeddedDocument):
    guest_owner_id = mongoengine.ObjectIdField()
    guest_snake_id = mongoengine.ObjectIdField()

    booked_date = mongoengine.DateTimeField()
    check_in_date = mongoengine.DateTimeField()
    check_out_date = mongoengine.DateTimeField()
    
    review = mongoengine.StringField()
    rating = mongoengine.IntField(default=0)