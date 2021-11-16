#!/usr/bin/env python3

import attr

from openedx_events.avro_attrs_bridge import AvroAttrsBridge

def test_base_types():
    @attr.s(auto_attribs=True)
    class SubTest:
        sub_name: str
        course_id: str

    @attr.s(auto_attribs=True)
    class Test:
        name: str
        course_id: str
        user_id: int
        more: SubTest

    bridge = AvroAttrsBridge(Test)

    # A test record that we can try to serialize to avro.
    record = Test("foo", "bar.course", 1, SubTest("a.sub.name", "a.nother.course"))
    serialized_record = bridge.serialize(record)

    # Try to de-serialize back to an attrs class.
    object_from_wire = bridge.deserialize(serialized_record)
    assert record == object_from_wire
