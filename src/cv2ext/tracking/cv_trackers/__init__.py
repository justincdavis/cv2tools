# Copyright (c) 2024 Justin Davis (davisjustin302@gmail.com)
#
# MIT License
"""
Contains the wrapped OpenCV trackers.

Classes
-------
:class:`BoostingTracker`
    A class for tracking objects in videos using the Boosting tracker.
:class:`CSRTTracker`
    A class for tracking objects in videos using the CSRT tracker.
:class:`KCFTracker`
    A class for tracking objects in videos using the KCF tracker.
:class:`MedianFlowTracker`
    A class for tracking objects in videos using the MedianFlow tracker.
:class:`MILTracker`
    A class for tracking objects in videos using the MIL tracker.
:class:`MOSSETracker`
    A class for tracking objects in videos using the MOSSE tracker.
:class:`TLDTracker`
    A class for tracking objects in videos using the TLD tracker.

"""

from __future__ import annotations

from ._boosting import BoostingTracker
from ._csrt import CSRTTracker
from ._kcf import KCFTracker
from ._medianflow import MedianFlowTracker
from ._mil import MILTracker
from ._mosse import MOSSETracker
from ._tld import TLDTracker

__all__ = [
    "BoostingTracker",
    "CSRTTracker",
    "KCFTracker",
    "MILTracker",
    "MOSSETracker",
    "MedianFlowTracker",
    "TLDTracker",
]
