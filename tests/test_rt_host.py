# SPDX-License-Identifier: BSD-2-Clause

# RTEMS Tools Project (http://www.rtems.org/)
# Copyright (C) 2020-2024 Amar Takhar <amar@rtems.org>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import re
import pytest

from rtemstoolkit import host


def test_cpu():
    assert type(host.cpus()) is int


def test_overrides():
    assert type(host.overrides()) is dict


def test_label_system():
    assert host.label(mode="system") is not None


def test_label_compact():
    assert re.match("^[a-zA-Z]*-.*-.*$", host.label(mode="compact"))


def test_label_extended():
    assert re.match("^[a-zA-Z]* .*$", host.label(mode="extended"))


def test_label_extended():
    assert re.match("^[a-zA-Z]* .*$", host.label(mode="extended"))


def test_label_all():
    assert re.match("^[a-zA-Z]*-.*-.* \\(.*\\)$", host.label(mode="all"))


def test_label_error():
    from rtemstoolkit.error import general
    with pytest.raises(general,
                       match=r"^error: invalid platform mode: _nonexistent_$"):
        assert host.label(mode="_nonexistent_")
