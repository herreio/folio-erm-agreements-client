from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.agreement import Agreement
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
from ...models.ref_data import RefData
from ...models.ref_data_category import RefDataCategory
from ...models.results import Results
from ...models.string_template import StringTemplate
from ...types import UNSET, Response


def _get_kwargs(
    domain: str,
    property_: str,
    *,
    client: Client,
    filters: str,
    match: str,
    term: str,
    sort: str,
    stats: bool,
    per_page: int,
    offset: int,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Dict[str, Any]:
    url = "{}/erm/refdata/{domain}/{property}".format(client.base_url, domain=domain, property=property_)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    headers["x-okapi-tenant"] = x_okapi_tenant

    headers["x-okapi-token"] = x_okapi_token

    params: Dict[str, Any] = {}
    params["filters"] = filters

    params["match"] = match

    params["term"] = term

    params["sort"] = sort

    params["stats"] = stats

    params["perPage"] = per_page

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[
        "Results",
        List[
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
            ]
        ],
    ]
]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "Results",
            List[
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
                ]
            ],
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = Results.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            response_200_type_1 = UNSET
            _response_200_type_1 = data
            for componentsschemas_results_array_item_data in _response_200_type_1:

                def _parse_componentsschemas_results_array_item(
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

                componentsschemas_results_array_item = _parse_componentsschemas_results_array_item(
                    componentsschemas_results_array_item_data
                )

                response_200_type_1.append(componentsschemas_results_array_item)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union[
        "Results",
        List[
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
            ]
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
    domain: str,
    property_: str,
    *,
    client: Client,
    filters: str,
    match: str,
    term: str,
    sort: str,
    stats: bool,
    per_page: int,
    offset: int,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Response[
    Union[
        "Results",
        List[
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
            ]
        ],
    ]
]:
    """Returns list of reference data values for specified domain/property

    Args:
        domain (str):
        property_ (str):
        filters (str):
        match (str):
        term (str):
        sort (str):
        stats (bool):
        per_page (int):
        offset (int):
        x_okapi_tenant (str):
        x_okapi_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['Results', List[Union['Agreement', 'CustomProperty', 'Entitlement', 'EntitlementOption', 'ErmResource', 'InternalContact', 'Job', 'Kb', 'LogEntry', 'Organisation', 'Package', 'PackageContentItem', 'RefData', 'RefDataCategory', 'StringTemplate']]]]
    """

    kwargs = _get_kwargs(
        domain=domain,
        property_=property_,
        client=client,
        filters=filters,
        match=match,
        term=term,
        sort=sort,
        stats=stats,
        per_page=per_page,
        offset=offset,
        x_okapi_tenant=x_okapi_tenant,
        x_okapi_token=x_okapi_token,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain: str,
    property_: str,
    *,
    client: Client,
    filters: str,
    match: str,
    term: str,
    sort: str,
    stats: bool,
    per_page: int,
    offset: int,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Optional[
    Union[
        "Results",
        List[
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
            ]
        ],
    ]
]:
    """Returns list of reference data values for specified domain/property

    Args:
        domain (str):
        property_ (str):
        filters (str):
        match (str):
        term (str):
        sort (str):
        stats (bool):
        per_page (int):
        offset (int):
        x_okapi_tenant (str):
        x_okapi_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['Results', List[Union['Agreement', 'CustomProperty', 'Entitlement', 'EntitlementOption', 'ErmResource', 'InternalContact', 'Job', 'Kb', 'LogEntry', 'Organisation', 'Package', 'PackageContentItem', 'RefData', 'RefDataCategory', 'StringTemplate']]]]
    """

    return sync_detailed(
        domain=domain,
        property_=property_,
        client=client,
        filters=filters,
        match=match,
        term=term,
        sort=sort,
        stats=stats,
        per_page=per_page,
        offset=offset,
        x_okapi_tenant=x_okapi_tenant,
        x_okapi_token=x_okapi_token,
    ).parsed


async def asyncio_detailed(
    domain: str,
    property_: str,
    *,
    client: Client,
    filters: str,
    match: str,
    term: str,
    sort: str,
    stats: bool,
    per_page: int,
    offset: int,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Response[
    Union[
        "Results",
        List[
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
            ]
        ],
    ]
]:
    """Returns list of reference data values for specified domain/property

    Args:
        domain (str):
        property_ (str):
        filters (str):
        match (str):
        term (str):
        sort (str):
        stats (bool):
        per_page (int):
        offset (int):
        x_okapi_tenant (str):
        x_okapi_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['Results', List[Union['Agreement', 'CustomProperty', 'Entitlement', 'EntitlementOption', 'ErmResource', 'InternalContact', 'Job', 'Kb', 'LogEntry', 'Organisation', 'Package', 'PackageContentItem', 'RefData', 'RefDataCategory', 'StringTemplate']]]]
    """

    kwargs = _get_kwargs(
        domain=domain,
        property_=property_,
        client=client,
        filters=filters,
        match=match,
        term=term,
        sort=sort,
        stats=stats,
        per_page=per_page,
        offset=offset,
        x_okapi_tenant=x_okapi_tenant,
        x_okapi_token=x_okapi_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain: str,
    property_: str,
    *,
    client: Client,
    filters: str,
    match: str,
    term: str,
    sort: str,
    stats: bool,
    per_page: int,
    offset: int,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Optional[
    Union[
        "Results",
        List[
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
            ]
        ],
    ]
]:
    """Returns list of reference data values for specified domain/property

    Args:
        domain (str):
        property_ (str):
        filters (str):
        match (str):
        term (str):
        sort (str):
        stats (bool):
        per_page (int):
        offset (int):
        x_okapi_tenant (str):
        x_okapi_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['Results', List[Union['Agreement', 'CustomProperty', 'Entitlement', 'EntitlementOption', 'ErmResource', 'InternalContact', 'Job', 'Kb', 'LogEntry', 'Organisation', 'Package', 'PackageContentItem', 'RefData', 'RefDataCategory', 'StringTemplate']]]]
    """

    return (
        await asyncio_detailed(
            domain=domain,
            property_=property_,
            client=client,
            filters=filters,
            match=match,
            term=term,
            sort=sort,
            stats=stats,
            per_page=per_page,
            offset=offset,
            x_okapi_tenant=x_okapi_tenant,
            x_okapi_token=x_okapi_token,
        )
    ).parsed
