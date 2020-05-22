from setuptools import setup, find_packages

setup(
    name="ibm_service_validator",
    version="0.0.3",
    description="Python package, Schemathesis, extended to include IBM API Handbook validation.",
    url="https://github.ibm.com/CloudEngineering/ibm-service-validator",
    author="Barrett Schonefeld, IBM",
    author_email="barrett.schonefeld@ibm.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["click", "ibm-cloud-sdk-core", "pyyaml", "schemathesis"],
    entry_points="""
        [console_scripts]
        ibm-service-validator=ibm_service_validator.cli.commands:ibm_service_validator
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
