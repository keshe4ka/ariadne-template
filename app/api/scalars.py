from ariadne import ScalarType, upload_scalar

from dateutil import parser

datetime_scalar = ScalarType('Datetime')
date_scalar = ScalarType('Date')


@date_scalar.serializer
@datetime_scalar.serializer
def serialize_datetime(value):
    return value.isoformat()


@date_scalar.value_parser
@datetime_scalar.value_parser
def parse_datetime_value(value):
    try:
        return parser.parse(value)
    except (ValueError, TypeError):
        raise ValueError(f'"{value}" is not a valid ISO 8601 string')


scalars = [datetime_scalar, upload_scalar, date_scalar]
