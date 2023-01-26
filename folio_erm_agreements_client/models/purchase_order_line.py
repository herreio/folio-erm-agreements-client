from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.purchase_order_line_owner import PurchaseOrderLineOwner


T = TypeVar("T", bound="PurchaseOrderLine")


@attr.s(auto_attribs=True)
class PurchaseOrderLine:
    """
    Attributes:
        id (Union[Unset, str]):
        owner (Union[Unset, PurchaseOrderLineOwner]):
        po_line_id (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    owner: Union[Unset, "PurchaseOrderLineOwner"] = UNSET
    po_line_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        po_line_id = self.po_line_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if po_line_id is not UNSET:
            field_dict["poLineId"] = po_line_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.purchase_order_line_owner import PurchaseOrderLineOwner

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, PurchaseOrderLineOwner]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = PurchaseOrderLineOwner.from_dict(_owner)

        po_line_id = d.pop("poLineId", UNSET)

        purchase_order_line = cls(
            id=id,
            owner=owner,
            po_line_id=po_line_id,
        )

        purchase_order_line.additional_properties = d
        return purchase_order_line

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
