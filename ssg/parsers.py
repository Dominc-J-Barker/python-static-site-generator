from typing import List
from pathlib import Path
import shutil

class Parser:

    EXTENSIONS:List[str] = []

    def valid_extensions(self, extension):
        return extension in self.EXTENSIONS

    def parse(self, path:Path, source:Path, dest:Path):
        raise NotImplementedError

    def read(self, path:Path):
        with open(path, 'rt', encoding='utf-8') as filehandle:
            return filehandle.read()

    def write(self, path, dest, content, ext='.html'):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, 'wt') as filehandle:
            filehandle.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest/ path.relative_to(source) )

class ResourceParser(Parser):

    extensions = ['.jpg', '.png', '.gif','.css','.hmtl']

    def parser(self, path, source, dest):
        self.copy(path, source, dest)

