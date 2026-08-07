@dataclass(slots=True, frozen=True)
class WatchfacePackageInfo:
    path: Path
    name: str
    version: str | None
    package_type: str