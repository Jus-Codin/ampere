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

import re

from components.conversions import XToY
from exceptions import InvalidExpressionException
from functions.base import base_arb_to_bytes


class NumericBaseToByteArray(XToY):

    def __init__(self, val, group_len: int, valid_chars_regex: str, base: int, *args, **kwargs):
        super().__init__(val)
        self.group_len = group_len
        self.valid_chars_regex = valid_chars_regex
        self.base = base

    def transform(self):
        val = str(self.val).replace(" ", "").lower()

        invalid_reason = None
        if len(val) % self.group_len != 0:
            # Not in groups of 8
            invalid_reason = f"Pattern is not in groups of {self.group_len}."
        elif re.match(rf"^{self.valid_chars_regex}+$", val) is None:
            invalid_reason = "Pattern contains invalid characters."

        if not invalid_reason:
            # Binary pattern is valid. Perform conversion.
            return base_arb_to_bytes(val, self.base)
        else:
            raise InvalidExpressionException(invalid_reason)

    def get_type(self) -> int:
        return self.FROM_UNICODE
