#   A multi-purpose Discord Bot written with Python and pycord.
#   Copyright (C) 2022 czlucius (lcz5#3392)
#
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import contextlib
import json


@contextlib.contextmanager
def json_open(filepath: str, mode: str):
    """
    Reads a JSON file from file path, with supplied mode, and returns JSON accessor object.
    Usage:

    .. code-block:: python

    with json_read("file.json", "r") as json_data:
        print(json_data)

        # Other operations here...

    
    :param filepath: File path
    :param mode: Mode to open file ("r", "rw", etc.)
    :return: 
    """
    file = open(filepath, mode)
    try:
        yield json.load(file)
    finally:
        file.close()
