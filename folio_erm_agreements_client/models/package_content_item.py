import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coverage_statement import CoverageStatement
    from ..models.package import Package
    from ..models.platform_title_instance import PlatformTitleInstance
    from ..models.ref_data import RefData
    from ..models.tag import Tag


T = TypeVar("T", bound="PackageContentItem")


@attr.s(auto_attribs=True)
class PackageContentItem:
    """
    Attributes:
        id (Union[Unset, str]):
        class_ (Union[Unset, str]):
        coverage (Union[Unset, List['CoverageStatement']]):
        custom_coverage (Union[Unset, bool]):
        date_created (Union[Unset, datetime.datetime]):
        last_update (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        publication_type (Union['RefData', Unset, str]):
        suppress_from_discovery (Union[Unset, bool]):
        sub_type (Union['RefData', Unset, str]):
        tags (Union[Unset, List['Tag']]):
        type (Union['RefData', Unset, str]):
        access_start (Union[Unset, datetime.date]):
        added_timestamp (Union[Unset, int]):
        depth (Union[Unset, str]):
        last_seen_timestamp (Union[Unset, int]):
        long_name (Union[Unset, str]):
        pkg (Union[Unset, Package]):
        pti (Union[Unset, PlatformTitleInstance]):
    """

    id: Union[Unset, str] = UNSET
    class_: Union[Unset, str] = UNSET
    coverage: Union[Unset, List["CoverageStatement"]] = UNSET
    custom_coverage: Union[Unset, bool] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    last_update: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    publication_type: Union["RefData", Unset, str] = UNSET
    suppress_from_discovery: Union[Unset, bool] = UNSET
    sub_type: Union["RefData", Unset, str] = UNSET
    tags: Union[Unset, List["Tag"]] = UNSET
    type: Union["RefData", Unset, str] = UNSET
    access_start: Union[Unset, datetime.date] = UNSET
    added_timestamp: Union[Unset, int] = UNSET
    depth: Union[Unset, str] = UNSET
    last_seen_timestamp: Union[Unset, int] = UNSET
    long_name: Union[Unset, str] = UNSET
    pkg: Union[Unset, "Package"] = UNSET
    pti: Union[Unset, "PlatformTitleInstance"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ref_data import RefData

        id = self.id
        class_ = self.class_
        coverage: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.coverage, Unset):
            coverage = []
            for coverage_item_data in self.coverage:
                coverage_item = coverage_item_data.to_dict()

                coverage.append(coverage_item)

        custom_coverage = self.custom_coverage
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        last_update: Union[Unset, str] = UNSET
        if not isinstance(self.last_update, Unset):
            last_update = self.last_update.isoformat()

        name = self.name
        publication_type: Union[Dict[str, Any], Unset, str]
        if isinstance(self.publication_type, Unset):
            publication_type = UNSET

        elif isinstance(self.publication_type, RefData):
            publication_type = UNSET
            if not isinstance(self.publication_type, Unset):
                publication_type = self.publication_type.to_dict()

        else:
            publication_type = self.publication_type

        suppress_from_discovery = self.suppress_from_discovery
        sub_type: Union[Dict[str, Any], Unset, str]
        if isinstance(self.sub_type, Unset):
            sub_type = UNSET

        elif isinstance(self.sub_type, RefData):
            sub_type = UNSET
            if not isinstance(self.sub_type, Unset):
                sub_type = self.sub_type.to_dict()

        else:
            sub_type = self.sub_type

        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        type: Union[Dict[str, Any], Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET

        elif isinstance(self.type, RefData):
            type = UNSET
            if not isinstance(self.type, Unset):
                type = self.type.to_dict()

        else:
            type = self.type

        access_start: Union[Unset, str] = UNSET
        if not isinstance(self.access_start, Unset):
            access_start = self.access_start.isoformat()

        added_timestamp = self.added_timestamp
        depth = self.depth
        last_seen_timestamp = self.last_seen_timestamp
        long_name = self.long_name
        pkg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pkg, Unset):
            pkg = self.pkg.to_dict()

        pti: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pti, Unset):
            pti = self.pti.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if class_ is not UNSET:
            field_dict["class"] = class_
        if coverage is not UNSET:
            field_dict["coverage"] = coverage
        if custom_coverage is not UNSET:
            field_dict["customCoverage"] = custom_coverage
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_update is not UNSET:
            field_dict["lastUpdate"] = last_update
        if name is not UNSET:
            field_dict["name"] = name
        if publication_type is not UNSET:
            field_dict["publicationType"] = publication_type
        if suppress_from_discovery is not UNSET:
            field_dict["suppressFromDiscovery"] = suppress_from_discovery
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type is not UNSET:
            field_dict["type"] = type
        if access_start is not UNSET:
            field_dict["accessStart"] = access_start
        if added_timestamp is not UNSET:
            field_dict["addedTimestamp"] = added_timestamp
        if depth is not UNSET:
            field_dict["depth"] = depth
        if last_seen_timestamp is not UNSET:
            field_dict["lastSeenTimestamp"] = last_seen_timestamp
        if long_name is not UNSET:
            field_dict["longName"] = long_name
        if pkg is not UNSET:
            field_dict["pkg"] = pkg
        if pti is not UNSET:
            field_dict["pti"] = pti

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coverage_statement import CoverageStatement
        from ..models.package import Package
        from ..models.platform_title_instance import PlatformTitleInstance
        from ..models.ref_data import RefData
        from ..models.tag import Tag

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        class_ = d.pop("class", UNSET)

        coverage = []
        _coverage = d.pop("coverage", UNSET)
        for coverage_item_data in _coverage or []:
            coverage_item = CoverageStatement.from_dict(coverage_item_data)

            coverage.append(coverage_item)

        custom_coverage = d.pop("customCoverage", UNSET)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _last_update = d.pop("lastUpdate", UNSET)
        last_update: Union[Unset, datetime.datetime]
        if isinstance(_last_update, Unset):
            last_update = UNSET
        else:
            last_update = isoparse(_last_update)

        name = d.pop("name", UNSET)

        def _parse_publication_type(data: object) -> Union["RefData", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _publication_type_type_1 = data
                publication_type_type_1: Union[Unset, RefData]
                if isinstance(_publication_type_type_1, Unset):
                    publication_type_type_1 = UNSET
                else:
                    publication_type_type_1 = RefData.from_dict(_publication_type_type_1)

                return publication_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RefData", Unset, str], data)

        publication_type = _parse_publication_type(d.pop("publicationType", UNSET))

        suppress_from_discovery = d.pop("suppressFromDiscovery", UNSET)

        def _parse_sub_type(data: object) -> Union["RefData", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _sub_type_type_1 = data
                sub_type_type_1: Union[Unset, RefData]
                if isinstance(_sub_type_type_1, Unset):
                    sub_type_type_1 = UNSET
                else:
                    sub_type_type_1 = RefData.from_dict(_sub_type_type_1)

                return sub_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RefData", Unset, str], data)

        sub_type = _parse_sub_type(d.pop("subType", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = Tag.from_dict(tags_item_data)

            tags.append(tags_item)

        def _parse_type(data: object) -> Union["RefData", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _type_type_1 = data
                type_type_1: Union[Unset, RefData]
                if isinstance(_type_type_1, Unset):
                    type_type_1 = UNSET
                else:
                    type_type_1 = RefData.from_dict(_type_type_1)

                return type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RefData", Unset, str], data)

        type = _parse_type(d.pop("type", UNSET))

        _access_start = d.pop("accessStart", UNSET)
        access_start: Union[Unset, datetime.date]
        if isinstance(_access_start, Unset):
            access_start = UNSET
        else:
            access_start = isoparse(_access_start).date()

        added_timestamp = d.pop("addedTimestamp", UNSET)

        depth = d.pop("depth", UNSET)

        last_seen_timestamp = d.pop("lastSeenTimestamp", UNSET)

        long_name = d.pop("longName", UNSET)

        _pkg = d.pop("pkg", UNSET)
        pkg: Union[Unset, Package]
        if isinstance(_pkg, Unset):
            pkg = UNSET
        else:
            pkg = Package.from_dict(_pkg)

        _pti = d.pop("pti", UNSET)
        pti: Union[Unset, PlatformTitleInstance]
        if isinstance(_pti, Unset):
            pti = UNSET
        else:
            pti = PlatformTitleInstance.from_dict(_pti)

        package_content_item = cls(
            id=id,
            class_=class_,
            coverage=coverage,
            custom_coverage=custom_coverage,
            date_created=date_created,
            last_update=last_update,
            name=name,
            publication_type=publication_type,
            suppress_from_discovery=suppress_from_discovery,
            sub_type=sub_type,
            tags=tags,
            type=type,
            access_start=access_start,
            added_timestamp=added_timestamp,
            depth=depth,
            last_seen_timestamp=last_seen_timestamp,
            long_name=long_name,
            pkg=pkg,
            pti=pti,
        )

        package_content_item.additional_properties = d
        return package_content_item

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
