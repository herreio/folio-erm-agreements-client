from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.application_error import ApplicationError
from ...models.post_erm_validate_subscription_agreement_name_json_body import (
    PostErmValidateSubscriptionAgreementNameJsonBody,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: PostErmValidateSubscriptionAgreementNameJsonBody,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Dict[str, Any]:
    url = "{}/erm/validate/subscriptionAgreement/name".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    headers["x-okapi-tenant"] = x_okapi_tenant

    headers["x-okapi-token"] = x_okapi_token

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ApplicationError]:
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ApplicationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ApplicationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PostErmValidateSubscriptionAgreementNameJsonBody,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Response[ApplicationError]:
    """Validate a name for an agreement

    Args:
        x_okapi_tenant (str):
        x_okapi_token (str):
        json_body (PostErmValidateSubscriptionAgreementNameJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicationError]
    """

    kwargs = _get_kwargs(
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
    *,
    client: Client,
    json_body: PostErmValidateSubscriptionAgreementNameJsonBody,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Optional[ApplicationError]:
    """Validate a name for an agreement

    Args:
        x_okapi_tenant (str):
        x_okapi_token (str):
        json_body (PostErmValidateSubscriptionAgreementNameJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicationError]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_okapi_tenant=x_okapi_tenant,
        x_okapi_token=x_okapi_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PostErmValidateSubscriptionAgreementNameJsonBody,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Response[ApplicationError]:
    """Validate a name for an agreement

    Args:
        x_okapi_tenant (str):
        x_okapi_token (str):
        json_body (PostErmValidateSubscriptionAgreementNameJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicationError]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        x_okapi_tenant=x_okapi_tenant,
        x_okapi_token=x_okapi_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: PostErmValidateSubscriptionAgreementNameJsonBody,
    x_okapi_tenant: str,
    x_okapi_token: str,
) -> Optional[ApplicationError]:
    """Validate a name for an agreement

    Args:
        x_okapi_tenant (str):
        x_okapi_token (str):
        json_body (PostErmValidateSubscriptionAgreementNameJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_okapi_tenant=x_okapi_tenant,
            x_okapi_token=x_okapi_token,
        )
    ).parsed
