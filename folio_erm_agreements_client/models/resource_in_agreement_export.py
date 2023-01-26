from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coverage_statement import CoverageStatement
    from ..models.entitlement import Entitlement
    from ..models.package import Package
    from ..models.platform import Platform
    from ..models.tag import Tag
    from ..models.title_instance import TitleInstance


T = TypeVar("T", bound="ResourceInAgreementExport")


@attr.s(auto_attribs=True)
class ResourceInAgreementExport:
    """
    Attributes:
        agreement_line (Union[Unset, Entitlement]):
        coverage (Union[Unset, List['CoverageStatement']]):
        custom_coverage (Union[Unset, bool]):
        depth (Union[Unset, str]):
        package (Union[Unset, Package]):
        platform (Union[Unset, Platform]):
        suppress_from_discovery (Union[Unset, bool]):
        tags (Union[Unset, List['Tag']]):
        title (Union[Unset, TitleInstance]):
        url (Union[Unset, str]):
    """

    agreement_line: Union[Unset, "Entitlement"] = UNSET
    coverage: Union[Unset, List["CoverageStatement"]] = UNSET
    custom_coverage: Union[Unset, bool] = UNSET
    depth: Union[Unset, str] = UNSET
    package: Union[Unset, "Package"] = UNSET
    platform: Union[Unset, "Platform"] = UNSET
    suppress_from_discovery: Union[Unset, bool] = UNSET
    tags: Union[Unset, List["Tag"]] = UNSET
    title: Union[Unset, "TitleInstance"] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agreement_line: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.agreement_line, Unset):
            agreement_line = self.agreement_line.to_dict()

        coverage: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.coverage, Unset):
            coverage = []
            for coverage_item_data in self.coverage:
                coverage_item = coverage_item_data.to_dict()

                coverage.append(coverage_item)

        custom_coverage = self.custom_coverage
        depth = self.depth
        package: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.package, Unset):
            package = self.package.to_dict()

        platform: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.to_dict()

        suppress_from_discovery = self.suppress_from_discovery
        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agreement_line is not UNSET:
            field_dict["agreementLine"] = agreement_line
        if coverage is not UNSET:
            field_dict["coverage"] = coverage
        if custom_coverage is not UNSET:
            field_dict["customCoverage"] = custom_coverage
        if depth is not UNSET:
            field_dict["depth"] = depth
        if package is not UNSET:
            field_dict["package"] = package
        if platform is not UNSET:
            field_dict["platform"] = platform
        if suppress_from_discovery is not UNSET:
            field_dict["suppressFromDiscovery"] = suppress_from_discovery
        if tags is not UNSET:
            field_dict["tags"] = tags
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coverage_statement import CoverageStatement
        from ..models.entitlement import Entitlement
        from ..models.package import Package
        from ..models.platform import Platform
        from ..models.tag import Tag
        from ..models.title_instance import TitleInstance

        d = src_dict.copy()
        _agreement_line = d.pop("agreementLine", UNSET)
        agreement_line: Union[Unset, Entitlement]
        if isinstance(_agreement_line, Unset):
            agreement_line = UNSET
        else:
            agreement_line = Entitlement.from_dict(_agreement_line)

        coverage = []
        _coverage = d.pop("coverage", UNSET)
        for coverage_item_data in _coverage or []:
            coverage_item = CoverageStatement.from_dict(coverage_item_data)

            coverage.append(coverage_item)

        custom_coverage = d.pop("customCoverage", UNSET)

        depth = d.pop("depth", UNSET)

        _package = d.pop("package", UNSET)
        package: Union[Unset, Package]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = Package.from_dict(_package)

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, Platform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = Platform.from_dict(_platform)

        suppress_from_discovery = d.pop("suppressFromDiscovery", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = Tag.from_dict(tags_item_data)

            tags.append(tags_item)

        _title = d.pop("title", UNSET)
        title: Union[Unset, TitleInstance]
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = TitleInstance.from_dict(_title)

        url = d.pop("url", UNSET)

        resource_in_agreement_export = cls(
            agreement_line=agreement_line,
            coverage=coverage,
            custom_coverage=custom_coverage,
            depth=depth,
            package=package,
            platform=platform,
            suppress_from_discovery=suppress_from_discovery,
            tags=tags,
            title=title,
            url=url,
        )

        resource_in_agreement_export.additional_properties = d
        return resource_in_agreement_export

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
