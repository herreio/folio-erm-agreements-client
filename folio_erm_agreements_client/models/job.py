from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comparison_point import ComparisonPoint
    from ..models.file import File
    from ..models.ref_data import RefData


T = TypeVar("T", bound="Job")


@attr.s(auto_attribs=True)
class Job:
    """
    Attributes:
        class_ (Union[Unset, str]):
        comparison_points (Union[Unset, List['ComparisonPoint']]):
        date_created (Union[Unset, int]):
        error_log_count (Union[Unset, int]):
        file_upload (Union[Unset, File]):
        full_log_count (Union[Unset, int]):
        id (Union[Unset, str]):
        info_log_count (Union[Unset, int]):
        name (Union[Unset, str]):
        started (Union[Unset, int]):
        status (Union['RefData', Unset, str]):
    """

    class_: Union[Unset, str] = UNSET
    comparison_points: Union[Unset, List["ComparisonPoint"]] = UNSET
    date_created: Union[Unset, int] = UNSET
    error_log_count: Union[Unset, int] = UNSET
    file_upload: Union[Unset, "File"] = UNSET
    full_log_count: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    info_log_count: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    started: Union[Unset, int] = UNSET
    status: Union["RefData", Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.ref_data import RefData

        class_ = self.class_
        comparison_points: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.comparison_points, Unset):
            comparison_points = []
            for comparison_points_item_data in self.comparison_points:
                comparison_points_item = comparison_points_item_data.to_dict()

                comparison_points.append(comparison_points_item)

        date_created = self.date_created
        error_log_count = self.error_log_count
        file_upload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file_upload, Unset):
            file_upload = self.file_upload.to_dict()

        full_log_count = self.full_log_count
        id = self.id
        info_log_count = self.info_log_count
        name = self.name
        started = self.started
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
        if class_ is not UNSET:
            field_dict["class"] = class_
        if comparison_points is not UNSET:
            field_dict["comparisonPoints"] = comparison_points
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if error_log_count is not UNSET:
            field_dict["errorLogCount"] = error_log_count
        if file_upload is not UNSET:
            field_dict["fileUpload"] = file_upload
        if full_log_count is not UNSET:
            field_dict["fullLogCount"] = full_log_count
        if id is not UNSET:
            field_dict["id"] = id
        if info_log_count is not UNSET:
            field_dict["infoLogCount"] = info_log_count
        if name is not UNSET:
            field_dict["name"] = name
        if started is not UNSET:
            field_dict["started"] = started
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comparison_point import ComparisonPoint
        from ..models.file import File
        from ..models.ref_data import RefData

        d = src_dict.copy()
        class_ = d.pop("class", UNSET)

        comparison_points = []
        _comparison_points = d.pop("comparisonPoints", UNSET)
        for comparison_points_item_data in _comparison_points or []:
            comparison_points_item = ComparisonPoint.from_dict(comparison_points_item_data)

            comparison_points.append(comparison_points_item)

        date_created = d.pop("dateCreated", UNSET)

        error_log_count = d.pop("errorLogCount", UNSET)

        _file_upload = d.pop("fileUpload", UNSET)
        file_upload: Union[Unset, File]
        if isinstance(_file_upload, Unset):
            file_upload = UNSET
        else:
            file_upload = File.from_dict(_file_upload)

        full_log_count = d.pop("fullLogCount", UNSET)

        id = d.pop("id", UNSET)

        info_log_count = d.pop("infoLogCount", UNSET)

        name = d.pop("name", UNSET)

        started = d.pop("started", UNSET)

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

        job = cls(
            class_=class_,
            comparison_points=comparison_points,
            date_created=date_created,
            error_log_count=error_log_count,
            file_upload=file_upload,
            full_log_count=full_log_count,
            id=id,
            info_log_count=info_log_count,
            name=name,
            started=started,
            status=status,
        )

        job.additional_properties = d
        return job

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
