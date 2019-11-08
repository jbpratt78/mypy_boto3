from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListPlacements(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, projectName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListProjects(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
