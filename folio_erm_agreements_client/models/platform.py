import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.platform_locators_item import PlatformLocatorsItem


T = TypeVar("T", bound="Platform")


@attr.s(auto_attribs=True)
class Platform:
    """
    Attributes:
        name (str):
        id (Union[Unset, str]):
        date_created (Union[Unset, datetime.date]):
        last_updated (Union[Unset, datetime.date]):
        locators (Union[Unset, List['PlatformLocatorsItem']]):
    """

    name: str
    id: Union[Unset, str] = UNSET
    date_created: Union[Unset, datetime.date] = UNSET
    last_updated: Union[Unset, datetime.date] = UNSET
    locators: Union[Unset, List["PlatformLocatorsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        locators: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locators, Unset):
            locators = []
            for locators_item_data in self.locators:
                locators_item = locators_item_data.to_dict()

                locators.append(locators_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if locators is not UNSET:
            field_dict["locators"] = locators

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.platform_locators_item import PlatformLocatorsItem

        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.date]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created).date()

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.date]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated).date()

        locators = []
        _locators = d.pop("locators", UNSET)
        for locators_item_data in _locators or []:
            locators_item = PlatformLocatorsItem.from_dict(locators_item_data)

            locators.append(locators_item)

        platform = cls(
            name=name,
            id=id,
            date_created=date_created,
            last_updated=last_updated,
            locators=locators,
        )

        platform.additional_properties = d
        return platform

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
