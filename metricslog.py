import os
import logging
from datetime import datetime

from structlog import PrintLogger
from structlog import wrap_logger
from structlog.processors import JSONRenderer



def add_metadata(_, __, event_dict):
    event_dict['timestamp'] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    return event_dict


class Logger(object):
    def __init__(self, output=None, service=None, hostname=None):
        output = output or open('/var/log/metrics.log', "a")
        self.service = service or os.environ.get('SERVICE_NAME')
        self.hostname = hostname or os.environ.get('HOSTNAME')
        self._log = wrap_logger(
                        PrintLogger(output),
                        processors=[add_metadata, JSONRenderer()])

    def emit(self, metric, value=1.0):
        return self._log.info(metric=metric, value=value,
                              service=self.service, hostname=self.hostname)
