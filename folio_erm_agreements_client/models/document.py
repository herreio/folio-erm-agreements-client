import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File
    from ..models.ref_data import RefData


T = TypeVar("T", bound="Document")


@attr.s(auto_attribs=True)
class Document:
    """
    Attributes:
        id (str):
        name (str):
        date_created (Union[Unset, datetime.datetime]):
        last_updated (Union[Unset, datetime.datetime]):
        location (Union[Unset, str]):
        url (Union[Unset, str]):
        note (Union[Unset, str]):
        at_type (Union['RefData', Unset, str]):
        file_upload (Union[Unset, File]):
    """

    id: str
    name: str
    date_created: Union[Unset, datetime.datetime] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    location: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    at_type: Union["RefData", Unset, str] = UNSET
    file_upload: Union[Unset, "File"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ref_data import RefData

        id = self.id
        name = self.name
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        location = self.location
        url = self.url
        note = self.note
        at_type: Union[Dict[str, Any], Unset, str]
        if isinstance(self.at_type, Unset):
            at_type = UNSET

        elif isinstance(self.at_type, RefData):
            at_type = UNSET
            if not isinstance(self.at_type, Unset):
                at_type = self.at_type.to_dict()

        else:
            at_type = self.at_type

        file_upload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file_upload, Unset):
            file_upload = self.file_upload.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if location is not UNSET:
            field_dict["location"] = location
        if url is not UNSET:
            field_dict["url"] = url
        if note is not UNSET:
            field_dict["note"] = note
        if at_type is not UNSET:
            field_dict["atType"] = at_type
        if file_upload is not UNSET:
            field_dict["fileUpload"] = file_upload

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file import File
        from ..models.ref_data import RefData

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        location = d.pop("location", UNSET)

        url = d.pop("url", UNSET)

        note = d.pop("note", UNSET)

        def _parse_at_type(data: object) -> Union["RefData", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _at_type_type_1 = data
                at_type_type_1: Union[Unset, RefData]
                if isinstance(_at_type_type_1, Unset):
                    at_type_type_1 = UNSET
                else:
                    at_type_type_1 = RefData.from_dict(_at_type_type_1)

                return at_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RefData", Unset, str], data)

        at_type = _parse_at_type(d.pop("atType", UNSET))

        _file_upload = d.pop("fileUpload", UNSET)
        file_upload: Union[Unset, File]
        if isinstance(_file_upload, Unset):
            file_upload = UNSET
        else:
            file_upload = File.from_dict(_file_upload)

        document = cls(
            id=id,
            name=name,
            date_created=date_created,
            last_updated=last_updated,
            location=location,
            url=url,
            note=note,
            at_type=at_type,
            file_upload=file_upload,
        )

        document.additional_properties = d
        return document

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
