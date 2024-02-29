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

import argparse
import os
import time

import cv2
from cv2ext import Display, IterableVideo


def naive(video: str, show: bool) -> float:
    cap = cv2.VideoCapture(video)

    t0 = time.perf_counter()
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if show:
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    t1 = time.perf_counter()

    cap.release()
    cv2.destroyAllWindows()

    return t1 - t0


def threaded(video: str, show: bool) -> float:
    video = IterableVideo(video, use_thread=True)
    if show:
        display = Display("example", show=show)

    t0 = time.perf_counter()
    for _, frame in video:
        if show:
            display(frame)
    t1 = time.perf_counter()

    return t1 - t0


def main():
    parser = argparse.ArgumentParser(description="Display a video.")
    parser.add_argument("--video", help="The video to process.")
    parser.add_argument("--show", action="store_true", help="Show the video.")
    args = parser.parse_args()

    if not os.path.exists(args.video):
        raise FileNotFoundError(f"Video {args.video} does not exist.")

    naivetime = naive(args.video, args.show)
    threadedtime = threaded(args.video, args.show)

    print(f"Naive time: {naivetime:.2f}s")
    print(f"Threaded time: {threadedtime:.2f}s")

if __name__ == "__main__":
    main()
