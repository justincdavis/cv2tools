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
import os

from cv2ext import IterableVideo, Display

try:
    from ._utils import VID_LINK, download_youtube_video
except ImportError:
    from _utils import VID_LINK, download_youtube_video


def test_stress():
    if not os.path.exists("video.mp4"):
        download_youtube_video(VID_LINK, "video.mp4")

    for _ in range(3):
        display = Display("test", show=False)

        video = IterableVideo("video.mp4")

        for fid, frame in video:
            display(frame)


if __name__ == "__main__":
    test_stress()