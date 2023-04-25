# KLYM Telemetry
A small library to add instrumentation in KLYM apps.

### Installation
```
pip install git+https://github.com/Dandresfsoto/klym_telemetry.git#egg=klym_telemetry
```

### Get started
#### Instrumenting a fastapi app
1. Import klym instrumenter

```python
from klym_telemetry.instrumenters import instrument_app
```
2. Import instrument decorator

```python
from klym_telemetry.utils import instrument
```
3. Initialize automatic instrumentation

```python
instrument_app(app_type='fastapi', app=app, service_name="test-klym-microservice", endpoint="http://localhost:4317")
```
Full example:

```python
import time

from fastapi import FastAPI
from klym_telemetry.instrumenters import instrument_app
from klym_telemetry.utils import instrument, klym_telemetry

app = FastAPI()
instrument_app(app_type='fastapi', app=app, service_name="test-klym-microservice", endpoint="http://localhost:4317")


@instrument(private_methods=True, attributes={"description": "Class to say hello"})
class Hello:

    @instrument(span_name="Get start message (private method)")
    def _get_start_message(self):
        return "Hello"

    def say_hello(self):
        return {"message": self._get_start_message() + " World"}

    def say_hello_with_name(self, name: str):
        return {"message": f"{self._get_start_message()} {name}"}


@app.get("/")
def root():
    klym_telemetry.add_event_curr_span("Start sleeping")  # Custom event example
    for _ in range(10):
        time.sleep(0.2)
    klym_telemetry.add_event_curr_span("Finished sleeping")
    return Hello().say_hello()


@app.get("/hello/{name}")
@instrument(span_name="Say hello with name", attributes={"description": "Class to say hello asynchrounously"})
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
```
