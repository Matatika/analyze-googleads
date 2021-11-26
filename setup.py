from setuptools import setup, find_packages

setup(
    name="analyze-google-ads",
    version="0.1.0",
    description="Meltano project file bundle of Matatika datasets for Google Ads",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/tap-google-ads/*.yaml"
        ]
    },
)
