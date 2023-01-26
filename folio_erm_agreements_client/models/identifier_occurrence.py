from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifier import Identifier
    from ..models.identifier_occurrence_title import IdentifierOccurrenceTitle
    from ..models.ref_data import RefData


T = TypeVar("T", bound="IdentifierOccurrence")


@attr.s(auto_attribs=True)
class IdentifierOccurrence:
    """
    Attributes:
        title (Union[Unset, IdentifierOccurrenceTitle]):
        identifier (Union[Unset, Identifier]):
        status (Union[Unset, RefData]):
    """

    title: Union[Unset, "IdentifierOccurrenceTitle"] = UNSET
    identifier: Union[Unset, "Identifier"] = UNSET
    status: Union[Unset, "RefData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        identifier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.identifier import Identifier
        from ..models.identifier_occurrence_title import IdentifierOccurrenceTitle
        from ..models.ref_data import RefData

        d = src_dict.copy()
        _title = d.pop("title", UNSET)
        title: Union[Unset, IdentifierOccurrenceTitle]
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = IdentifierOccurrenceTitle.from_dict(_title)

        _identifier = d.pop("identifier", UNSET)
        identifier: Union[Unset, Identifier]
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = Identifier.from_dict(_identifier)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RefData]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RefData.from_dict(_status)

        identifier_occurrence = cls(
            title=title,
            identifier=identifier,
            status=status,
        )

        identifier_occurrence.additional_properties = d
        return identifier_occurrence

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
