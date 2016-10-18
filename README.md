# Celery Example

```bash
# Start the Broker(Redis)
>> brew services redis start
>> celery worker -A tasks -l DEBUG
```

```python
python3 example.py
```