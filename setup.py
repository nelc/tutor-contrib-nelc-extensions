import io
import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tutornelc_extensions", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-contrib-nelc-extensions",
    version=ABOUT["__version__"],
    url="https://github.com/nelc/tutor-contrib-nelc-extensions",
    project_urls={
        "Code": "https://github.com/nelc/tutor-contrib-nelc-extensions",
        "Issue tracker": "https://github.com/nelc/tutor-contrib-nelc-extensions/issues",
    },
    license="MIT",
    author="Johanseto",
    author_email="johan.castiblanco@edunext.co",
    description="Tutor Plugin to add features, tools, extension to nelc docker images.",
    long_description=load_readme(),
    long_description_content_type="text/x-rst",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["tutor>=16.0.0,<17.0.0"],
    extras_require={
        "dev": [
            "tutor[dev]>=16.0.0,<17.0.0",
        ]
    },
    entry_points={
        "tutor.plugin.v1": [
            "nelc-extensions = tutornelc_extensions.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
