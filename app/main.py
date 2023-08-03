from ariadne.asgi import GraphQL

from app import settings
from app.api import schema

app = GraphQL(schema, debug=settings.debug)
