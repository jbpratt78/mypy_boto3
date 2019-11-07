from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class ListRuleNamesByTarget(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TargetArn: str,
        EventBusName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListRules(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        NamePrefix: str = None,
        EventBusName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListTargetsByRule(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Rule: str,
        EventBusName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
