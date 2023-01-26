import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CoverageStatement")


@attr.s(auto_attribs=True)
class CoverageStatement:
    """
    Attributes:
        id (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        summary (Union[Unset, str]):
        start_volume (Union[Unset, str]):
        start_issue (Union[Unset, str]):
        end_volume (Union[Unset, str]):
        end_issue (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    summary: Union[Unset, str] = UNSET
    start_volume: Union[Unset, str] = UNSET
    start_issue: Union[Unset, str] = UNSET
    end_volume: Union[Unset, str] = UNSET
    end_issue: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        summary = self.summary
        start_volume = self.start_volume
        start_issue = self.start_issue
        end_volume = self.end_volume
        end_issue = self.end_issue

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if summary is not UNSET:
            field_dict["summary"] = summary
        if start_volume is not UNSET:
            field_dict["startVolume"] = start_volume
        if start_issue is not UNSET:
            field_dict["startIssue"] = start_issue
        if end_volume is not UNSET:
            field_dict["endVolume"] = end_volume
        if end_issue is not UNSET:
            field_dict["endIssue"] = end_issue

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

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

        summary = d.pop("summary", UNSET)

        start_volume = d.pop("startVolume", UNSET)

        start_issue = d.pop("startIssue", UNSET)

        end_volume = d.pop("endVolume", UNSET)

        end_issue = d.pop("endIssue", UNSET)

        coverage_statement = cls(
            id=id,
            start_date=start_date,
            end_date=end_date,
            summary=summary,
            start_volume=start_volume,
            start_issue=start_issue,
            end_volume=end_volume,
            end_issue=end_issue,
        )

        coverage_statement.additional_properties = d
        return coverage_statement

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
