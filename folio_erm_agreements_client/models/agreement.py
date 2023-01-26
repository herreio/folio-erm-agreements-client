import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agreement_periods_item import AgreementPeriodsItem
    from ..models.document import Document
    from ..models.internal_contact import InternalContact
    from ..models.linked_license import LinkedLicense
    from ..models.organisation import Organisation
    from ..models.ref_data import RefData
    from ..models.tag import Tag
    from ..models.usage_data_provider import UsageDataProvider


T = TypeVar("T", bound="Agreement")


@attr.s(auto_attribs=True)
class Agreement:
    """
    Attributes:
        id (str):
        name (str):
        status (Union['RefData', str]):
        description (Union[Unset, str]):
        is_perpetual (Union['RefData', Unset, str]):
        reason_for_closure (Union['RefData', Unset, str]):
        renewal_priority (Union['RefData', Unset, str]):
        alternate_names (Union[Unset, List[str]]):
        periods (Union[Unset, List['AgreementPeriodsItem']]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        cancellation_deadline (Union[Unset, datetime.date]):
        contacts (Union[Unset, List['InternalContact']]):
        orgs (Union[Unset, List['Organisation']]):
        external_license_docs (Union[Unset, List['Document']]):
        supplementary_docs (Union[Unset, List['Document']]):
        linked_licenses (Union[Unset, List['LinkedLicense']]):
        usage_data_providers (Union[Unset, List['UsageDataProvider']]):
        tags (Union[Unset, List['Tag']]):
    """

    id: str
    name: str
    status: Union["RefData", str]
    description: Union[Unset, str] = UNSET
    is_perpetual: Union["RefData", Unset, str] = UNSET
    reason_for_closure: Union["RefData", Unset, str] = UNSET
    renewal_priority: Union["RefData", Unset, str] = UNSET
    alternate_names: Union[Unset, List[str]] = UNSET
    periods: Union[Unset, List["AgreementPeriodsItem"]] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    cancellation_deadline: Union[Unset, datetime.date] = UNSET
    contacts: Union[Unset, List["InternalContact"]] = UNSET
    orgs: Union[Unset, List["Organisation"]] = UNSET
    external_license_docs: Union[Unset, List["Document"]] = UNSET
    supplementary_docs: Union[Unset, List["Document"]] = UNSET
    linked_licenses: Union[Unset, List["LinkedLicense"]] = UNSET
    usage_data_providers: Union[Unset, List["UsageDataProvider"]] = UNSET
    tags: Union[Unset, List["Tag"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ref_data import RefData

        id = self.id
        name = self.name
        status: Union[Dict[str, Any], str]

        if isinstance(self.status, RefData):
            status = self.status.to_dict()

        else:
            status = self.status

        description = self.description
        is_perpetual: Union[Dict[str, Any], Unset, str]
        if isinstance(self.is_perpetual, Unset):
            is_perpetual = UNSET

        elif isinstance(self.is_perpetual, RefData):
            is_perpetual = UNSET
            if not isinstance(self.is_perpetual, Unset):
                is_perpetual = self.is_perpetual.to_dict()

        else:
            is_perpetual = self.is_perpetual

        reason_for_closure: Union[Dict[str, Any], Unset, str]
        if isinstance(self.reason_for_closure, Unset):
            reason_for_closure = UNSET

        elif isinstance(self.reason_for_closure, RefData):
            reason_for_closure = UNSET
            if not isinstance(self.reason_for_closure, Unset):
                reason_for_closure = self.reason_for_closure.to_dict()

        else:
            reason_for_closure = self.reason_for_closure

        renewal_priority: Union[Dict[str, Any], Unset, str]
        if isinstance(self.renewal_priority, Unset):
            renewal_priority = UNSET

        elif isinstance(self.renewal_priority, RefData):
            renewal_priority = UNSET
            if not isinstance(self.renewal_priority, Unset):
                renewal_priority = self.renewal_priority.to_dict()

        else:
            renewal_priority = self.renewal_priority

        alternate_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.alternate_names, Unset):
            alternate_names = self.alternate_names

        periods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()

                periods.append(periods_item)

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        cancellation_deadline: Union[Unset, str] = UNSET
        if not isinstance(self.cancellation_deadline, Unset):
            cancellation_deadline = self.cancellation_deadline.isoformat()

        contacts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()

                contacts.append(contacts_item)

        orgs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.orgs, Unset):
            orgs = []
            for orgs_item_data in self.orgs:
                orgs_item = orgs_item_data.to_dict()

                orgs.append(orgs_item)

        external_license_docs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.external_license_docs, Unset):
            external_license_docs = []
            for external_license_docs_item_data in self.external_license_docs:
                external_license_docs_item = external_license_docs_item_data.to_dict()

                external_license_docs.append(external_license_docs_item)

        supplementary_docs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.supplementary_docs, Unset):
            supplementary_docs = []
            for supplementary_docs_item_data in self.supplementary_docs:
                supplementary_docs_item = supplementary_docs_item_data.to_dict()

                supplementary_docs.append(supplementary_docs_item)

        linked_licenses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.linked_licenses, Unset):
            linked_licenses = []
            for linked_licenses_item_data in self.linked_licenses:
                linked_licenses_item = linked_licenses_item_data.to_dict()

                linked_licenses.append(linked_licenses_item)

        usage_data_providers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.usage_data_providers, Unset):
            usage_data_providers = []
            for usage_data_providers_item_data in self.usage_data_providers:
                usage_data_providers_item = usage_data_providers_item_data.to_dict()

                usage_data_providers.append(usage_data_providers_item)

        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_perpetual is not UNSET:
            field_dict["isPerpetual"] = is_perpetual
        if reason_for_closure is not UNSET:
            field_dict["reasonForClosure"] = reason_for_closure
        if renewal_priority is not UNSET:
            field_dict["renewalPriority"] = renewal_priority
        if alternate_names is not UNSET:
            field_dict["alternateNames"] = alternate_names
        if periods is not UNSET:
            field_dict["periods"] = periods
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if cancellation_deadline is not UNSET:
            field_dict["cancellationDeadline"] = cancellation_deadline
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if orgs is not UNSET:
            field_dict["orgs"] = orgs
        if external_license_docs is not UNSET:
            field_dict["externalLicenseDocs"] = external_license_docs
        if supplementary_docs is not UNSET:
            field_dict["supplementaryDocs"] = supplementary_docs
        if linked_licenses is not UNSET:
            field_dict["linkedLicenses"] = linked_licenses
        if usage_data_providers is not UNSET:
            field_dict["usageDataProviders"] = usage_data_providers
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agreement_periods_item import AgreementPeriodsItem
        from ..models.document import Document
        from ..models.internal_contact import InternalContact
        from ..models.linked_license import LinkedLicense
        from ..models.organisation import Organisation
        from ..models.ref_data import RefData
        from ..models.tag import Tag
        from ..models.usage_data_provider import UsageDataProvider

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        def _parse_status(data: object) -> Union["RefData", str]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = RefData.from_dict(data)

                return status_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RefData", str], data)

        status = _parse_status(d.pop("status"))

        description = d.pop("description", UNSET)

        def _parse_is_perpetual(data: object) -> Union["RefData", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _is_perpetual_type_1 = data
                is_perpetual_type_1: Union[Unset, RefData]
                if isinstance(_is_perpetual_type_1, Unset):
                    is_perpetual_type_1 = UNSET
                else:
                    is_perpetual_type_1 = RefData.from_dict(_is_perpetual_type_1)

                return is_perpetual_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RefData", Unset, str], data)

        is_perpetual = _parse_is_perpetual(d.pop("isPerpetual", UNSET))

        def _parse_reason_for_closure(data: object) -> Union["RefData", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _reason_for_closure_type_1 = data
                reason_for_closure_type_1: Union[Unset, RefData]
                if isinstance(_reason_for_closure_type_1, Unset):
                    reason_for_closure_type_1 = UNSET
                else:
                    reason_for_closure_type_1 = RefData.from_dict(_reason_for_closure_type_1)

                return reason_for_closure_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RefData", Unset, str], data)

        reason_for_closure = _parse_reason_for_closure(d.pop("reasonForClosure", UNSET))

        def _parse_renewal_priority(data: object) -> Union["RefData", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _renewal_priority_type_1 = data
                renewal_priority_type_1: Union[Unset, RefData]
                if isinstance(_renewal_priority_type_1, Unset):
                    renewal_priority_type_1 = UNSET
                else:
                    renewal_priority_type_1 = RefData.from_dict(_renewal_priority_type_1)

                return renewal_priority_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RefData", Unset, str], data)

        renewal_priority = _parse_renewal_priority(d.pop("renewalPriority", UNSET))

        alternate_names = cast(List[str], d.pop("alternateNames", UNSET))

        periods = []
        _periods = d.pop("periods", UNSET)
        for periods_item_data in _periods or []:
            periods_item = AgreementPeriodsItem.from_dict(periods_item_data)

            periods.append(periods_item)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        _cancellation_deadline = d.pop("cancellationDeadline", UNSET)
        cancellation_deadline: Union[Unset, datetime.date]
        if isinstance(_cancellation_deadline, Unset):
            cancellation_deadline = UNSET
        else:
            cancellation_deadline = isoparse(_cancellation_deadline).date()

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = InternalContact.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        orgs = []
        _orgs = d.pop("orgs", UNSET)
        for orgs_item_data in _orgs or []:
            orgs_item = Organisation.from_dict(orgs_item_data)

            orgs.append(orgs_item)

        external_license_docs = []
        _external_license_docs = d.pop("externalLicenseDocs", UNSET)
        for external_license_docs_item_data in _external_license_docs or []:
            external_license_docs_item = Document.from_dict(external_license_docs_item_data)

            external_license_docs.append(external_license_docs_item)

        supplementary_docs = []
        _supplementary_docs = d.pop("supplementaryDocs", UNSET)
        for supplementary_docs_item_data in _supplementary_docs or []:
            supplementary_docs_item = Document.from_dict(supplementary_docs_item_data)

            supplementary_docs.append(supplementary_docs_item)

        linked_licenses = []
        _linked_licenses = d.pop("linkedLicenses", UNSET)
        for linked_licenses_item_data in _linked_licenses or []:
            linked_licenses_item = LinkedLicense.from_dict(linked_licenses_item_data)

            linked_licenses.append(linked_licenses_item)

        usage_data_providers = []
        _usage_data_providers = d.pop("usageDataProviders", UNSET)
        for usage_data_providers_item_data in _usage_data_providers or []:
            usage_data_providers_item = UsageDataProvider.from_dict(usage_data_providers_item_data)

            usage_data_providers.append(usage_data_providers_item)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = Tag.from_dict(tags_item_data)

            tags.append(tags_item)

        agreement = cls(
            id=id,
            name=name,
            status=status,
            description=description,
            is_perpetual=is_perpetual,
            reason_for_closure=reason_for_closure,
            renewal_priority=renewal_priority,
            alternate_names=alternate_names,
            periods=periods,
            start_date=start_date,
            end_date=end_date,
            cancellation_deadline=cancellation_deadline,
            contacts=contacts,
            orgs=orgs,
            external_license_docs=external_license_docs,
            supplementary_docs=supplementary_docs,
            linked_licenses=linked_licenses,
            usage_data_providers=usage_data_providers,
            tags=tags,
        )

        agreement.additional_properties = d
        return agreement

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
