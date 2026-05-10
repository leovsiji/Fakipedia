from setuptools import setup,find_packages

setup(
    name = "Fakipedia",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],

    entry_points={
        "console_scripts":[
                "beyond=faki.fakipedia:beyond",
            ],
    },

)