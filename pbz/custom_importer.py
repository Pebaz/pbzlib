"""
This module works.

Place any PNG image file in the current working directory and import it by name.

Only images with variable-like names can be imported.

https://stackoverflow.com/questions/43571737/how-to-implement-an-import-hook-that-can-modify-the-source-code-on-the-fly-using
"""

import sys
from pathlib import Path
from importlib.util import spec_from_file_location
from importlib.abc import Loader, MetaPathFinder
from importlib.util import spec_from_file_location
from PIL import Image


class MyMetaFinder(MetaPathFinder):
    def find_spec(self, fullname, path, target=None): 
        files_in_cwd = {
            path.stem: path
            for path in Path().iterdir()
            if path.is_file()
        }

        if fullname in files_in_cwd:
            return spec_from_file_location(
                fullname,
                path,
                loader=MyLoader(files_in_cwd[fullname])
            )


class MyLoader(Loader):
    def __init__(self, filename):
        "Record the filename for later."
        self.filename = filename

    def create_module(self, *args):
        "Instead of returning a valid Python module, return an Image object!"
        return Image.open(self.filename)

    def exec_module(self, *args):
        "Override to make sure image is not loaded."


# Insert the finder into the import machinery
sys.meta_path.insert(0, MyMetaFinder())


if __name__ == '__main__':
    def generate_image(width, name):
        img = Image.new('RGBA', (width, width))
        for x in range(width):
            for y in range(width):
                img.putpixel((x, y), (255, 255 - x, 255 - y, 255))
        img.save(name + '.png')

    print('-' * 80)
    import foo
    foo.show()
