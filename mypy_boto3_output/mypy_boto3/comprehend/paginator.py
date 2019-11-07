from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class ListDocumentClassificationJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filter: Dict[str, Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListDocumentClassifiers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filter: Dict[str, Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListDominantLanguageDetectionJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filter: Dict[str, Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListEntitiesDetectionJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filter: Dict[str, Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListEntityRecognizers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filter: Dict[str, Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListKeyPhrasesDetectionJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filter: Dict[str, Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListSentimentDetectionJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filter: Dict[str, Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTopicsDetectionJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filter: Dict[str, Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
