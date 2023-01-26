import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ref_data import RefData


T = TypeVar("T", bound="Kb")


@attr.s(auto_attribs=True)
class Kb:
    """
    Attributes:
        activation_enabled (Union[Unset, bool]):
        active (Union[Unset, bool]):
        cursor (Union[Unset, datetime.datetime]):
        full_prefix (Union[Unset, str]):
        id (Union[Unset, str]):
        last_check (Union[Unset, int]):
        name (Union[Unset, str]):
        readonly (Union[Unset, bool]):
        rectype (Union[Unset, int]):
        supports_harvesting (Union[Unset, bool]):
        sync_status (Union['RefData', Unset, str]):
        trusted_source_ti (Union[Unset, bool]):
        type (Union[Unset, str]):
        uri (Union[Unset, str]):
    """

    activation_enabled: Union[Unset, bool] = UNSET
    active: Union[Unset, bool] = UNSET
    cursor: Union[Unset, datetime.datetime] = UNSET
    full_prefix: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_check: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    readonly: Union[Unset, bool] = UNSET
    rectype: Union[Unset, int] = UNSET
    supports_harvesting: Union[Unset, bool] = UNSET
    sync_status: Union["RefData", Unset, str] = UNSET
    trusted_source_ti: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    uri: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ref_data import RefData

        activation_enabled = self.activation_enabled
        active = self.active
        cursor: Union[Unset, str] = UNSET
        if not isinstance(self.cursor, Unset):
            cursor = self.cursor.isoformat()

        full_prefix = self.full_prefix
        id = self.id
        last_check = self.last_check
        name = self.name
        readonly = self.readonly
        rectype = self.rectype
        supports_harvesting = self.supports_harvesting
        sync_status: Union[Dict[str, Any], Unset, str]
        if isinstance(self.sync_status, Unset):
            sync_status = UNSET

        elif isinstance(self.sync_status, RefData):
            sync_status = UNSET
            if not isinstance(self.sync_status, Unset):
                sync_status = self.sync_status.to_dict()

        else:
            sync_status = self.sync_status

        trusted_source_ti = self.trusted_source_ti
        type = self.type
        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activation_enabled is not UNSET:
            field_dict["activationEnabled"] = activation_enabled
        if active is not UNSET:
            field_dict["active"] = active
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if full_prefix is not UNSET:
            field_dict["fullPrefix"] = full_prefix
        if id is not UNSET:
            field_dict["id"] = id
        if last_check is not UNSET:
            field_dict["lastCheck"] = last_check
        if name is not UNSET:
            field_dict["name"] = name
        if readonly is not UNSET:
            field_dict["readonly"] = readonly
        if rectype is not UNSET:
            field_dict["rectype"] = rectype
        if supports_harvesting is not UNSET:
            field_dict["supportsHarvesting"] = supports_harvesting
        if sync_status is not UNSET:
            field_dict["syncStatus"] = sync_status
        if trusted_source_ti is not UNSET:
            field_dict["trustedSourceTI"] = trusted_source_ti
        if type is not UNSET:
            field_dict["type"] = type
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ref_data import RefData

        d = src_dict.copy()
        activation_enabled = d.pop("activationEnabled", UNSET)

        active = d.pop("active", UNSET)

        _cursor = d.pop("cursor", UNSET)
        cursor: Union[Unset, datetime.datetime]
        if isinstance(_cursor, Unset):
            cursor = UNSET
        else:
            cursor = isoparse(_cursor)

        full_prefix = d.pop("fullPrefix", UNSET)

        id = d.pop("id", UNSET)

        last_check = d.pop("lastCheck", UNSET)

        name = d.pop("name", UNSET)

        readonly = d.pop("readonly", UNSET)

        rectype = d.pop("rectype", UNSET)

        supports_harvesting = d.pop("supportsHarvesting", UNSET)

        def _parse_sync_status(data: object) -> Union["RefData", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _sync_status_type_1 = data
                sync_status_type_1: Union[Unset, RefData]
                if isinstance(_sync_status_type_1, Unset):
                    sync_status_type_1 = UNSET
                else:
                    sync_status_type_1 = RefData.from_dict(_sync_status_type_1)

                return sync_status_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RefData", Unset, str], data)

        sync_status = _parse_sync_status(d.pop("syncStatus", UNSET))

        trusted_source_ti = d.pop("trustedSourceTI", UNSET)

        type = d.pop("type", UNSET)

        uri = d.pop("uri", UNSET)

        kb = cls(
            activation_enabled=activation_enabled,
            active=active,
            cursor=cursor,
            full_prefix=full_prefix,
            id=id,
            last_check=last_check,
            name=name,
            readonly=readonly,
            rectype=rectype,
            supports_harvesting=supports_harvesting,
            sync_status=sync_status,
            trusted_source_ti=trusted_source_ti,
            type=type,
            uri=uri,
        )

        kb.additional_properties = d
        return kb

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
