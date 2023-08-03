from pathlib import Path

from ariadne import (make_executable_schema, load_schema_from_path,
                     snake_case_fallback_resolvers)

from .mutation import mutation
from .query import query
from .scalars import scalars

type_defs = load_schema_from_path(Path('app/api/schema'))

schema = make_executable_schema(
    type_defs,
    query,
    mutation,
    scalars,
    snake_case_fallback_resolvers,
)
