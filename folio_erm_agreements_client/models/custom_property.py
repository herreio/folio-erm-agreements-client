from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ref_data_category import RefDataCategory


T = TypeVar("T", bound="CustomProperty")


@attr.s(auto_attribs=True)
class CustomProperty:
    """
    Attributes:
        default_internal (Union[Unset, bool]):
        description (Union[Unset, str]):
        id (Union[Unset, str]):
        label (Union[Unset, str]):
        name (Union[Unset, str]):
        primary (Union[Unset, bool]):
        type (Union[Unset, str]):
        weight (Union[Unset, int]):
        category (Union[Unset, RefDataCategory]):
    """

    default_internal: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    primary: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    weight: Union[Unset, int] = UNSET
    category: Union[Unset, "RefDataCategory"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_internal = self.default_internal
        description = self.description
        id = self.id
        label = self.label
        name = self.name
        primary = self.primary
        type = self.type
        weight = self.weight
        category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_internal is not UNSET:
            field_dict["defaultInternal"] = default_internal
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if name is not UNSET:
            field_dict["name"] = name
        if primary is not UNSET:
            field_dict["primary"] = primary
        if type is not UNSET:
            field_dict["type"] = type
        if weight is not UNSET:
            field_dict["weight"] = weight
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ref_data_category import RefDataCategory

        d = src_dict.copy()
        default_internal = d.pop("defaultInternal", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        name = d.pop("name", UNSET)

        primary = d.pop("primary", UNSET)

        type = d.pop("type", UNSET)

        weight = d.pop("weight", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, RefDataCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = RefDataCategory.from_dict(_category)

        custom_property = cls(
            default_internal=default_internal,
            description=description,
            id=id,
            label=label,
            name=name,
            primary=primary,
            type=type,
            weight=weight,
            category=category,
        )

        custom_property.additional_properties = d
        return custom_property

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
