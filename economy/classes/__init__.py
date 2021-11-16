import re

from setuptools import setup

with open("readme.md", "r") as fh:
    long_description = fh.read()

_version_regex = (
    r"^__version__ = ('|\")((?:[0-9]+\.)*[0-9]+(?:\.?([a-z]+)(?:\.?[0-9])?)?)\1$"
)

try:
    with open("economy/__init__.py") as stream:
        match = re.search(_version_regex, stream.read(), re.MULTILINE)
        version = match.group(2)
except FileNotFoundError:
    version = "0.0.0"


def parse_requirements_file(path):
    with open(path) as fp:
        dependencies = (d.strip() for d in fp.read().split("\n") if d.strip())
        return [d for d in dependencies if not d.startswith("#")]


setup(
    name="economy",
    version=version,
    author="Skelmis",
    author_email="ethan@koldfusion.xyz",
    description=".",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Skelmis/Discord-Economy",
    packages=[
        "antispam",
        "antispam.caches",
        "antispam.caches.memory",
        "antispam.caches.redis",
        "antispam.dataclasses",
        "antispam.enums",
        "antispam.plugins",
        "antispam.libs",
    ],
    install_requires=parse_requirements_file("requirements.txt"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
    ],
    python_requires=">=3.8",
)
