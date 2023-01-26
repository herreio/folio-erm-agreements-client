from enum import Enum


class GetErmSasAgreementUUIDResourcesExportCurrentDownloadFormatDownloadFormat(str, Enum):
    KBART = "kbart"

    def __str__(self) -> str:
        return str(self.value)
