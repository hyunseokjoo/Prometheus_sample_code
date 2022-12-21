import time
import random
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY
from prometheus_client import start_http_server

class myCustomCollector(object):
    def __init__(self):
        pass

    # Collect 함수를 꼭 만들어 주어야 Start_http_server에서 사용함
    def collect(self):
        # Gauge 만들기
        g = GaugeMetricFamily("random_number", "Gauge - Number Generator", labels=["randomNum1", "randomNum2"])
        # Gauge 값 넣기
        g.add_metric("",random.randint(1, 20))
        g.add_metric(["First"], random.randint(1, 20))
        g.add_metric(["","Second"], random.randint(1, 20))
        g.add_metric(["First", "Second"], random.randint(1, 20))
        yield g

        # Counter 만들기 
        c = CounterMetricFamily("random_number_2", "Counter - Number Generator", labels=["randomNum1", "randomNum2"])
        # Counter 값 넣기
        c.add_metric("", random.randint(1, 20))
        c.add_metric(["First"], random.randint(1, 20))
        c.add_metric(["First", "Second"], random.randint(1, 20))
        yield c

if __name__ == "__main__":
    port = 9000
    frequency = 1

    # Exporter 서버 시작하기
    start_http_server(port)    
    # CustomCollector 등록
    REGISTRY.register(myCustomCollector())
    
    while True: 
        # period between collection
        time.sleep(frequency)
        
        