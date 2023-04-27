from klym_telemetry.instrumenters.celery import _CeleryInstrumentor
from klym_telemetry.instrumenters.django import _DjangoInstrumentor
from klym_telemetry.instrumenters.fastapi import _FastAPIInstrumentor

FACTORIES = {
    "fastapi": _FastAPIInstrumentor,
    "django": _DjangoInstrumentor,
    "celery": _CeleryInstrumentor,
}


def instrument_app(app_type: str, **kwargs):
    if app_type in FACTORIES:
        return FACTORIES[app_type](**kwargs).instrument()
    raise ValueError(f"Invalid app type: {app_type}")
