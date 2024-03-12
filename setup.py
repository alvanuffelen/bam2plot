import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setuptools.setup(
    name="bam2plot",
    version="0.2.3",
    description="Plot of coverage from bam file",
    url="https://github.com/willros/bam2plot",
    author="William Rosenbaum",
    author_email="william.rosenbaum@gmail.com",
    license="MIT",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    install_requires=[
        "fire==0.6.0",
        "pandas==2.2.1",
        "pysam==0.22.0",
        "seaborn==0.13.2",
    ],
    entry_points={"console_scripts": ["bam2plot=bam2plot.main:run"]},
)
