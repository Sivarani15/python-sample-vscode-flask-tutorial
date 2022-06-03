import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-sample-vscode-flask-tutorial",
    version="0.0.1",
    author="Sivarani",
    author_email="sivarani42@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sivarani15/python-sample-vscode-flask-tutorial.git",
    
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "hello_app"},
    packages=setuptools.find_packages(where="hello_app"),
    python_requires=">=3.8.2",
)