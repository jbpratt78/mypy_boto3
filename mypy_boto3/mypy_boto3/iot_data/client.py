from typing import Dict
from typing import IO
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def delete_thing_shadow(
        self,
        thingName: str,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_thing_shadow(
        self,
        thingName: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def publish(
        self,
        topic: str,
        qos: Optional[int] = None,
        payload: Optional[Union[bytes, IO]] = None,
    ):
        pass


    def update_thing_shadow(
        self,
        thingName: str,
        payload: Union[bytes, IO],
    ) -> Dict:
        pass

