#!/usr/bin/env python
"""Simple example of runner usage.

This example demonstrates how to implement custom Feature extractor classes
and how they can be executed using the fex runner.

The runner has sensible defaults for arguments which can be modified via
commandline arguments. For details call this file with `-h` or `--help`.

    examples/simple_example.py --help
"""

import logging

import pandas as pd

import fex
from fex import runner

logging.basicConfig(format='%(levelname)s:%(name)s:%(asctime)s=> %(message)s',
                    datefmt='%m/%d %H:%M:%S',
                    level=logging.INFO)


class ExampleFeature1(fex.FeatureExtractor):
    """First example feature extractor, super cool."""

    def extract(self):
        """Overriden method with custom logic.

        This is the place where one would do the data extraction and
        transformation.
        """
        data_frame = pd.DataFrame({'col1': [666]}, index=[1])
        self.emit(data_frame)


class ExampleFeature2(fex.FeatureExtractor):
    """Another example feature extractor."""

    def extract(self):
        """Overriden method with custom logic."""
        data_frame = pd.DataFrame({'col1': [42], 'col2': [314]}, index=[2])
        self.emit(data_frame)

runner.run(ExampleFeature1(), ExampleFeature2())
