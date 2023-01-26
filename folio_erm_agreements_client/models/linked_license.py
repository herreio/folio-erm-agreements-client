from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linked_amendment import LinkedAmendment
    from ..models.linked_license_remote_id_object import LinkedLicenseRemoteIdObject
    from ..models.ref_data import RefData


T = TypeVar("T", bound="LinkedLicense")


@attr.s(auto_attribs=True)
class LinkedLicense:
    """
    Attributes:
        amendments (Union[Unset, List['LinkedAmendment']]):
        id (Union[Unset, str]):
        owner (Union[Unset, str]):
        remote_id (Union[Unset, str]):
        remote_id_object (Union[Unset, LinkedLicenseRemoteIdObject]):
        status (Union['RefData', Unset, str]):
    """

    amendments: Union[Unset, List["LinkedAmendment"]] = UNSET
    id: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    remote_id: Union[Unset, str] = UNSET
    remote_id_object: Union[Unset, "LinkedLicenseRemoteIdObject"] = UNSET
    status: Union["RefData", Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ref_data import RefData

        amendments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.amendments, Unset):
            amendments = []
            for amendments_item_data in self.amendments:
                amendments_item = amendments_item_data.to_dict()

                amendments.append(amendments_item)

        id = self.id
        owner = self.owner
        remote_id = self.remote_id
        remote_id_object: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remote_id_object, Unset):
            remote_id_object = self.remote_id_object.to_dict()

        status: Union[Dict[str, Any], Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET

        elif isinstance(self.status, RefData):
            status = UNSET
            if not isinstance(self.status, Unset):
                status = self.status.to_dict()

        else:
            status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amendments is not UNSET:
            field_dict["amendments"] = amendments
        if id is not UNSET:
            field_dict["id"] = id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if remote_id is not UNSET:
            field_dict["remoteId"] = remote_id
        if remote_id_object is not UNSET:
            field_dict["remoteId_object"] = remote_id_object
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.linked_amendment import LinkedAmendment
        from ..models.linked_license_remote_id_object import LinkedLicenseRemoteIdObject
        from ..models.ref_data import RefData

        d = src_dict.copy()
        amendments = []
        _amendments = d.pop("amendments", UNSET)
        for amendments_item_data in _amendments or []:
            amendments_item = LinkedAmendment.from_dict(amendments_item_data)

            amendments.append(amendments_item)

        id = d.pop("id", UNSET)

        owner = d.pop("owner", UNSET)

        remote_id = d.pop("remoteId", UNSET)

        _remote_id_object = d.pop("remoteId_object", UNSET)
        remote_id_object: Union[Unset, LinkedLicenseRemoteIdObject]
        if isinstance(_remote_id_object, Unset):
            remote_id_object = UNSET
        else:
            remote_id_object = LinkedLicenseRemoteIdObject.from_dict(_remote_id_object)

        def _parse_status(data: object) -> Union["RefData", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _status_type_1 = data
                status_type_1: Union[Unset, RefData]
                if isinstance(_status_type_1, Unset):
                    status_type_1 = UNSET
                else:
                    status_type_1 = RefData.from_dict(_status_type_1)

                return status_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RefData", Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        linked_license = cls(
            amendments=amendments,
            id=id,
            owner=owner,
            remote_id=remote_id,
            remote_id_object=remote_id_object,
            status=status,
        )

        linked_license.additional_properties = d
        return linked_license

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
