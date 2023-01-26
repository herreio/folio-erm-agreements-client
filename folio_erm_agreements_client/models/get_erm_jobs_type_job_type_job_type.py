from enum import Enum


class GetErmJobsTypeJobTypeJobType(str, Enum):
    COMPARISON = "comparison"
    COVERAGEREGENERATION = "coverageRegeneration"
    PACKAGEIMPORT = "packageImport"
    KBARTIMPORT = "kbartImport"
    PACKAGEINGEST = "packageIngest"
    SUPPLEMENTARYDOCUMENTSCLEANING = "supplementaryDocumentsCleaning"

    def __str__(self) -> str:
        return str(self.value)
