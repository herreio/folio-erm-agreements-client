from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_error_errors_item import ApplicationErrorErrorsItem


T = TypeVar("T", bound="ApplicationError")


@attr.s(auto_attribs=True)
class ApplicationError:
    """
    Attributes:
        total (Union[Unset, int]):
        errors (Union[Unset, List['ApplicationErrorErrorsItem']]):
    """

    total: Union[Unset, int] = UNSET
    errors: Union[Unset, List["ApplicationErrorErrorsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.application_error_errors_item import ApplicationErrorErrorsItem

        d = src_dict.copy()
        total = d.pop("total", UNSET)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ApplicationErrorErrorsItem.from_dict(errors_item_data)

            errors.append(errors_item)

        application_error = cls(
            total=total,
            errors=errors,
        )

        application_error.additional_properties = d
        return application_error

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
