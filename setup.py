"""\
This application is a special request for the Dutch tax office
(Belastingdienst).
"""


from setuptools import setup, find_packages


setup(
    name = "cr2.zaakspecificatie",
    version = "0.1",
    packages = find_packages(),

    install_requires = ['gaphor>=0.14.0'],

    namespace_packages = ['cr2'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },

    # metadata for upload to PyPI
    author = "Arjan Molenaar",
    author_email = "gaphor@gmail.com",
    description = "CR2 Zaakbegeleider 3 zaak specificatie",
    long_description = __doc__,
    license = "GPL",
    keywords = "gaphor cr2 zaakspecificatie",

    entry_points = {
        'gaphor.services': [
            'crea-zaakspecificatie-export = cr2.zaakspecificatie:ZaakspecificatieExportPlugin',
        ]
    }
)

# vim:sw=4:et:ai
