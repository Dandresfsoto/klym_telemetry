from enum import Enum
import klym_telemetry.instrumenters.module_import as importer

class SupportedInstrumenters(Enum):

    INSTRUMENTERS = {
        "fastapi": ("klym_telemetry.instrumenters.fastapi", "_FastAPIInstrumentor"),
        "django": ("klym_telemetry.instrumenters.django", "_DjangoInstrumentor"),
        "celery": ("klym_telemetry.instrumenters.celery", "_CeleryInstrumentor"),
        "psycopg2": ("klym_telemetry.instrumenters.psycopg2", "_Psycopg2Instrumentor"),
        "requests": ("klym_telemetry.instrumenters.requests", "_RequestsInstrumentor"),
    }

def instrument_app(app_type: str, **kwargs):
    try:
        package = SupportedInstrumenters.INSTRUMENTERS.value.get(app_type)[0]
        classname = SupportedInstrumenters.INSTRUMENTERS.value.get(app_type)[1]
        return importer.import_module(package, classname)(**kwargs).instrument()
    except Exception as e:
        print(f"Dependency error. You need to import the instrumenter for {app_type} if you want to use it")
        raise
