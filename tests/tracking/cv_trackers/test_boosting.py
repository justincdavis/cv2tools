# Copyright (c) 2024 Justin Davis (davisjustin302@gmail.com)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
from __future__ import annotations

from cv2ext.tracking import TrackerType

from .generic import check_basic_tracking, check_full_tracking


def test_boosting_basic():
    check_basic_tracking(TrackerType.BOOSTING)


def test_boosting_full():
    check_full_tracking(TrackerType.BOOSTING, use_gray=False)


def test_boosting_full_gray():
    # this should throw a ValueError, assert it does
    try:
        check_full_tracking(TrackerType.BOOSTING, use_gray=True)
        assert False
    except ValueError:
        assert True