from datetime import datetime, timedelta

# 1
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 2
future_date = datetime.now() + timedelta(days=10)

# 3
date_obj = datetime.strptime("2026-12-25", "%Y-%m-%d")

# 4
days_left = (date_obj - datetime.now()).days

# 5
timestamp = datetime.now().timestamp()