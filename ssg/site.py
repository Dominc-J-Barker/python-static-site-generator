#!/usr/bin/env python
"""Site class to configure the site and setup the root file structure."""

from pathlib import Path

class Site:
    """Site class to configure the site and setup the root file structure."""
    def __init__(self, source:str, dest:str):

        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        """Make the site build directory."""

        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        """Make the output build directory."""

        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob('*'):
            if path.is_dir():
                self.create_dir(path)
