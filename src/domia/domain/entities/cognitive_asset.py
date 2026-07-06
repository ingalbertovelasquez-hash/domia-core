from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class CognitiveAsset:
    name: str
    asset_type: str
    id: str = field(default_factory=lambda: str(uuid4()))
    status: str = "active"