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

from pathlib import Path
from threading import Condition, Lock, Thread

import cv2  # type: ignore[import-untyped]
import numpy as np
from typing_extensions import Self


class IterableVideo:
    """
    Iterable version of cv2.VideoCapture with extras.

    Parameters
    ----------
    filename : Path
        Path to the video file.
    thread_loads : bool
        If True, the frames will be loaded in a separate thread.
        This can help speedup iteration times.

    Attributes
    ----------
    frame : numpy.ndarray
        The current frame.
    frame_num : int
        The current frame number.
    success : bool
        True if the frame was successfully loaded.
    length : int
        The number of frames in the video.
    fps : float
        The frames per second of the video.
    size : tuple
        The width and height of the video.

    Methods
    -------
    __len__
    __iter__
    __next__
    read
        Gets the next frame and status from the video.

    """

    def __init__(
        self: Self,
        filename: Path | str,
        channels: int = 3,
        *,
        use_thread: bool = False,
    ) -> None:
        """
        Create a new instance of the video.

        Parameters
        ----------
        filename : Path | str
            Path to the video file.
        channels : int
            The number of channels in the video.
            This defaults to 3, and is used to pre-allocate a frame,
            such that the first frame is not empty.
            Use 1 for grayscale videos.
        use_thread : bool
            If True, the frames will be loaded in a separate thread.
            This can help speedup iteration times.

        """
        if isinstance(filename, Path):
            filename = str(filename.resolve())
        self._cap = cv2.VideoCapture(filename)
        self._frame_num = 0
        self._got = False
        self._length = int(self._cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self._fps = float(self._cap.get(cv2.CAP_PROP_FPS))
        self._width = int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self._height = int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self._channels = channels
        self._frame: np.ndarray = np.zeros(
            (self._height, self._width, self._channels),
            dtype=np.uint8,
        )

        # info for the thread
        self._thread_loads = use_thread
        if self._thread_loads:
            self._thread = Thread(target=self._run)
            self._frame_lock = Lock()
            self._condition = Condition()
            self._closed = False
            self._thread.start()

    def _run(self: Self) -> None:
        """Read the VideoCapture object."""
        while not self._closed:
            with self._frame_lock:
                if self._frame_num == self._length:
                    return
                self._got, self._frame = self._cap.read()
                self._frame_num += 1
            with self._condition:
                self._condition.wait()

    @property
    def frame(self: Self) -> np.ndarray:
        """
        Get the current frame.

        Returns
        -------
        numpy.ndarray
            The current frame.

        """
        return self._frame

    @property
    def frame_num(self: Self) -> int:
        """
        Get the current frame number.

        Returns
        -------
        int
            The current frame number.

        """
        return self._frame_num

    @property
    def success(self: Self) -> bool:
        """
        Get the success of the last frame read.

        Returns
        -------
        bool
            True if the frame was successfully loaded.

        """
        return self._got

    @property
    def length(self: Self) -> int:
        """
        Get the length of the video.

        Returns
        -------
        int
            The number of frames in the video.

        """
        return self._length

    @property
    def fps(self: Self) -> float:
        """
        Get the frames per second of the video.

        Returns
        -------
        float
            The frames per second of the video.

        """
        return self._fps

    @property
    def size(self: Self) -> tuple[int, int]:
        """
        Get the size of the video.

        Returns
        -------
        tuple
            The width and height of the video.

        """
        return (self._width, self._height)

    @property
    def channels(self: Self) -> int:
        """
        Get the number of channels in the video.

        Returns
        -------
        int
            The number of channels in the video.

        """
        return self._channels

    @property
    def width(self: Self) -> int:
        """
        Get the width of the video.

        Returns
        -------
        int
            The width of the video.

        """
        return self._width

    @property
    def height(self: Self) -> int:
        """
        Get the height of the video.

        Returns
        -------
        int
            The height of the video.

        """
        return self._height

    def _stop(self: Self) -> None:
        """Stop the video."""
        if self._thread_loads:
            self._closed = True
            with self._condition:
                self._condition.notify()
            self._thread.join()
            self._cap.release()
        else:
            self._cap.release()

    def __len__(self: Self) -> int:
        """
        Get the length of the video.

        Returns
        -------
        int
            The number of frames in the video.

        """
        return self.length

    def __iter__(self: Self) -> Self:
        """
        Get the iterator.

        Returns
        -------
        IterableVideo
            The current instance.

        """
        return self

    def __next__(self: Self) -> tuple[int, np.ndarray]:
        """
        Read the next frame from the video.

        Returns
        -------
        bool
            True if the frame was successfully loaded.
        numpy.ndarray
            The current frame.

        """
        if not self._thread_loads:
            self._got, self._frame = self._cap.read()
            self._frame_num += 1
            if not self._got:
                self._stop()
                raise StopIteration
            return self._frame_num, self._frame
        # otherwise use threading
        with self._frame_lock:
            if not self._got:
                self._stop()
                raise StopIteration
            num, frame = self._frame_num, self._frame
        with self._condition:
            self._condition.notify()
        return num, frame

    def read(self: Self) -> tuple[bool, np.ndarray]:
        """
        Read the next frame from the video.

        Returns
        -------
        bool
            True if the frame was successfully loaded.
        numpy.ndarray
            The current frame.

        """
        if not self._thread_loads:
            self._got, self._frame = self._cap.read()
            self._frame_num += 1
            return self._got, self._frame
        with self._frame_lock:
            return self._got, self._frame
