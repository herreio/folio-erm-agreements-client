import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coverage_statement import CoverageStatement
    from ..models.identifier_occurrence import IdentifierOccurrence
    from ..models.ref_data import RefData
    from ..models.tag import Tag
    from ..models.title_instance_work import TitleInstanceWork


T = TypeVar("T", bound="TitleInstance")


@attr.s(auto_attribs=True)
class TitleInstance:
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
        date_monograph_published (Union[Unset, str]):
        first_author (Union[Unset, str]):
        first_editor (Union[Unset, str]):
        identifiers (Union[Unset, List['IdentifierOccurrence']]):
        long_name (Union[Unset, str]):
        monograph_edition (Union[Unset, str]):
        monograph_volume (Union[Unset, str]):
        work (Union[Unset, TitleInstanceWork]):
        related_titles (Union[Unset, List['TitleInstance']]):
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
    date_monograph_published: Union[Unset, str] = UNSET
    first_author: Union[Unset, str] = UNSET
    first_editor: Union[Unset, str] = UNSET
    identifiers: Union[Unset, List["IdentifierOccurrence"]] = UNSET
    long_name: Union[Unset, str] = UNSET
    monograph_edition: Union[Unset, str] = UNSET
    monograph_volume: Union[Unset, str] = UNSET
    work: Union[Unset, "TitleInstanceWork"] = UNSET
    related_titles: Union[Unset, List["TitleInstance"]] = UNSET
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

        date_monograph_published = self.date_monograph_published
        first_author = self.first_author
        first_editor = self.first_editor
        identifiers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = []
            for identifiers_item_data in self.identifiers:
                identifiers_item = identifiers_item_data.to_dict()

                identifiers.append(identifiers_item)

        long_name = self.long_name
        monograph_edition = self.monograph_edition
        monograph_volume = self.monograph_volume
        work: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.work, Unset):
            work = self.work.to_dict()

        related_titles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.related_titles, Unset):
            related_titles = []
            for related_titles_item_data in self.related_titles:
                related_titles_item = related_titles_item_data.to_dict()

                related_titles.append(related_titles_item)

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
        if date_monograph_published is not UNSET:
            field_dict["dateMonographPublished"] = date_monograph_published
        if first_author is not UNSET:
            field_dict["firstAuthor"] = first_author
        if first_editor is not UNSET:
            field_dict["firstEditor"] = first_editor
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if long_name is not UNSET:
            field_dict["longName"] = long_name
        if monograph_edition is not UNSET:
            field_dict["monographEdition"] = monograph_edition
        if monograph_volume is not UNSET:
            field_dict["monographVolume"] = monograph_volume
        if work is not UNSET:
            field_dict["work"] = work
        if related_titles is not UNSET:
            field_dict["relatedTitles"] = related_titles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coverage_statement import CoverageStatement
        from ..models.identifier_occurrence import IdentifierOccurrence
        from ..models.ref_data import RefData
        from ..models.tag import Tag
        from ..models.title_instance_work import TitleInstanceWork

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

        date_monograph_published = d.pop("dateMonographPublished", UNSET)

        first_author = d.pop("firstAuthor", UNSET)

        first_editor = d.pop("firstEditor", UNSET)

        identifiers = []
        _identifiers = d.pop("identifiers", UNSET)
        for identifiers_item_data in _identifiers or []:
            identifiers_item = IdentifierOccurrence.from_dict(identifiers_item_data)

            identifiers.append(identifiers_item)

        long_name = d.pop("longName", UNSET)

        monograph_edition = d.pop("monographEdition", UNSET)

        monograph_volume = d.pop("monographVolume", UNSET)

        _work = d.pop("work", UNSET)
        work: Union[Unset, TitleInstanceWork]
        if isinstance(_work, Unset):
            work = UNSET
        else:
            work = TitleInstanceWork.from_dict(_work)

        related_titles = []
        _related_titles = d.pop("relatedTitles", UNSET)
        for related_titles_item_data in _related_titles or []:
            related_titles_item = TitleInstance.from_dict(related_titles_item_data)

            related_titles.append(related_titles_item)

        title_instance = cls(
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
            date_monograph_published=date_monograph_published,
            first_author=first_author,
            first_editor=first_editor,
            identifiers=identifiers,
            long_name=long_name,
            monograph_edition=monograph_edition,
            monograph_volume=monograph_volume,
            work=work,
            related_titles=related_titles,
        )

        title_instance.additional_properties = d
        return title_instance

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
