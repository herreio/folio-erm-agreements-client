import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agreement import Agreement
    from ..models.coverage_statement import CoverageStatement
    from ..models.entitlement_option import EntitlementOption
    from ..models.purchase_order_line import PurchaseOrderLine
    from ..models.tag import Tag


T = TypeVar("T", bound="Entitlement")


@attr.s(auto_attribs=True)
class Entitlement:
    """
    Attributes:
        id (Union[Unset, str]):
        active_from (Union[Unset, datetime.date]):
        active_to (Union[Unset, datetime.date]):
        custom_coverage (Union[Unset, bool]):
        coverage (Union[Unset, List['CoverageStatement']]):
        explanation (Union[Unset, str]):
        have_access (Union[Unset, bool]):
        note (Union[Unset, str]):
        description (Union[Unset, str]):
        owner (Union[Unset, Agreement]):
        po_lines (Union[Unset, List['PurchaseOrderLine']]):
        resource (Union[Unset, EntitlementOption]):
        suppress_from_discovery (Union[Unset, bool]):
        tags (Union[Unset, List['Tag']]):
    """

    id: Union[Unset, str] = UNSET
    active_from: Union[Unset, datetime.date] = UNSET
    active_to: Union[Unset, datetime.date] = UNSET
    custom_coverage: Union[Unset, bool] = UNSET
    coverage: Union[Unset, List["CoverageStatement"]] = UNSET
    explanation: Union[Unset, str] = UNSET
    have_access: Union[Unset, bool] = UNSET
    note: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    owner: Union[Unset, "Agreement"] = UNSET
    po_lines: Union[Unset, List["PurchaseOrderLine"]] = UNSET
    resource: Union[Unset, "EntitlementOption"] = UNSET
    suppress_from_discovery: Union[Unset, bool] = UNSET
    tags: Union[Unset, List["Tag"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        active_from: Union[Unset, str] = UNSET
        if not isinstance(self.active_from, Unset):
            active_from = self.active_from.isoformat()

        active_to: Union[Unset, str] = UNSET
        if not isinstance(self.active_to, Unset):
            active_to = self.active_to.isoformat()

        custom_coverage = self.custom_coverage
        coverage: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.coverage, Unset):
            coverage = []
            for coverage_item_data in self.coverage:
                coverage_item = coverage_item_data.to_dict()

                coverage.append(coverage_item)

        explanation = self.explanation
        have_access = self.have_access
        note = self.note
        description = self.description
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        po_lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.po_lines, Unset):
            po_lines = []
            for po_lines_item_data in self.po_lines:
                po_lines_item = po_lines_item_data.to_dict()

                po_lines.append(po_lines_item)

        resource: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        suppress_from_discovery = self.suppress_from_discovery
        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if active_from is not UNSET:
            field_dict["activeFrom"] = active_from
        if active_to is not UNSET:
            field_dict["activeTo"] = active_to
        if custom_coverage is not UNSET:
            field_dict["customCoverage"] = custom_coverage
        if coverage is not UNSET:
            field_dict["coverage"] = coverage
        if explanation is not UNSET:
            field_dict["explanation"] = explanation
        if have_access is not UNSET:
            field_dict["haveAccess"] = have_access
        if note is not UNSET:
            field_dict["note"] = note
        if description is not UNSET:
            field_dict["description"] = description
        if owner is not UNSET:
            field_dict["owner"] = owner
        if po_lines is not UNSET:
            field_dict["poLines"] = po_lines
        if resource is not UNSET:
            field_dict["resource"] = resource
        if suppress_from_discovery is not UNSET:
            field_dict["suppressFromDiscovery"] = suppress_from_discovery
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agreement import Agreement
        from ..models.coverage_statement import CoverageStatement
        from ..models.entitlement_option import EntitlementOption
        from ..models.purchase_order_line import PurchaseOrderLine
        from ..models.tag import Tag

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _active_from = d.pop("activeFrom", UNSET)
        active_from: Union[Unset, datetime.date]
        if isinstance(_active_from, Unset):
            active_from = UNSET
        else:
            active_from = isoparse(_active_from).date()

        _active_to = d.pop("activeTo", UNSET)
        active_to: Union[Unset, datetime.date]
        if isinstance(_active_to, Unset):
            active_to = UNSET
        else:
            active_to = isoparse(_active_to).date()

        custom_coverage = d.pop("customCoverage", UNSET)

        coverage = []
        _coverage = d.pop("coverage", UNSET)
        for coverage_item_data in _coverage or []:
            coverage_item = CoverageStatement.from_dict(coverage_item_data)

            coverage.append(coverage_item)

        explanation = d.pop("explanation", UNSET)

        have_access = d.pop("haveAccess", UNSET)

        note = d.pop("note", UNSET)

        description = d.pop("description", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, Agreement]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = Agreement.from_dict(_owner)

        po_lines = []
        _po_lines = d.pop("poLines", UNSET)
        for po_lines_item_data in _po_lines or []:
            po_lines_item = PurchaseOrderLine.from_dict(po_lines_item_data)

            po_lines.append(po_lines_item)

        _resource = d.pop("resource", UNSET)
        resource: Union[Unset, EntitlementOption]
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = EntitlementOption.from_dict(_resource)

        suppress_from_discovery = d.pop("suppressFromDiscovery", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = Tag.from_dict(tags_item_data)

            tags.append(tags_item)

        entitlement = cls(
            id=id,
            active_from=active_from,
            active_to=active_to,
            custom_coverage=custom_coverage,
            coverage=coverage,
            explanation=explanation,
            have_access=have_access,
            note=note,
            description=description,
            owner=owner,
            po_lines=po_lines,
            resource=resource,
            suppress_from_discovery=suppress_from_discovery,
            tags=tags,
        )

        entitlement.additional_properties = d
        return entitlement

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
