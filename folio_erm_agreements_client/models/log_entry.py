from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_entry_additional_info import LogEntryAdditionalInfo


T = TypeVar("T", bound="LogEntry")


@attr.s(auto_attribs=True)
class LogEntry:
    """
    Attributes:
        additional_info (Union[Unset, LogEntryAdditionalInfo]):
        date_created (Union[Unset, int]):
        id (Union[Unset, str]):
        message (Union[Unset, str]):
        origin (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    additional_info: Union[Unset, "LogEntryAdditionalInfo"] = UNSET
    date_created: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    origin: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        additional_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_info, Unset):
            additional_info = self.additional_info.to_dict()

        date_created = self.date_created
        id = self.id
        message = self.message
        origin = self.origin
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_info is not UNSET:
            field_dict["additionalInfo"] = additional_info
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if origin is not UNSET:
            field_dict["origin"] = origin
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.log_entry_additional_info import LogEntryAdditionalInfo

        d = src_dict.copy()
        _additional_info = d.pop("additionalInfo", UNSET)
        additional_info: Union[Unset, LogEntryAdditionalInfo]
        if isinstance(_additional_info, Unset):
            additional_info = UNSET
        else:
            additional_info = LogEntryAdditionalInfo.from_dict(_additional_info)

        date_created = d.pop("dateCreated", UNSET)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        origin = d.pop("origin", UNSET)

        type = d.pop("type", UNSET)

        log_entry = cls(
            additional_info=additional_info,
            date_created=date_created,
            id=id,
            message=message,
            origin=origin,
            type=type,
        )

        log_entry.additional_properties = d
        return log_entry

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
