import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgreementPeriodsItem")


@attr.s(auto_attribs=True)
class AgreementPeriodsItem:
    """
    Attributes:
        start_date (datetime.date):
        end_date (Union[Unset, datetime.date]):
        cancellation_deadline (Union[Unset, datetime.date]):
        period_status (Union[Unset, str]):
        note (Union[Unset, str]):
        id (Union[Unset, str]):
    """

    start_date: datetime.date
    end_date: Union[Unset, datetime.date] = UNSET
    cancellation_deadline: Union[Unset, datetime.date] = UNSET
    period_status: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date = self.start_date.isoformat()
        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        cancellation_deadline: Union[Unset, str] = UNSET
        if not isinstance(self.cancellation_deadline, Unset):
            cancellation_deadline = self.cancellation_deadline.isoformat()

        period_status = self.period_status
        note = self.note
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startDate": start_date,
            }
        )
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if cancellation_deadline is not UNSET:
            field_dict["cancellationDeadline"] = cancellation_deadline
        if period_status is not UNSET:
            field_dict["periodStatus"] = period_status
        if note is not UNSET:
            field_dict["note"] = note
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_date = isoparse(d.pop("startDate")).date()

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

        period_status = d.pop("periodStatus", UNSET)

        note = d.pop("note", UNSET)

        id = d.pop("id", UNSET)

        agreement_periods_item = cls(
            start_date=start_date,
            end_date=end_date,
            cancellation_deadline=cancellation_deadline,
            period_status=period_status,
            note=note,
            id=id,
        )

        agreement_periods_item.additional_properties = d
        return agreement_periods_item

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
