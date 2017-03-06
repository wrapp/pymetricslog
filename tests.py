import json
from mock import ANY
from cStringIO import StringIO
from metricslog import Logger


class TestMetricLogObserver(object):
    def setup(self):
        self.out = StringIO()
        self.service = 'myservice'
        self.hostname = 'host-01'
        self.log = Logger(self.out, service=self.service, hostname=self.hostname)

    def test_emit(self):
        metric = 'user_created'
        value = 10.0
        self.log.emit(metric, value)
        self.assert_output({
            "timestamp": ANY,
            "service": self.service,
            "hostname": self.hostname,
            "metric": metric,
            "value": value
        })

    def test_emit_with_default_value(self):
        metric = 'user_created'
        self.log.emit(metric)
        self.assert_output({
            "timestamp": ANY,
            "service": self.service,
            "hostname": self.hostname,
            "metric": metric,
            "value": 1.0
        })

    def get_output(self):
        self.out.reset()
        return json.loads(self.out.read())

    def assert_output(self, expected):
        actual = self.get_output()
        assert actual == expected, repr(actual)
