import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stockdata-pass100days",
    version="0.0.1",
    author="BHushan Rathod",
    author_email="abhushanprathod@example.com",
    description="Sample flask app to show stock data over pass 100 days",
    long_description=long_description,
    url="https://github.com/BHushanRathod/stock-data",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)