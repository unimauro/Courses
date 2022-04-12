#pip install tzdata

from datetime import datetime, timezone
import tzdata

from zoneinfo import ZoneInfo

z = ZoneInfo("Asia/Kolkata")
print(z)
post_date = datetime.datetime.now(z)
