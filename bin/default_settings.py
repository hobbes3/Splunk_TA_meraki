# Meraki REST API info
API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
ORG_ID = 999999

INDEX = "main"

# Size of each log file.
# 1 MB = 1 * 1024 * 1024
LOG_ROTATION_BYTES = 25 * 1024 * 1024
# Maximum number of log files.
LOG_ROTATION_LIMIT = 100

# For some calls, the required time range in seconds for the metric.
# This number should be the same as how often get_data.py runs, ie every hour = 3600 seconds.
REPEAT = 3600

# set_syslog_servers.py
SET_SYSLOG_SERVERS_LOG_PATH = "/home/splunk/splunk_apps_log/meraki_set_syslog_servers.log"
SYSLOG_HOST = "1.2.3.4"
SYSLOG_PORT = 514
# Removes syslog host if it exists.
REMOVE_SYSLOG_HOST = "5.6.7.8"

# get_data.py
GET_DATA_LOG_PATH = "/home/splunk/splunk_apps_log/meraki_get_data.log"
THREADS = 4
SLEEP = 1
# Splunk or Cribl HEC info
HTTP_URL = "https://1.2.3.4:8088/services/collector/event"
HTTP_HEADERS = {
    "Authorization": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
