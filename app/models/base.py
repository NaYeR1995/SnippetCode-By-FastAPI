from sqlalchemy import String, TypeDecorator
import uuid

# Custom UUID Type for SQLite
class GUID(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        if isinstance(value, uuid.UUID):
            return str(value)
        return value

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        try:
            return uuid.UUID(value)
        except ValueError:
            return None
    cache_ok = True


    
