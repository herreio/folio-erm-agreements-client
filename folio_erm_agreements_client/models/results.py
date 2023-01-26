from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agreement import Agreement
    from ..models.custom_property import CustomProperty
    from ..models.entitlement import Entitlement
    from ..models.entitlement_option import EntitlementOption
    from ..models.erm_resource import ErmResource
    from ..models.internal_contact import InternalContact
    from ..models.job import Job
    from ..models.kb import Kb
    from ..models.log_entry import LogEntry
    from ..models.organisation import Organisation
    from ..models.package import Package
    from ..models.package_content_item import PackageContentItem
    from ..models.ref_data import RefData
    from ..models.ref_data_category import RefDataCategory
    from ..models.results_meta import ResultsMeta
    from ..models.string_template import StringTemplate


T = TypeVar("T", bound="Results")


@attr.s(auto_attribs=True)
class Results:
    """
    Attributes:
        results (List[Union['Agreement', 'CustomProperty', 'Entitlement', 'EntitlementOption', 'ErmResource',
            'InternalContact', 'Job', 'Kb', 'LogEntry', 'Organisation', 'Package', 'PackageContentItem', 'RefData',
            'RefDataCategory', 'StringTemplate']]):
        meta (Union[Unset, ResultsMeta]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        total (Union[Unset, int]):
        total_pages (Union[Unset, int]):
        total_records (Union[Unset, int]):
    """

    results: List[
        Union[
            "Agreement",
            "CustomProperty",
            "Entitlement",
            "EntitlementOption",
            "ErmResource",
            "InternalContact",
            "Job",
            "Kb",
            "LogEntry",
            "Organisation",
            "Package",
            "PackageContentItem",
            "RefData",
            "RefDataCategory",
            "StringTemplate",
        ]
    ]
    meta: Union[Unset, "ResultsMeta"] = UNSET
    page: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    total_pages: Union[Unset, int] = UNSET
    total_records: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.agreement import Agreement
        from ..models.custom_property import CustomProperty
        from ..models.entitlement import Entitlement
        from ..models.entitlement_option import EntitlementOption
        from ..models.erm_resource import ErmResource
        from ..models.internal_contact import InternalContact
        from ..models.job import Job
        from ..models.kb import Kb
        from ..models.log_entry import LogEntry
        from ..models.organisation import Organisation
        from ..models.package import Package
        from ..models.package_content_item import PackageContentItem
        from ..models.ref_data import RefData
        from ..models.ref_data_category import RefDataCategory

        results = []
        for componentsschemas_results_array_item_data in self.results:
            componentsschemas_results_array_item: Dict[str, Any]

            if isinstance(componentsschemas_results_array_item_data, Agreement):
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            elif isinstance(componentsschemas_results_array_item_data, CustomProperty):
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            elif isinstance(componentsschemas_results_array_item_data, Entitlement):
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            elif isinstance(componentsschemas_results_array_item_data, EntitlementOption):
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            elif isinstance(componentsschemas_results_array_item_data, ErmResource):
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            elif isinstance(componentsschemas_results_array_item_data, InternalContact):
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            elif isinstance(componentsschemas_results_array_item_data, Job):
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            elif isinstance(componentsschemas_results_array_item_data, Kb):
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            elif isinstance(componentsschemas_results_array_item_data, LogEntry):
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            elif isinstance(componentsschemas_results_array_item_data, Organisation):
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            elif isinstance(componentsschemas_results_array_item_data, Package):
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            elif isinstance(componentsschemas_results_array_item_data, PackageContentItem):
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            elif isinstance(componentsschemas_results_array_item_data, RefData):
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            elif isinstance(componentsschemas_results_array_item_data, RefDataCategory):
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            else:
                componentsschemas_results_array_item = componentsschemas_results_array_item_data.to_dict()

            results.append(componentsschemas_results_array_item)

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        page = self.page
        page_size = self.page_size
        total = self.total
        total_pages = self.total_pages
        total_records = self.total_records

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if total is not UNSET:
            field_dict["total"] = total
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if total_records is not UNSET:
            field_dict["totalRecords"] = total_records

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agreement import Agreement
        from ..models.custom_property import CustomProperty
        from ..models.entitlement import Entitlement
        from ..models.entitlement_option import EntitlementOption
        from ..models.erm_resource import ErmResource
        from ..models.internal_contact import InternalContact
        from ..models.job import Job
        from ..models.kb import Kb
        from ..models.log_entry import LogEntry
        from ..models.organisation import Organisation
        from ..models.package import Package
        from ..models.package_content_item import PackageContentItem
        from ..models.ref_data import RefData
        from ..models.ref_data_category import RefDataCategory
        from ..models.results_meta import ResultsMeta
        from ..models.string_template import StringTemplate

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for componentsschemas_results_array_item_data in _results:

            def _parse_componentsschemas_results_array_item(
                data: object,
            ) -> Union[
                "Agreement",
                "CustomProperty",
                "Entitlement",
                "EntitlementOption",
                "ErmResource",
                "InternalContact",
                "Job",
                "Kb",
                "LogEntry",
                "Organisation",
                "Package",
                "PackageContentItem",
                "RefData",
                "RefDataCategory",
                "StringTemplate",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_entity_type_0 = Agreement.from_dict(data)

                    return componentsschemas_entity_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_entity_type_1 = CustomProperty.from_dict(data)

                    return componentsschemas_entity_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_entity_type_2 = Entitlement.from_dict(data)

                    return componentsschemas_entity_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_entity_type_3 = EntitlementOption.from_dict(data)

                    return componentsschemas_entity_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_entity_type_4 = ErmResource.from_dict(data)

                    return componentsschemas_entity_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_entity_type_5 = InternalContact.from_dict(data)

                    return componentsschemas_entity_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_entity_type_6 = Job.from_dict(data)

                    return componentsschemas_entity_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_entity_type_7 = Kb.from_dict(data)

                    return componentsschemas_entity_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_entity_type_8 = LogEntry.from_dict(data)

                    return componentsschemas_entity_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_entity_type_9 = Organisation.from_dict(data)

                    return componentsschemas_entity_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_entity_type_10 = Package.from_dict(data)

                    return componentsschemas_entity_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_entity_type_11 = PackageContentItem.from_dict(data)

                    return componentsschemas_entity_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_entity_type_12 = RefData.from_dict(data)

                    return componentsschemas_entity_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_entity_type_13 = RefDataCategory.from_dict(data)

                    return componentsschemas_entity_type_13
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_entity_type_14 = StringTemplate.from_dict(data)

                return componentsschemas_entity_type_14

            componentsschemas_results_array_item = _parse_componentsschemas_results_array_item(
                componentsschemas_results_array_item_data
            )

            results.append(componentsschemas_results_array_item)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ResultsMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResultsMeta.from_dict(_meta)

        page = d.pop("page", UNSET)

        page_size = d.pop("pageSize", UNSET)

        total = d.pop("total", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        total_records = d.pop("totalRecords", UNSET)

        results = cls(
            results=results,
            meta=meta,
            page=page,
            page_size=page_size,
            total=total,
            total_pages=total_pages,
            total_records=total_records,
        )

        results.additional_properties = d
        return results

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
