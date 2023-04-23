from codecs import open
from os import path

from setuptools import setup

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="klym_telemetry",
    version="0.1.0",
    description="Scaffold library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dummy.readthedocs.io/",
    author="Klym Telemetry",
    author_email="example@email.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "fastapi",
        "requests ==2.28.2",
        "opentelemetry-instrumentation-fastapi ==0.38b0",
        "opentelemetry-exporter-otlp-proto-grpc ==1.17.0",
        "opentelemetry-propagator-aws-xray ==1.0.1",
        "opentelemetry-sdk-extension-aws ==2.0.1",
        "opentelemetry-instrumentation-sqlalchemy ==0.38b0",
        "opentelemetry-instrumentation-requests ==0.38b0"
    ]
)
