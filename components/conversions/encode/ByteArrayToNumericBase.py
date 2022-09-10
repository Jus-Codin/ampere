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

from components.conversions import XToY
from functions.base import bytes_to_base_arb


class ByteArrayToNumericBase(XToY):

    def __init__(self, val, base: int, *args, **kwargs):
        super().__init__(val)
        self.base = base

    def transform(self):
        # val is given as bytes, so we just have to convert it to an arbitrary base.
        val_conv = bytes_to_base_arb(self.val, self.base)
        return str(val_conv)

    def get_type(self) -> int:
        return self.TO_UNICODE
