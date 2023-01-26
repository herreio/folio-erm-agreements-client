from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogEntryAdditionalInfo")


@attr.s(auto_attribs=True)
class LogEntryAdditionalInfo:
    """
    Attributes:
        job_id (Union[Unset, str]):
        tenant (Union[Unset, str]):
        tenant_id (Union[Unset, str]):
    """

    job_id: Union[Unset, str] = UNSET
    tenant: Union[Unset, str] = UNSET
    tenant_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        tenant = self.tenant
        tenant_id = self.tenant_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_id = d.pop("jobId", UNSET)

        tenant = d.pop("tenant", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        log_entry_additional_info = cls(
            job_id=job_id,
            tenant=tenant,
            tenant_id=tenant_id,
        )

        log_entry_additional_info.additional_properties = d
        return log_entry_additional_info

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
