import setuptools

with open("README.md", encoding="utf8") as readme:
    long_description = readme.read()


setuptools.setup(
    name="async_mongo",
    packages=setuptools.find_packages(),
    version="0.0.1",
    description="Asynchronous wrapper for pymongo.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Abishnoi69/async_mongo",
    download_url="https://github.com/Abishnoi69/async_mongo/releases/latest",
    author="Abishnoi",
    author_email="Abishnoi69@Abg.org",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    keywords="mongo-db mongo pymongo pymongo-db Python",
    project_urls={
        "Tracker": "https://github.com/Abishnoi69/async_mongo/issues",
        "Community": "https://t.me/Abgpy",
        "Source": "https://github.com/Abishnoi69/async_mongo",
        "Documentation": "https://github.com/Abishnoi69/async_mongo/tree/master/doce",
    },
    python_requires="~=3.7",
    zip_safe=False,
)
