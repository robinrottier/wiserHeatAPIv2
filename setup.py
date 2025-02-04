import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rrwiserHeatAPIv2", # Replace with your own username
    #version="0.0.28",
    author="Robin Rottier",
    author_email="robin@rottier.co.uk",
    description="An API for controlling the Drayton Wiser Heating system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robinrottier/wiserheatapiv2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["ruamel.yaml>=0.16.12", "zeroconf>=0.37.0", "requests>=2.26.0"],
    python_requires='>=3.9',
    entry_points = {
        'console_scripts': ['wiser = wiserHeatAPIv2.cli:main'],
    },
    setuptools_git_versioning={
        "enabled": True,
    },
    setup_requires=["setuptools-git-versioning"],
)
