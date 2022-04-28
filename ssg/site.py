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

        directory = self.dest / Path.relative_to(path, self.source)
        Path.mkdir(directory, parents=True, exist_ok=True)

    def build(self):
        """Make the output build directory."""

        Path.mkdir(self.dest, parents=True, exist_ok=True)
        for path in self.source.rglob('*'):
            if Path.is_dir(path):
                self.create_dir(path)
