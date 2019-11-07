from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_attributes_to_findings(
        self,
        findingArns: List,
        attributes: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_assessment_target(
        self,
        assessmentTargetName: str,
        resourceGroupArn: Optional[str] = None,
    ) -> Dict:
        pass


    def create_assessment_template(
        self,
        assessmentTargetArn: str,
        assessmentTemplateName: str,
        durationInSeconds: int,
        rulesPackageArns: List,
        userAttributesForFindings: Optional[List] = None,
    ) -> Dict:
        pass


    def create_exclusions_preview(
        self,
        assessmentTemplateArn: str,
    ) -> Dict:
        pass


    def create_resource_group(
        self,
        resourceGroupTags: List,
    ) -> Dict:
        pass


    def delete_assessment_run(
        self,
        assessmentRunArn: str,
    ):
        pass


    def delete_assessment_target(
        self,
        assessmentTargetArn: str,
    ):
        pass


    def delete_assessment_template(
        self,
        assessmentTemplateArn: str,
    ):
        pass


    def describe_assessment_runs(
        self,
        assessmentRunArns: List,
    ) -> Dict:
        pass


    def describe_assessment_targets(
        self,
        assessmentTargetArns: List,
    ) -> Dict:
        pass


    def describe_assessment_templates(
        self,
        assessmentTemplateArns: List,
    ) -> Dict:
        pass


    def describe_cross_account_access_role(
        self,
    ) -> Dict:
        pass


    def describe_exclusions(
        self,
        exclusionArns: List,
        locale: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_findings(
        self,
        findingArns: List,
        locale: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_resource_groups(
        self,
        resourceGroupArns: List,
    ) -> Dict:
        pass


    def describe_rules_packages(
        self,
        rulesPackageArns: List,
        locale: Optional[str] = None,
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


    def get_assessment_report(
        self,
        assessmentRunArn: str,
        reportFileFormat: str,
        reportType: str,
    ) -> Dict:
        pass


    def get_exclusions_preview(
        self,
        assessmentTemplateArn: str,
        previewToken: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        locale: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_telemetry_metadata(
        self,
        assessmentRunArn: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_assessment_run_agents(
        self,
        assessmentRunArn: str,
        filter: Optional[Dict] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_assessment_runs(
        self,
        assessmentTemplateArns: Optional[List] = None,
        filter: Optional[Dict] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_assessment_targets(
        self,
        filter: Optional[Dict] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_assessment_templates(
        self,
        assessmentTargetArns: Optional[List] = None,
        filter: Optional[Dict] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_event_subscriptions(
        self,
        resourceArn: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_exclusions(
        self,
        assessmentRunArn: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_findings(
        self,
        assessmentRunArns: Optional[List] = None,
        filter: Optional[Dict] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_rules_packages(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
    ) -> Dict:
        pass


    def preview_agents(
        self,
        previewAgentsArn: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def register_cross_account_access_role(
        self,
        roleArn: str,
    ):
        pass


    def remove_attributes_from_findings(
        self,
        findingArns: List,
        attributeKeys: List,
    ) -> Dict:
        pass


    def set_tags_for_resource(
        self,
        resourceArn: str,
        tags: Optional[List] = None,
    ):
        pass


    def start_assessment_run(
        self,
        assessmentTemplateArn: str,
        assessmentRunName: Optional[str] = None,
    ) -> Dict:
        pass


    def stop_assessment_run(
        self,
        assessmentRunArn: str,
        stopAction: Optional[str] = None,
    ):
        pass


    def subscribe_to_event(
        self,
        resourceArn: str,
        event: str,
        topicArn: str,
    ):
        pass


    def unsubscribe_from_event(
        self,
        resourceArn: str,
        event: str,
        topicArn: str,
    ):
        pass


    def update_assessment_target(
        self,
        assessmentTargetArn: str,
        assessmentTargetName: str,
        resourceGroupArn: Optional[str] = None,
    ):
        pass

