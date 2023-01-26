from enum import Enum


class PostErmEntityTypeEntityType(str, Enum):
    CONTACTS = "contacts"
    CUSTPROPS = "custprops"
    ENTITLEMENTS = "entitlements"
    ENTITLEMENTLOGENTRY = "entitlementLogEntry"
    JOBS = "jobs"
    KBS = "kbs"
    ORG = "org"
    PACKAGES = "packages"
    PCI = "pci"
    PTI = "pti"
    PLATFORMS = "platforms"
    REFDATA = "refdata"
    RESOURCE = "resource"
    SAS = "sas"
    STS = "sts"
    TITLES = "titles"

    def __str__(self) -> str:
        return str(self.value)
