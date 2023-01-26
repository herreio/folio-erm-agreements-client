from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organisation_orgs_uuid_object import OrganisationOrgsUuidObject


T = TypeVar("T", bound="Organisation")


@attr.s(auto_attribs=True)
class Organisation:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        orgs_uuid (Union[Unset, str]):
        orgs_uuid_object (Union[Unset, OrganisationOrgsUuidObject]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    orgs_uuid: Union[Unset, str] = UNSET
    orgs_uuid_object: Union[Unset, "OrganisationOrgsUuidObject"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        orgs_uuid = self.orgs_uuid
        orgs_uuid_object: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.orgs_uuid_object, Unset):
            orgs_uuid_object = self.orgs_uuid_object.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if orgs_uuid is not UNSET:
            field_dict["orgsUuid"] = orgs_uuid
        if orgs_uuid_object is not UNSET:
            field_dict["orgsUuid_object"] = orgs_uuid_object

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organisation_orgs_uuid_object import OrganisationOrgsUuidObject

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        orgs_uuid = d.pop("orgsUuid", UNSET)

        _orgs_uuid_object = d.pop("orgsUuid_object", UNSET)
        orgs_uuid_object: Union[Unset, OrganisationOrgsUuidObject]
        if isinstance(_orgs_uuid_object, Unset):
            orgs_uuid_object = UNSET
        else:
            orgs_uuid_object = OrganisationOrgsUuidObject.from_dict(_orgs_uuid_object)

        organisation = cls(
            id=id,
            name=name,
            orgs_uuid=orgs_uuid,
            orgs_uuid_object=orgs_uuid_object,
        )

        organisation.additional_properties = d
        return organisation

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
