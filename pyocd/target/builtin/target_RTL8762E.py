# pyOCD debugger
# Copyright (c) 2023 PyOCD Authors
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FLASH_ALGO = {
    'load_address' : 0x00200000,

    # Flash algorithm as a hex string
    'instructions': [
    0xe7fdbe00,
    0x47702000, 0x47702000, 0x47702000, 0x47702000, 0x47702000, 0x47702000, 0x47704408, 0x00000000
    ],

    # Relative function addresses
    'pc_init': 0x00200005,
    'pc_unInit': 0x00200009,
    'pc_program_page': 0x00200015,
    'pc_erase_sector': 0x00200011,
    'pc_eraseAll': 0x0020000d,

    'static_base' : 0x00200000 + 0x00000004 + 0x0000001c,
    'begin_stack' : 0x00205030,
    'end_stack' : 0x00204030,
    'begin_data' : 0x00200000 + 0x1000,
    'page_size' : 0x2000,
    'analyzer_supported' : False,
    'analyzer_address' : 0x00000000,
    # Enable double buffering
    'page_buffers' : [
        0x00200030,
        0x00202030
    ],
    'min_program_length' : 0x2000,

    # Relative region addresses and sizes
    'ro_start': 0x4,
    'ro_size': 0x1c,
    'rw_start': 0x20,
    'rw_size': 0x4,
    'zi_start': 0x24,
    'zi_size': 0x0,

    # Flash information
    'flash_start': 0x8000000,
    'flash_size': 0x1000000,
    'sector_sizes': (
        (0x0, 0x40000),
    )
}

from ...coresight.coresight_target import CoreSightTarget
from ...core.memory_map import (FlashRegion, RamRegion, MemoryMap)

class RTL8762E(CoreSightTarget):

    VENDOR = "Realtek Semiconductor"

    MEMORY_MAP = MemoryMap(
        FlashRegion(    start=0x800000,  length=0x1000000, blocksize=0x800, is_boot_memory=True, algo=FLASH_ALGO),
        RamRegion(      start=0x200000,  length=0x24000),
        RamRegion(      start=0x224000,  length=0x2000),
        RamRegion(      start=0x226000,  length=0x2000),
        RamRegion(      start=0x280000,  length=0x8000)
        )

    def __init__(self, session):
        super(RTL8762E, self).__init__(session, self.MEMORY_MAP)
