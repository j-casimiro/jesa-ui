from setuptools import setup, find_packages

setup(
    name='jesa_ui',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'jesa-ui = jesa_ui.cli:main',
        ],
    },
    package_data={
        'jesa_ui': ['components/*.j2'],
    },
    description='installable jinja-based tailwind ui components for any python web framework.',
)