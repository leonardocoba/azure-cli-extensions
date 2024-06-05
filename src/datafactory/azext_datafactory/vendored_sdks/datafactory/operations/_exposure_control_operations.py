# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_feature_value_request(location_id: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.DataFactory/locations/{locationId}/getFeatureValue",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "locationId": _SERIALIZER.url("location_id", location_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_feature_value_by_factory_request(  # pylint: disable=name-too-long
    resource_group_name: str, factory_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/getFeatureValue",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "factoryName": _SERIALIZER.url(
            "factory_name",
            factory_name,
            "str",
            max_length=63,
            min_length=3,
            pattern=r"^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$",
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_query_feature_values_by_factory_request(  # pylint: disable=name-too-long
    resource_group_name: str, factory_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/queryFeaturesValue",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "factoryName": _SERIALIZER.url(
            "factory_name",
            factory_name,
            "str",
            max_length=63,
            min_length=3,
            pattern=r"^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$",
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class ExposureControlOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.datafactory.DataFactoryManagementClient`'s
        :attr:`exposure_control` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def get_feature_value(
        self,
        location_id: str,
        exposure_control_request: _models.ExposureControlRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ExposureControlResponse:
        """Get exposure control feature for specific location.

        :param location_id: The location identifier. Required.
        :type location_id: str
        :param exposure_control_request: The exposure control request. Required.
        :type exposure_control_request: ~azure.mgmt.datafactory.models.ExposureControlRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ExposureControlResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def get_feature_value(
        self,
        location_id: str,
        exposure_control_request: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ExposureControlResponse:
        """Get exposure control feature for specific location.

        :param location_id: The location identifier. Required.
        :type location_id: str
        :param exposure_control_request: The exposure control request. Required.
        :type exposure_control_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ExposureControlResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def get_feature_value(
        self,
        location_id: str,
        exposure_control_request: Union[_models.ExposureControlRequest, IO[bytes]],
        **kwargs: Any
    ) -> _models.ExposureControlResponse:
        """Get exposure control feature for specific location.

        :param location_id: The location identifier. Required.
        :type location_id: str
        :param exposure_control_request: The exposure control request. Is either a
         ExposureControlRequest type or a IO[bytes] type. Required.
        :type exposure_control_request: ~azure.mgmt.datafactory.models.ExposureControlRequest or
         IO[bytes]
        :return: ExposureControlResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ExposureControlResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(exposure_control_request, (IOBase, bytes)):
            _content = exposure_control_request
        else:
            _json = self._serialize.body(exposure_control_request, "ExposureControlRequest")

        _request = build_get_feature_value_request(
            location_id=location_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ExposureControlResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def get_feature_value_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        exposure_control_request: _models.ExposureControlRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ExposureControlResponse:
        """Get exposure control feature for specific factory.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param exposure_control_request: The exposure control request. Required.
        :type exposure_control_request: ~azure.mgmt.datafactory.models.ExposureControlRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ExposureControlResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def get_feature_value_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        exposure_control_request: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ExposureControlResponse:
        """Get exposure control feature for specific factory.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param exposure_control_request: The exposure control request. Required.
        :type exposure_control_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ExposureControlResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def get_feature_value_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        exposure_control_request: Union[_models.ExposureControlRequest, IO[bytes]],
        **kwargs: Any
    ) -> _models.ExposureControlResponse:
        """Get exposure control feature for specific factory.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param exposure_control_request: The exposure control request. Is either a
         ExposureControlRequest type or a IO[bytes] type. Required.
        :type exposure_control_request: ~azure.mgmt.datafactory.models.ExposureControlRequest or
         IO[bytes]
        :return: ExposureControlResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ExposureControlResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(exposure_control_request, (IOBase, bytes)):
            _content = exposure_control_request
        else:
            _json = self._serialize.body(exposure_control_request, "ExposureControlRequest")

        _request = build_get_feature_value_by_factory_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ExposureControlResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def query_feature_values_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        exposure_control_batch_request: _models.ExposureControlBatchRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ExposureControlBatchResponse:
        """Get list of exposure control features for specific factory.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param exposure_control_batch_request: The exposure control request for list of features.
         Required.
        :type exposure_control_batch_request:
         ~azure.mgmt.datafactory.models.ExposureControlBatchRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ExposureControlBatchResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlBatchResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def query_feature_values_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        exposure_control_batch_request: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ExposureControlBatchResponse:
        """Get list of exposure control features for specific factory.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param exposure_control_batch_request: The exposure control request for list of features.
         Required.
        :type exposure_control_batch_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ExposureControlBatchResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlBatchResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def query_feature_values_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        exposure_control_batch_request: Union[_models.ExposureControlBatchRequest, IO[bytes]],
        **kwargs: Any
    ) -> _models.ExposureControlBatchResponse:
        """Get list of exposure control features for specific factory.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param exposure_control_batch_request: The exposure control request for list of features. Is
         either a ExposureControlBatchRequest type or a IO[bytes] type. Required.
        :type exposure_control_batch_request:
         ~azure.mgmt.datafactory.models.ExposureControlBatchRequest or IO[bytes]
        :return: ExposureControlBatchResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlBatchResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ExposureControlBatchResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(exposure_control_batch_request, (IOBase, bytes)):
            _content = exposure_control_batch_request
        else:
            _json = self._serialize.body(exposure_control_batch_request, "ExposureControlBatchRequest")

        _request = build_query_feature_values_by_factory_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ExposureControlBatchResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
