from klym_telemetry.instrumenters.celery import _CeleryInstrumentor
from klym_telemetry.instrumenters.django import _DjangoInstrumentor
from klym_telemetry.instrumenters.fastapi import _FastAPIInstrumentor
from klym_telemetry.instrumenters.postgres import _Psycopg2Instrumentor
from klym_telemetry.instrumenters.requests import _RequestsInstrumentor

FACTORIES = {
    "fastapi": _FastAPIInstrumentor,
    "django": _DjangoInstrumentor,
    "celery": _CeleryInstrumentor,
    "psycopg2": _Psycopg2Instrumentor,
    "requests": _RequestsInstrumentor,
}


def instrument_app(app_type: str, **kwargs):
    if app_type in FACTORIES:
        return FACTORIES[app_type](**kwargs).instrument()
    raise ValueError(f"Invalid app type: {app_type}")
