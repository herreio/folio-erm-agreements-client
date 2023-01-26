from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_contact_owner import InternalContactOwner
    from ..models.ref_data import RefData


T = TypeVar("T", bound="InternalContact")


@attr.s(auto_attribs=True)
class InternalContact:
    """
    Attributes:
        id (Union[Unset, str]):
        owner (Union[Unset, InternalContactOwner]):
        role (Union['RefData', Unset, str]):
        user (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    owner: Union[Unset, "InternalContactOwner"] = UNSET
    role: Union["RefData", Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ref_data import RefData

        id = self.id
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        role: Union[Dict[str, Any], Unset, str]
        if isinstance(self.role, Unset):
            role = UNSET

        elif isinstance(self.role, RefData):
            role = UNSET
            if not isinstance(self.role, Unset):
                role = self.role.to_dict()

        else:
            role = self.role

        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if role is not UNSET:
            field_dict["role"] = role
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.internal_contact_owner import InternalContactOwner
        from ..models.ref_data import RefData

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, InternalContactOwner]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = InternalContactOwner.from_dict(_owner)

        def _parse_role(data: object) -> Union["RefData", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _role_type_1 = data
                role_type_1: Union[Unset, RefData]
                if isinstance(_role_type_1, Unset):
                    role_type_1 = UNSET
                else:
                    role_type_1 = RefData.from_dict(_role_type_1)

                return role_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RefData", Unset, str], data)

        role = _parse_role(d.pop("role", UNSET))

        user = d.pop("user", UNSET)

        internal_contact = cls(
            id=id,
            owner=owner,
            role=role,
            user=user,
        )

        internal_contact.additional_properties = d
        return internal_contact

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
