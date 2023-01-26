from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ref_data import RefData


T = TypeVar("T", bound="LinkedAmendment")


@attr.s(auto_attribs=True)
class LinkedAmendment:
    """
    Attributes:
        amendment_id (Union[Unset, str]):
        id (Union[Unset, str]):
        owner (Union[Unset, str]):
        status (Union['RefData', Unset, str]):
    """

    amendment_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    status: Union["RefData", Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ref_data import RefData

        amendment_id = self.amendment_id
        id = self.id
        owner = self.owner
        status: Union[Dict[str, Any], Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET

        elif isinstance(self.status, RefData):
            status = UNSET
            if not isinstance(self.status, Unset):
                status = self.status.to_dict()

        else:
            status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amendment_id is not UNSET:
            field_dict["amendmentId"] = amendment_id
        if id is not UNSET:
            field_dict["id"] = id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ref_data import RefData

        d = src_dict.copy()
        amendment_id = d.pop("amendmentId", UNSET)

        id = d.pop("id", UNSET)

        owner = d.pop("owner", UNSET)

        def _parse_status(data: object) -> Union["RefData", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _status_type_1 = data
                status_type_1: Union[Unset, RefData]
                if isinstance(_status_type_1, Unset):
                    status_type_1 = UNSET
                else:
                    status_type_1 = RefData.from_dict(_status_type_1)

                return status_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RefData", Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        linked_amendment = cls(
            amendment_id=amendment_id,
            id=id,
            owner=owner,
            status=status,
        )

        linked_amendment.additional_properties = d
        return linked_amendment

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
