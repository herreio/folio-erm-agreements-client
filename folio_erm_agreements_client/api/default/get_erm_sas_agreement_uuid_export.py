from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.agreement import Agreement
from ...types import Response


def _get_kwargs(
    agreement_uuid: str,
    *,
    client: Client,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Dict[str, Any]:
    url = "{}/erm/sas/{agreementUUID}/export".format(client.base_url, agreementUUID=agreement_uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    headers["x-okapi-tenant"] = x_okapi_tenant

    headers["x-okapi-token"] = x_okapi_token

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Agreement]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Agreement.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Agreement]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agreement_uuid: str,
    *,
    client: Client,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Response[Agreement]:
    """Export the specified agreement as JSON including all resources in the internal KB associated with
    specified agreement

    Args:
        agreement_uuid (str):
        x_okapi_tenant (str):
        x_okapi_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Agreement]
    """

    kwargs = _get_kwargs(
        agreement_uuid=agreement_uuid,
        client=client,
        x_okapi_tenant=x_okapi_tenant,
        x_okapi_token=x_okapi_token,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agreement_uuid: str,
    *,
    client: Client,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Optional[Agreement]:
    """Export the specified agreement as JSON including all resources in the internal KB associated with
    specified agreement

    Args:
        agreement_uuid (str):
        x_okapi_tenant (str):
        x_okapi_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Agreement]
    """

    return sync_detailed(
        agreement_uuid=agreement_uuid,
        client=client,
        x_okapi_tenant=x_okapi_tenant,
        x_okapi_token=x_okapi_token,
    ).parsed


async def asyncio_detailed(
    agreement_uuid: str,
    *,
    client: Client,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Response[Agreement]:
    """Export the specified agreement as JSON including all resources in the internal KB associated with
    specified agreement

    Args:
        agreement_uuid (str):
        x_okapi_tenant (str):
        x_okapi_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Agreement]
    """

    kwargs = _get_kwargs(
        agreement_uuid=agreement_uuid,
        client=client,
        x_okapi_tenant=x_okapi_tenant,
        x_okapi_token=x_okapi_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agreement_uuid: str,
    *,
    client: Client,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Optional[Agreement]:
    """Export the specified agreement as JSON including all resources in the internal KB associated with
    specified agreement

    Args:
        agreement_uuid (str):
        x_okapi_tenant (str):
        x_okapi_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Agreement]
    """

    return (
        await asyncio_detailed(
            agreement_uuid=agreement_uuid,
            client=client,
            x_okapi_tenant=x_okapi_tenant,
            x_okapi_token=x_okapi_token,
        )
    ).parsed
