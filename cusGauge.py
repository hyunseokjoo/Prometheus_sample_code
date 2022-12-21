import time
from prometheus_client import start_http_server, Gauge

g = Gauge(
    name="gauge_test",
    documentation="This is Custom Gauge",
    labelnames=["first", "second"])


if __name__ == "__main__":
    port = 9000
    frequency = 1

    g.labels(first='1', second='2').inc(2)
    g.labels(first='1', second='2').dec(2)

    start_http_server(port)
    
    while True: 
        # period between collection
        time.sleep(frequency)
        
        