import logging

from fastapi import FastAPI
from opentelemetry import propagate, trace, metrics
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.propagators.aws import AwsXRayPropagator
from opentelemetry.sdk.extension.aws.trace import AwsXRayIdGenerator
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

logger = logging.getLogger(__name__)


def instrument_app(app: FastAPI, service_name: str, otel_collector_endpoint: str):
    try:
        propagate.set_global_textmap(AwsXRayPropagator())

        resource = Resource.create(attributes={"service.name": service_name})

        tracer_provider = TracerProvider(resource=resource, id_generator=AwsXRayIdGenerator())

        span_exporter = OTLPSpanExporter(endpoint=otel_collector_endpoint)

        processor = BatchSpanProcessor(span_exporter)
        tracer_provider.add_span_processor(processor)

        trace.set_tracer_provider(tracer_provider)

        metrics_exporter = OTLPMetricExporter(endpoint=otel_collector_endpoint,)

        reader = PeriodicExportingMetricReader(metrics_exporter)
        meter_provider = MeterProvider(resource=resource, metric_readers=[reader])

        metrics.set_meter_provider(meter_provider)

        FastAPIInstrumentor.instrument_app(app, tracer_provider=tracer_provider, meter_provider=meter_provider,)

        RequestsInstrumentor().instrument()

    except Exception:  # pylint: disable=broad-exception-caught
        logger.exception("No telemetry gateway configured")
