from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ref_data import RefData


T = TypeVar("T", bound="RefDataCategory")


@attr.s(auto_attribs=True)
class RefDataCategory:
    """
    Attributes:
        desc (Union[Unset, str]):
        id (Union[Unset, str]):
        internal (Union[Unset, bool]):
        values (Union[Unset, List['RefData']]):
    """

    desc: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    internal: Union[Unset, bool] = UNSET
    values: Union[Unset, List["RefData"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        desc = self.desc
        id = self.id
        internal = self.internal
        values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()

                values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if desc is not UNSET:
            field_dict["desc"] = desc
        if id is not UNSET:
            field_dict["id"] = id
        if internal is not UNSET:
            field_dict["internal"] = internal
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ref_data import RefData

        d = src_dict.copy()
        desc = d.pop("desc", UNSET)

        id = d.pop("id", UNSET)

        internal = d.pop("internal", UNSET)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = RefData.from_dict(values_item_data)

            values.append(values_item)

        ref_data_category = cls(
            desc=desc,
            id=id,
            internal=internal,
            values=values,
        )

        ref_data_category.additional_properties = d
        return ref_data_category

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
