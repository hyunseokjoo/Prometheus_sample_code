# Prometheus Custom Exporter
Promehteus Metric 수집기 샘플 코드 입니다.

### 관련 패키지 다운로드
```bash 
pip install -r requirements.txt
```
# Prometheus Service Discovery - file
Service Discovery를 File단위로 작성하여 관리하는 예시 입니다.
### Prometheus Basic Config파일 - prometheus.yml
기본으로 실행하기
```bash
./prometheus --config.file=prometheus.yml
```

### Prometheus SD Config파일 - prometheus_sd.yml
SD 파일로 설정된 config 실행하기
```bash
./prometheus --config.file=prometheus_sd.yml
```


