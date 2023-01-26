from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="PostErmFilesMultipartData")


@attr.s(auto_attribs=True)
class PostErmFilesMultipartData:
    """
    Attributes:
        name (Union[Unset, str]):
        filename (Union[Unset, File]):
    """

    name: Union[Unset, str] = UNSET
    filename: Union[Unset, File] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        filename: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.filename, Unset):
            filename = self.filename.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        filename: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.filename, Unset):
            filename = self.filename.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _filename = d.pop("filename", UNSET)
        filename: Union[Unset, File]
        if isinstance(_filename, Unset):
            filename = UNSET
        else:
            filename = File(payload=BytesIO(_filename))

        post_erm_files_multipart_data = cls(
            name=name,
            filename=filename,
        )

        post_erm_files_multipart_data.additional_properties = d
        return post_erm_files_multipart_data

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
