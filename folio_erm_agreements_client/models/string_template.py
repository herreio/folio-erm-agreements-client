import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ref_data import RefData


T = TypeVar("T", bound="StringTemplate")


@attr.s(auto_attribs=True)
class StringTemplate:
    """
    Attributes:
        id (Union[Unset, str]):
        date_created (Union[Unset, int]):
        rule (Union[Unset, str]):
        context (Union['RefData', Unset, str]):
        last_updated (Union[Unset, datetime.date]):
        name (Union[Unset, str]):
        id_scopes (Union[Unset, List[str]]):
    """

    id: Union[Unset, str] = UNSET
    date_created: Union[Unset, int] = UNSET
    rule: Union[Unset, str] = UNSET
    context: Union["RefData", Unset, str] = UNSET
    last_updated: Union[Unset, datetime.date] = UNSET
    name: Union[Unset, str] = UNSET
    id_scopes: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ref_data import RefData

        id = self.id
        date_created = self.date_created
        rule = self.rule
        context: Union[Dict[str, Any], Unset, str]
        if isinstance(self.context, Unset):
            context = UNSET

        elif isinstance(self.context, RefData):
            context = UNSET
            if not isinstance(self.context, Unset):
                context = self.context.to_dict()

        else:
            context = self.context

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        name = self.name
        id_scopes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.id_scopes, Unset):
            id_scopes = self.id_scopes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if rule is not UNSET:
            field_dict["rule"] = rule
        if context is not UNSET:
            field_dict["context"] = context
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if name is not UNSET:
            field_dict["name"] = name
        if id_scopes is not UNSET:
            field_dict["idScopes"] = id_scopes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ref_data import RefData

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        rule = d.pop("rule", UNSET)

        def _parse_context(data: object) -> Union["RefData", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _context_type_1 = data
                context_type_1: Union[Unset, RefData]
                if isinstance(_context_type_1, Unset):
                    context_type_1 = UNSET
                else:
                    context_type_1 = RefData.from_dict(_context_type_1)

                return context_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RefData", Unset, str], data)

        context = _parse_context(d.pop("context", UNSET))

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.date]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated).date()

        name = d.pop("name", UNSET)

        id_scopes = cast(List[str], d.pop("idScopes", UNSET))

        string_template = cls(
            id=id,
            date_created=date_created,
            rule=rule,
            context=context,
            last_updated=last_updated,
            name=name,
            id_scopes=id_scopes,
        )

        string_template.additional_properties = d
        return string_template

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
