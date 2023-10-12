EXPECTED_DIFF = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

EXPECTED_DIFF_PLAIN = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

EXPECTED_DIFF_JSON = """{
    "common": {
        "type": "nested",
        "value": {
            "follow": {
                "type": "added",
                "value": false,
                "changed_value": null
            },
            "setting1": {
                "type": "no_change",
                "value": "Value 1",
                "changed_value": null
            },
            "setting2": {
                "type": "missing",
                "value": 200,
                "changed_value": null
            },
            "setting3": {
                "type": "changed",
                "value": true,
                "changed_value": null
            },
            "setting4": {
                "type": "added",
                "value": "blah blah",
                "changed_value": null
            },
            "setting5": {
                "type": "added_nested",
                "value": {
                    "key5": {
                        "type": "no_change",
                        "value": "value5",
                        "changed_value": null
                    }
                },
                "changed_value": null
            },
            "setting6": {
                "type": "nested",
                "value": {
                    "doge": {
                        "type": "nested",
                        "value": {
                            "wow": {
                                "type": "changed",
                                "value": "",
                                "changed_value": "so much"
                            }
                        },
                        "changed_value": null
                    },
                    "key": {
                        "type": "no_change",
                        "value": "value",
                        "changed_value": null
                    },
                    "ops": {
                        "type": "added",
                        "value": "vops",
                        "changed_value": null
                    }
                },
                "changed_value": null
            }
        },
        "changed_value": null
    },
    "group1": {
        "type": "nested",
        "value": {
            "baz": {
                "type": "changed",
                "value": "bas",
                "changed_value": "bars"
            },
            "foo": {
                "type": "no_change",
                "value": "bar",
                "changed_value": null
            },
            "nest": {
                "type": "changed_nested",
                "value": {
                    "key": {
                        "type": "no_change",
                        "value": "value",
                        "changed_value": null
                    }
                },
                "changed_value": "str"
            }
        },
        "changed_value": null
    },
    "group2": {
        "type": "missing_nested",
        "value": {
            "abc": {
                "type": "no_change",
                "value": 12345,
                "changed_value": null
            },
            "deep": {
                "type": "nested",
                "value": {
                    "id": {
                        "type": "no_change",
                        "value": 45,
                        "changed_value": null
                    }
                },
                "changed_value": null
            }
        },
        "changed_value": null
    },
    "group3": {
        "type": "added_nested",
        "value": {
            "deep": {
                "type": "nested",
                "value": {
                    "id": {
                        "type": "nested",
                        "value": {
                            "number": {
                                "type": "no_change",
                                "value": 45,
                                "changed_value": null
                            }
                        },
                        "changed_value": null
                    }
                },
                "changed_value": null
            },
            "fee": {
                "type": "no_change",
                "value": 100500,
                "changed_value": null
            }
        },
        "changed_value": null
    }
}"""
