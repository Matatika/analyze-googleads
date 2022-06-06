from setuptools import setup, find_packages

setup(
    name="analyze-googleads",
    version="0.4.2",
    description="Meltano project file bundle of Matatika datasets for Google Ads",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/tap-googleads/*.yml",
            "orchestrate/tap-googleads/elt.sh",
        ]
    },
)
