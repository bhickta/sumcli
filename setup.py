from setuptools import setup, find_packages

setup(
    name='sumcli',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click==8.1.7',
        'joblib==1.4.2',
        'nltk==3.8.1',
        'pyperclip==1.8.2',
        'regex==2024.5.15',
        'tqdm==4.66.4',
    ],
    entry_points={
        'console_scripts': [
            'sumcli = core.cli:main'
        ]
    },
)