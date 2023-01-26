from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package import Package
    from ..models.package_content_item import PackageContentItem
    from ..models.platform_title_instance import PlatformTitleInstance
    from ..models.title_instance import TitleInstance


T = TypeVar("T", bound="EntitlementOption")


@attr.s(auto_attribs=True)
class EntitlementOption:
    """
    Attributes:
        field_object_ (Union['Package', 'PackageContentItem', 'PlatformTitleInstance', 'TitleInstance', Unset]):
    """

    field_object_: Union["Package", "PackageContentItem", "PlatformTitleInstance", "TitleInstance", Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.package_content_item import PackageContentItem
        from ..models.platform_title_instance import PlatformTitleInstance
        from ..models.title_instance import TitleInstance

        field_object_: Union[Dict[str, Any], Unset]
        if isinstance(self.field_object_, Unset):
            field_object_ = UNSET

        elif isinstance(self.field_object_, TitleInstance):
            field_object_ = UNSET
            if not isinstance(self.field_object_, Unset):
                field_object_ = self.field_object_.to_dict()

        elif isinstance(self.field_object_, PlatformTitleInstance):
            field_object_ = UNSET
            if not isinstance(self.field_object_, Unset):
                field_object_ = self.field_object_.to_dict()

        elif isinstance(self.field_object_, PackageContentItem):
            field_object_ = UNSET
            if not isinstance(self.field_object_, Unset):
                field_object_ = self.field_object_.to_dict()

        else:
            field_object_ = UNSET
            if not isinstance(self.field_object_, Unset):
                field_object_ = self.field_object_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_object_ is not UNSET:
            field_dict["_object"] = field_object_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package import Package
        from ..models.package_content_item import PackageContentItem
        from ..models.platform_title_instance import PlatformTitleInstance
        from ..models.title_instance import TitleInstance

        d = src_dict.copy()

        def _parse_field_object_(
            data: object,
        ) -> Union["Package", "PackageContentItem", "PlatformTitleInstance", "TitleInstance", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _field_object_type_0 = data
                field_object_type_0: Union[Unset, TitleInstance]
                if isinstance(_field_object_type_0, Unset):
                    field_object_type_0 = UNSET
                else:
                    field_object_type_0 = TitleInstance.from_dict(_field_object_type_0)

                return field_object_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _field_object_type_1 = data
                field_object_type_1: Union[Unset, PlatformTitleInstance]
                if isinstance(_field_object_type_1, Unset):
                    field_object_type_1 = UNSET
                else:
                    field_object_type_1 = PlatformTitleInstance.from_dict(_field_object_type_1)

                return field_object_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _field_object_type_2 = data
                field_object_type_2: Union[Unset, PackageContentItem]
                if isinstance(_field_object_type_2, Unset):
                    field_object_type_2 = UNSET
                else:
                    field_object_type_2 = PackageContentItem.from_dict(_field_object_type_2)

                return field_object_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _field_object_type_3 = data
            field_object_type_3: Union[Unset, Package]
            if isinstance(_field_object_type_3, Unset):
                field_object_type_3 = UNSET
            else:
                field_object_type_3 = Package.from_dict(_field_object_type_3)

            return field_object_type_3

        field_object_ = _parse_field_object_(d.pop("_object", UNSET))

        entitlement_option = cls(
            field_object_=field_object_,
        )

        entitlement_option.additional_properties = d
        return entitlement_option

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
