metricslog
===========

Logs metrics to /var/log/metrics.log. These metrics take the format:

```json
{"timestamp": "YYYY-mm-ddTHH:MM:SS", "host": "host01", "service": "users", "metric":"foo.bar", "value": 1.0}
```


If you have the SERVICE_NAME and HOSTNAME environment variables set, then these fields would also be logged with the metric.

If it is not set, you can also pass it when initializing the logger.

```python

In [1]: import metricslog

In [2]: log = metricslog.Logger()

In [3]: log.emit(metric="user_created")
{"timestamp": "2017-01-91T00:00:00Z", "hostname": "production-i-02332", "service": "users", "metric":"user_created", "value": 1.0}

In [4]: log = metricslog.Logger(service="offers", hostname="production-i-02332")

In [5]: log.emit(metric="user_created", value=1.0)
{"timestamp": "2017-01-91T00:00:00Z", "hostname": "production-i-02332", "service": "offers", "metric":"user_created", "value": 1.0}


```

License: MIT
