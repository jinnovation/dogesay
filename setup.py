from setuptools import setup

setup(
    name = "dogesay",
    packages = ["dogesay"],
    version = "1.0.0b1",
    description = "Like cowsay but doge",
    url = "https://github.com/jinnovation/dogesay",
    download_url = "https://github.com/jinnovation/dogesay/tarball/1.0b",
    author = "Jonathan Jin",
    author_email = "jonathan@jjin.me",
    license  = "MIT",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment",

        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3', 
    ],
    keywords = "",

    entry_points={
        "console_scripts": [
            "dogesay=dogesay.dogesay:main",
        ],
    },

    package_data = {
        "dogesay": ["static/*.txt"],
    },
)

