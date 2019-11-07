from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class DescribeBackups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        BackupId: str = None,
        ServerName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ServerName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeServers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ServerName: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
