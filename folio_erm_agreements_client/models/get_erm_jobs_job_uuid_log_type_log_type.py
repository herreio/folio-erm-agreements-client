from enum import Enum


class GetErmJobsJobUUIDLogTypeLogType(str, Enum):
    INFOLOG = "infoLog"
    ERRORLOG = "errorLog"
    FULLLOG = "fullLog"

    def __str__(self) -> str:
        return str(self.value)
