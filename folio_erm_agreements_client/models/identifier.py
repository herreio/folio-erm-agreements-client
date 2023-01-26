from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifier_ns import IdentifierNs


T = TypeVar("T", bound="Identifier")


@attr.s(auto_attribs=True)
class Identifier:
    """
    Attributes:
        ns (Union[Unset, IdentifierNs]):
        value (Union[Unset, str]):
    """

    ns: Union[Unset, "IdentifierNs"] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ns: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ns, Unset):
            ns = self.ns.to_dict()

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ns is not UNSET:
            field_dict["ns"] = ns
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.identifier_ns import IdentifierNs

        d = src_dict.copy()
        _ns = d.pop("ns", UNSET)
        ns: Union[Unset, IdentifierNs]
        if isinstance(_ns, Unset):
            ns = UNSET
        else:
            ns = IdentifierNs.from_dict(_ns)

        value = d.pop("value", UNSET)

        identifier = cls(
            ns=ns,
            value=value,
        )

        identifier.additional_properties = d
        return identifier

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
