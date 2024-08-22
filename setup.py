from setuptools import setup, find_packages

setup(
    name="codebase-analyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "anthropic",
        "pydantic",
        "httpx",
        "tqdm",
    ],
    entry_points={
        "console_scripts": [
            "codebase-analyzer=src.main:main",
        ],
    },
)