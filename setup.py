from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='quantile_normalize',
    version='0.1',
    description="""scikit-learn extension that adds quantile normalization""",
    url='https://github.com/r-a-qureshi/quantile_normalize/',
    author='Rehman Qureshi',
    python_requires=">=3.6",
    packages=find_packages(),
    install_requires=requirements,
    keywords=["quantile normalization", "scikit-learn", "sklearn"],
    test_suite="test",
    zip_safe=False,
)