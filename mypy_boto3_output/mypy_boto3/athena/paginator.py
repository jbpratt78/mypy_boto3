from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class GetQueryResults(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, QueryExecutionId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListNamedQueries(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, WorkGroup: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListQueryExecutions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, WorkGroup: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
