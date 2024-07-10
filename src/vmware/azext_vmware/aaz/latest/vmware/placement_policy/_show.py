# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "vmware placement-policy show",
)
class Show(AAZCommand):
    """Get a placement policy by name in a private cloud cluster

    :example: Get a placement policy by name.
        az vmware placement-policy show --resource-group group1 --private-cloud cloud1 --cluster-name cluster1 --placement-policy-name policy1
    """

    _aaz_info = {
        "version": "2023-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.avs/privateclouds/{}/clusters/{}/placementpolicies/{}", "2023-09-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_name = AAZStrArg(
            options=["--cluster-name"],
            help="Name of the cluster in the private cloud",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^[-\w\._]+$",
            ),
        )
        _args_schema.placement_policy_name = AAZStrArg(
            options=["-n", "--name", "--placement-policy-name"],
            help="Name of the VMware vSphere Distributed Resource Scheduler (DRS) placement policy",
            required=True,
            id_part="child_name_2",
            fmt=AAZStrArgFormat(
                pattern="^[-\w\._]+$",
            ),
        )
        _args_schema.private_cloud = AAZStrArg(
            options=["-c", "--private-cloud"],
            help="Name of the private cloud",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[-\w\._]+$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PlacementPoliciesGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class PlacementPoliciesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/clusters/{clusterName}/placementPolicies/{placementPolicyName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "placementPolicyName", self.ctx.args.placement_policy_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "privateCloudName", self.ctx.args.private_cloud,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.state = AAZStrType()
            properties.type = AAZStrType(
                flags={"required": True},
            )

            disc_vm_host = cls._schema_on_200.properties.discriminate_by("type", "VmHost")
            disc_vm_host.affinity_strength = AAZStrType(
                serialized_name="affinityStrength",
            )
            disc_vm_host.affinity_type = AAZStrType(
                serialized_name="affinityType",
                flags={"required": True},
            )
            disc_vm_host.azure_hybrid_benefit_type = AAZStrType(
                serialized_name="azureHybridBenefitType",
            )
            disc_vm_host.host_members = AAZListType(
                serialized_name="hostMembers",
                flags={"required": True},
            )
            disc_vm_host.vm_members = AAZListType(
                serialized_name="vmMembers",
                flags={"required": True},
            )

            host_members = cls._schema_on_200.properties.discriminate_by("type", "VmHost").host_members
            host_members.Element = AAZStrType()

            vm_members = cls._schema_on_200.properties.discriminate_by("type", "VmHost").vm_members
            vm_members.Element = AAZStrType()

            disc_vm_vm = cls._schema_on_200.properties.discriminate_by("type", "VmVm")
            disc_vm_vm.affinity_type = AAZStrType(
                serialized_name="affinityType",
                flags={"required": True},
            )
            disc_vm_vm.vm_members = AAZListType(
                serialized_name="vmMembers",
                flags={"required": True},
            )

            vm_members = cls._schema_on_200.properties.discriminate_by("type", "VmVm").vm_members
            vm_members.Element = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
