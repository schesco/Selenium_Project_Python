class expect:
    @staticmethod
    def equal(actual, expected):
        assert actual == expected

    @staticmethod
    def true(condition):
        assert condition

    @staticmethod
    def contains(actual, expected):
        assert expected in actual
