from typing import TypedDict, Union, Optional, Literal
from pyntone.types import RecordID, Revision

class RecordItem(TypedDict):
    value: Union[int, str]

RecordForParameter = dict[str, RecordItem]

class UpdateKey(TypedDict):
    field: str
    value: str

class UpdateRecordForParameter(TypedDict, total=False):
    id: RecordID
    record: RecordForParameter
    revision: Revision

class UpdateKeyRecordForParameter(TypedDict, total=False):
    updateKey: UpdateKey
    record: RecordForParameter
    revision: Revision

class DeleteRecordParameter(TypedDict, total=False):
    id: RecordID
    revision: Revision

class Mention(TypedDict):
    code: str
    type: Literal['USER', 'GROUP', 'ORGANIZATION']

class Comment(TypedDict, total=False):
    text: str
    mentions: list[Mention]

class UpdateRecordStatusParameter(TypedDict, total=False):
    action: str
    assignee: str
    id: RecordID
    revision: Revision