EXPECTED_KEYS_GROUPS = {
    "common": "nested",
    "group1": "nested",
    "group2": "missing_nested",
    "group3": "added_nested",
}


EXPECTED_DIFF_VIEW = {
    "common": {
        "type": "nested",
        "value": {
            "setting2": {
                "type": "missing",
                "value": 200,
                "changed_value": None,
            },
            "setting4": {
                "type": "added",
                "value": "blah blah",
                "changed_value": None,
            },
            "follow": {"type": "added", "value": False, "changed_value": None},
            "setting5": {
                "type": "added_nested",
                "value": {
                    "key5": {
                        "type": "no_change",
                        "value": "value5",
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
            "setting6": {
                "type": "nested",
                "value": {
                    "ops": {
                        "type": "added",
                        "value": "vops",
                        "changed_value": None,
                    },
                    "doge": {
                        "type": "nested",
                        "value": {
                            "wow": {
                                "type": "changed",
                                "value": "",
                                "changed_value": "so much",
                            }
                        },
                        "changed_value": None,
                    },
                    "key": {
                        "type": "no_change",
                        "value": "value",
                        "changed_value": None,
                    },
                },
                "changed_value": None,
            },
            "setting1": {
                "type": "no_change",
                "value": "Value 1",
                "changed_value": None,
            },
            "setting3": {
                "type": "changed",
                "value": True,
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
    "group1": {
        "type": "nested",
        "value": {
            "nest": {
                "type": "changed_nested",
                "value": {
                    "key": {
                        "type": "no_change",
                        "value": "value",
                        "changed_value": None,
                    }
                },
                "changed_value": "str",
            },
            "foo": {
                "type": "no_change",
                "value": "bar",
                "changed_value": None,
            },
            "baz": {
                "type": "changed",
                "value": "bas",
                "changed_value": "bars",
            },
        },
        "changed_value": None,
    },
    "group2": {
        "type": "missing_nested",
        "value": {
            "abc": {
                "type": "no_change",
                "value": 12345,
                "changed_value": None,
            },
            "deep": {
                "type": "nested",
                "value": {
                    "id": {
                        "type": "no_change",
                        "value": 45,
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
    "group3": {
        "type": "added_nested",
        "value": {
            "fee": {
                "type": "no_change",
                "value": 100500,
                "changed_value": None,
            },
            "deep": {
                "type": "nested",
                "value": {
                    "id": {
                        "type": "nested",
                        "value": {
                            "number": {
                                "type": "no_change",
                                "value": 45,
                                "changed_value": None,
                            }
                        },
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
}
