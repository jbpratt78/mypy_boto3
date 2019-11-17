"Main interface for kinesis-video-archived-media service"

from mypy_boto3_kinesis_video_archived_media.client import Client
from mypy_boto3_kinesis_video_archived_media.helpers import (
    boto3_client,
    get_list_fragments_paginator,
)


__all__ = ("Client", "boto3_client", "get_list_fragments_paginator")
