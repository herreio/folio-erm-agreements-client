from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.delete_erm_entity_type_entity_uuid_entity_type import DeleteErmEntityTypeEntityUUIDEntityType
from ...types import Response


def _get_kwargs(
    entity_type: DeleteErmEntityTypeEntityUUIDEntityType,
    entity_uuid: str,
    *,
    client: Client,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Dict[str, Any]:
    url = "{}/erm/{entityType}/{entityUUID}".format(client.base_url, entityType=entity_type, entityUUID=entity_uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    headers["x-okapi-tenant"] = x_okapi_tenant

    headers["x-okapi-token"] = x_okapi_token

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity_type: DeleteErmEntityTypeEntityUUIDEntityType,
    entity_uuid: str,
    *,
    client: Client,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Response[Any]:
    """Delete an Entity

    Args:
        entity_type (DeleteErmEntityTypeEntityUUIDEntityType):
        entity_uuid (str):
        x_okapi_tenant (str):
        x_okapi_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        entity_uuid=entity_uuid,
        client=client,
        x_okapi_tenant=x_okapi_tenant,
        x_okapi_token=x_okapi_token,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    entity_type: DeleteErmEntityTypeEntityUUIDEntityType,
    entity_uuid: str,
    *,
    client: Client,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Response[Any]:
    """Delete an Entity

    Args:
        entity_type (DeleteErmEntityTypeEntityUUIDEntityType):
        entity_uuid (str):
        x_okapi_tenant (str):
        x_okapi_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        entity_uuid=entity_uuid,
        client=client,
        x_okapi_tenant=x_okapi_tenant,
        x_okapi_token=x_okapi_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
