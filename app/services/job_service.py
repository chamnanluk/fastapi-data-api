from datetime import datetime
from pathlib import Path


AUDIT_LOG_PATH = Path("job_audit.log")


def write_job_log(report_name: str) -> None:
    timestamp = datetime.utcnow().isoformat()
    with AUDIT_LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(f"[{timestamp} UTC] Triggered refresh for: {report_name}\n")
