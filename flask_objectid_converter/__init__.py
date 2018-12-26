from bson.objectid import ObjectId, InvalidId

from werkzeug.routing import BaseConverter, ValidationError
from itsdangerous import base64_encode, base64_decode


class ObjectIDConverter(BaseConverter):
    base64: bool
    """
    Flags wether received and converted ObjectId strings should be in Base64
    """
        
    def __init__(self, base64 = False):
        self.base64 = base64
    
    def to_python(self, value):
        try:
            if self.base64:
                value = base64_decode(value)
            return ObjectId(value)
        
        except (InvalidId, ValueError, TypeError):
            raise ValidationError()

    def to_url(self, value):
        if self.base64:
            return base64_encode(value.binary).decode('utf-8')
        else:
            return str(value)
