EXPECTED_DIFF = """{
    - follow: false
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: true
}"""

EXPECTED_DIFF_NESTED = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

EXPECTED_KEYS_GROUPS = {
    'union': {
        'group3',
        'common',
        'group2',
        'group1'
    },
    'common': {
        'common',
        'group1'
    },
    'missing': {
        'group2'
    },
    'new': {
        'group3'
    }
}

EXPECTED_DIFF_VIEW = {
    'common': {
        'type': 'changed_nested',
        'value': {
            'setting1': 'Value 1',
            'setting2': 200,
            'setting3': True,
            'setting6': {
                'doge': {
                    'wow': ''
                },
                'key': 'value'
            }
        },
        'changed_value': {
            'follow': {
                'type': 'added',
                'value': '',
                'changed_value': False
            },
            'setting1': {
                'type': 'no_change',
                'value': 'Value 1',
                'changed_value': 'Value 1'
            },
            'setting2': {
                'type': 'missing',
                'value': 200,
                'changed_value': ''
            },
            'setting3': {
                'type': 'changed',
                'value': True,
                'changed_value': None
            },
            'setting4': {
                'type': 'added',
                'value': '',
                'changed_value': 'blah blah'
            },
            'setting5': {
                'type': 'added_nested',
                'value': '',
                'changed_value': {
                    'key5': 'value5'
                }
            },
            'setting6': {
                'type': 'changed_nested',
                'value': {
                    'doge': {
                        'wow': ''
                    },
                    'key': 'value'
                },
                'changed_value': {
                    'doge': {
                        'type': 'changed_nested',
                        'value': {
                            'wow': ''
                        },
                        'changed_value': {
                            'wow': {
                                'type': 'changed',
                                'value': '',
                                'changed_value': 'so much'
                            }
                        }
                    },
                    'key': {
                        'type': 'no_change',
                        'value': 'value',
                        'changed_value': 'value'
                    },
                    'ops': {
                        'type': 'added',
                        'value': '',
                        'changed_value': 'vops'
                    }
                }
            }
        }
    },
    'group1': {
        'type': 'changed_nested',
        'value': {
            'baz': 'bas',
            'foo': 'bar',
            'nest': {
                'key': 'value'
            }
        },
        'changed_value': {
            'baz': {
                'type': 'changed',
                'value': 'bas',
                'changed_value': 'bars'
            },
            'foo': {
                'type': 'no_change',
                'value': 'bar',
                'changed_value': 'bar'
            },
            'nest': {
                'type': 'changed',
                'value': {
                    'key': 'value'
                },
                'changed_value': 'str'
            }
        }
    },
    'group2': {
        'type': 'missing_nested',
        'value': {
            'abc': 12345,
            'deep': {
                'id': 45
            }
        },
        'changed_value': ''
    },
    'group3': {
        'type': 'added_nested',
        'value': '',
        'changed_value': {
            'deep': {
                'id': {
                    'number': 45
                }
            },
            'fee': 100500
        }
    }
}
