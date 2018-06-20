import sys
from datetime import datetime
import os

class logging:
    @staticmethod
    def log_info(msg, file, line):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = "\x1B[32mINFO\x1B[0m"
        service_name = os.getenv("SERVICE_NAME")
        sys.stderr.write('[{}] {} {} {}:{} "{}"\n'.format(now,level, service_name, file, line, msg))
        return None

    @staticmethod
    def log_warning(msg, file, line):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = "\x1B[33mWARNING\x1B[0m"
        service_name = os.getenv("SERVICE_NAME")
        sys.stderr.write('[{}] {} {} {}:{} "{}"\n'.format(now,level, service_name, file, line, msg))
        return None

    @staticmethod
    def log_error(msg, file, line):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = "\x1B[31mERROR\x1B[0m"
        service_name = os.getenv("SERVICE_NAME")
        sys.stderr.write('[{}] {} {} {}:{} "{}"\n'.format(now,level, service_name, file, line, msg))
        return None
