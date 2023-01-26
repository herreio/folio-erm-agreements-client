from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.agreement import Agreement
from ...models.application_error import ApplicationError
from ...models.custom_property import CustomProperty
from ...models.entitlement import Entitlement
from ...models.entitlement_option import EntitlementOption
from ...models.erm_resource import ErmResource
from ...models.internal_contact import InternalContact
from ...models.job import Job
from ...models.kb import Kb
from ...models.log_entry import LogEntry
from ...models.organisation import Organisation
from ...models.package import Package
from ...models.package_content_item import PackageContentItem
from ...models.post_erm_entity_type_entity_type import PostErmEntityTypeEntityType
from ...models.ref_data import RefData
from ...models.ref_data_category import RefDataCategory
from ...models.string_template import StringTemplate
from ...types import Response


def _get_kwargs(
    entity_type: PostErmEntityTypeEntityType,
    *,
    client: Client,
    json_body: Union[
        "Agreement",
        "CustomProperty",
        "Entitlement",
        "EntitlementOption",
        "ErmResource",
        "InternalContact",
        "Job",
        "Kb",
        "LogEntry",
        "Organisation",
        "Package",
        "PackageContentItem",
        "RefData",
        "RefDataCategory",
        "StringTemplate",
    ],
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Dict[str, Any]:
    url = "{}/erm/{entityType}".format(client.base_url, entityType=entity_type)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    headers["x-okapi-tenant"] = x_okapi_tenant

    headers["x-okapi-token"] = x_okapi_token

    json_json_body: Dict[str, Any]

    if isinstance(json_body, Agreement):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, CustomProperty):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Entitlement):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, EntitlementOption):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, ErmResource):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, InternalContact):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Job):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Kb):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, LogEntry):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Organisation):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Package):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, PackageContentItem):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, RefData):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, RefDataCategory):
        json_json_body = json_body.to_dict()

    else:
        json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[
        ApplicationError,
        Union[
            "Agreement",
            "CustomProperty",
            "Entitlement",
            "EntitlementOption",
            "ErmResource",
            "InternalContact",
            "Job",
            "Kb",
            "LogEntry",
            "Organisation",
            "Package",
            "PackageContentItem",
            "RefData",
            "RefDataCategory",
            "StringTemplate",
        ],
    ]
]:
    if response.status_code == HTTPStatus.CREATED:

        def _parse_response_201(
            data: object,
        ) -> Union[
            "Agreement",
            "CustomProperty",
            "Entitlement",
            "EntitlementOption",
            "ErmResource",
            "InternalContact",
            "Job",
            "Kb",
            "LogEntry",
            "Organisation",
            "Package",
            "PackageContentItem",
            "RefData",
            "RefDataCategory",
            "StringTemplate",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_0 = Agreement.from_dict(data)

                return componentsschemas_entity_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_1 = CustomProperty.from_dict(data)

                return componentsschemas_entity_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_2 = Entitlement.from_dict(data)

                return componentsschemas_entity_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_3 = EntitlementOption.from_dict(data)

                return componentsschemas_entity_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_4 = ErmResource.from_dict(data)

                return componentsschemas_entity_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_5 = InternalContact.from_dict(data)

                return componentsschemas_entity_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_6 = Job.from_dict(data)

                return componentsschemas_entity_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_7 = Kb.from_dict(data)

                return componentsschemas_entity_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_8 = LogEntry.from_dict(data)

                return componentsschemas_entity_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_9 = Organisation.from_dict(data)

                return componentsschemas_entity_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_10 = Package.from_dict(data)

                return componentsschemas_entity_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_11 = PackageContentItem.from_dict(data)

                return componentsschemas_entity_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_12 = RefData.from_dict(data)

                return componentsschemas_entity_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_13 = RefDataCategory.from_dict(data)

                return componentsschemas_entity_type_13
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_entity_type_14 = StringTemplate.from_dict(data)

            return componentsschemas_entity_type_14

        response_201 = _parse_response_201(response.json())

        return response_201
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ApplicationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union[
        ApplicationError,
        Union[
            "Agreement",
            "CustomProperty",
            "Entitlement",
            "EntitlementOption",
            "ErmResource",
            "InternalContact",
            "Job",
            "Kb",
            "LogEntry",
            "Organisation",
            "Package",
            "PackageContentItem",
            "RefData",
            "RefDataCategory",
            "StringTemplate",
        ],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity_type: PostErmEntityTypeEntityType,
    *,
    client: Client,
    json_body: Union[
        "Agreement",
        "CustomProperty",
        "Entitlement",
        "EntitlementOption",
        "ErmResource",
        "InternalContact",
        "Job",
        "Kb",
        "LogEntry",
        "Organisation",
        "Package",
        "PackageContentItem",
        "RefData",
        "RefDataCategory",
        "StringTemplate",
    ],
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Response[
    Union[
        ApplicationError,
        Union[
            "Agreement",
            "CustomProperty",
            "Entitlement",
            "EntitlementOption",
            "ErmResource",
            "InternalContact",
            "Job",
            "Kb",
            "LogEntry",
            "Organisation",
            "Package",
            "PackageContentItem",
            "RefData",
            "RefDataCategory",
            "StringTemplate",
        ],
    ]
]:
    """Create Entity of specified type

    Args:
        entity_type (PostErmEntityTypeEntityType):
        x_okapi_tenant (str):
        x_okapi_token (str):
        json_body (Union['Agreement', 'CustomProperty', 'Entitlement', 'EntitlementOption',
            'ErmResource', 'InternalContact', 'Job', 'Kb', 'LogEntry', 'Organisation', 'Package',
            'PackageContentItem', 'RefData', 'RefDataCategory', 'StringTemplate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApplicationError, Union['Agreement', 'CustomProperty', 'Entitlement', 'EntitlementOption', 'ErmResource', 'InternalContact', 'Job', 'Kb', 'LogEntry', 'Organisation', 'Package', 'PackageContentItem', 'RefData', 'RefDataCategory', 'StringTemplate']]]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        client=client,
        json_body=json_body,
        x_okapi_tenant=x_okapi_tenant,
        x_okapi_token=x_okapi_token,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity_type: PostErmEntityTypeEntityType,
    *,
    client: Client,
    json_body: Union[
        "Agreement",
        "CustomProperty",
        "Entitlement",
        "EntitlementOption",
        "ErmResource",
        "InternalContact",
        "Job",
        "Kb",
        "LogEntry",
        "Organisation",
        "Package",
        "PackageContentItem",
        "RefData",
        "RefDataCategory",
        "StringTemplate",
    ],
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Optional[
    Union[
        ApplicationError,
        Union[
            "Agreement",
            "CustomProperty",
            "Entitlement",
            "EntitlementOption",
            "ErmResource",
            "InternalContact",
            "Job",
            "Kb",
            "LogEntry",
            "Organisation",
            "Package",
            "PackageContentItem",
            "RefData",
            "RefDataCategory",
            "StringTemplate",
        ],
    ]
]:
    """Create Entity of specified type

    Args:
        entity_type (PostErmEntityTypeEntityType):
        x_okapi_tenant (str):
        x_okapi_token (str):
        json_body (Union['Agreement', 'CustomProperty', 'Entitlement', 'EntitlementOption',
            'ErmResource', 'InternalContact', 'Job', 'Kb', 'LogEntry', 'Organisation', 'Package',
            'PackageContentItem', 'RefData', 'RefDataCategory', 'StringTemplate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApplicationError, Union['Agreement', 'CustomProperty', 'Entitlement', 'EntitlementOption', 'ErmResource', 'InternalContact', 'Job', 'Kb', 'LogEntry', 'Organisation', 'Package', 'PackageContentItem', 'RefData', 'RefDataCategory', 'StringTemplate']]]
    """

    return sync_detailed(
        entity_type=entity_type,
        client=client,
        json_body=json_body,
        x_okapi_tenant=x_okapi_tenant,
        x_okapi_token=x_okapi_token,
    ).parsed


async def asyncio_detailed(
    entity_type: PostErmEntityTypeEntityType,
    *,
    client: Client,
    json_body: Union[
        "Agreement",
        "CustomProperty",
        "Entitlement",
        "EntitlementOption",
        "ErmResource",
        "InternalContact",
        "Job",
        "Kb",
        "LogEntry",
        "Organisation",
        "Package",
        "PackageContentItem",
        "RefData",
        "RefDataCategory",
        "StringTemplate",
    ],
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Response[
    Union[
        ApplicationError,
        Union[
            "Agreement",
            "CustomProperty",
            "Entitlement",
            "EntitlementOption",
            "ErmResource",
            "InternalContact",
            "Job",
            "Kb",
            "LogEntry",
            "Organisation",
            "Package",
            "PackageContentItem",
            "RefData",
            "RefDataCategory",
            "StringTemplate",
        ],
    ]
]:
    """Create Entity of specified type

    Args:
        entity_type (PostErmEntityTypeEntityType):
        x_okapi_tenant (str):
        x_okapi_token (str):
        json_body (Union['Agreement', 'CustomProperty', 'Entitlement', 'EntitlementOption',
            'ErmResource', 'InternalContact', 'Job', 'Kb', 'LogEntry', 'Organisation', 'Package',
            'PackageContentItem', 'RefData', 'RefDataCategory', 'StringTemplate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApplicationError, Union['Agreement', 'CustomProperty', 'Entitlement', 'EntitlementOption', 'ErmResource', 'InternalContact', 'Job', 'Kb', 'LogEntry', 'Organisation', 'Package', 'PackageContentItem', 'RefData', 'RefDataCategory', 'StringTemplate']]]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        client=client,
        json_body=json_body,
        x_okapi_tenant=x_okapi_tenant,
        x_okapi_token=x_okapi_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity_type: PostErmEntityTypeEntityType,
    *,
    client: Client,
    json_body: Union[
        "Agreement",
        "CustomProperty",
        "Entitlement",
        "EntitlementOption",
        "ErmResource",
        "InternalContact",
        "Job",
        "Kb",
        "LogEntry",
        "Organisation",
        "Package",
        "PackageContentItem",
        "RefData",
        "RefDataCategory",
        "StringTemplate",
    ],
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Optional[
    Union[
        ApplicationError,
        Union[
            "Agreement",
            "CustomProperty",
            "Entitlement",
            "EntitlementOption",
            "ErmResource",
            "InternalContact",
            "Job",
            "Kb",
            "LogEntry",
            "Organisation",
            "Package",
            "PackageContentItem",
            "RefData",
            "RefDataCategory",
            "StringTemplate",
        ],
    ]
]:
    """Create Entity of specified type

    Args:
        entity_type (PostErmEntityTypeEntityType):
        x_okapi_tenant (str):
        x_okapi_token (str):
        json_body (Union['Agreement', 'CustomProperty', 'Entitlement', 'EntitlementOption',
            'ErmResource', 'InternalContact', 'Job', 'Kb', 'LogEntry', 'Organisation', 'Package',
            'PackageContentItem', 'RefData', 'RefDataCategory', 'StringTemplate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApplicationError, Union['Agreement', 'CustomProperty', 'Entitlement', 'EntitlementOption', 'ErmResource', 'InternalContact', 'Job', 'Kb', 'LogEntry', 'Organisation', 'Package', 'PackageContentItem', 'RefData', 'RefDataCategory', 'StringTemplate']]]
    """

    return (
        await asyncio_detailed(
            entity_type=entity_type,
            client=client,
            json_body=json_body,
            x_okapi_tenant=x_okapi_tenant,
            x_okapi_token=x_okapi_token,
        )
    ).parsed
