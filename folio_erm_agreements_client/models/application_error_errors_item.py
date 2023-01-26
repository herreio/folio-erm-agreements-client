from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationErrorErrorsItem")


@attr.s(auto_attribs=True)
class ApplicationErrorErrorsItem:
    """
    Attributes:
        code (Union[Unset, str]):
        i18n_code (Union[Unset, str]):
        message (Union[Unset, str]):
        object_ (Union[Unset, str]):
    """

    code: Union[Unset, str] = UNSET
    i18n_code: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    object_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        i18n_code = self.i18n_code
        message = self.message
        object_ = self.object_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if i18n_code is not UNSET:
            field_dict["i18n_code"] = i18n_code
        if message is not UNSET:
            field_dict["message"] = message
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        i18n_code = d.pop("i18n_code", UNSET)

        message = d.pop("message", UNSET)

        object_ = d.pop("object", UNSET)

        application_error_errors_item = cls(
            code=code,
            i18n_code=i18n_code,
            message=message,
            object_=object_,
        )

        application_error_errors_item.additional_properties = d
        return application_error_errors_item

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
