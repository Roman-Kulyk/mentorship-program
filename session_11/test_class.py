class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")


    def test_three(self):
        x = 'R2D2'
        assert '2' in x
