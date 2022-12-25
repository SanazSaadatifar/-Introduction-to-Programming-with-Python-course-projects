import hw3_cycles as cyc
class TestSample:
    """
    Autograder - *DO NOT* alter this file
    It tests if your functions are working as expected.
    """
    path = [1,2,3,0]
    unit = [0]
    def test_unit(self):
        """
        Tests that the path [0] is recognized as a unit path
        """
        assert callable(getattr(cyc,'isUnitPath')) , "isUnitPath function not defined"
        assert isinstance(cyc.isUnitPath(self.unit), bool) , "should return True or False"
        assert cyc.isUnitPath(self.unit) , "[0] is a unit path"
        assert not cyc.isUnitPath(self.path) , "[1,2,3,0] is not [0]"
        assert self.path == [1,2,3,0] , "path list was changed"
        assert not cyc.isUnitPath([]) , "empty path list [] is not a unit path"
    
    def test_matching(self):
        """
        Test a path that points to itself
        """
        assert callable(getattr(cyc,'hasMatchingIndex')) , "hasMatchingIndex function not defined"
        assert isinstance(cyc.hasMatchingIndex(self.unit), bool) , "should return True or False"
        assert cyc.hasMatchingIndex(self.unit) , "[0] points to itself"
        assert not cyc.hasMatchingIndex(self.path) , "[1,2,3,0] never points to itself"
        assert self.path == [1,2,3,0] , "path list was changed"
        assert cyc.hasMatchingIndex([0,1,2,3,4,5]) , "[0,1,2,3,4,5] always points to itself"
        assert not cyc.hasMatchingIndex([5,4,3,2,1,0]) , "[5,4,3,2,1,0] never points to itself"
        assert not cyc.hasMatchingIndex([]) , "empty path list [] has no matches"
    
    def test_invalid(self):
        """
        Test to see if any element of the path is outside of the range
        """
        assert callable(getattr(cyc,'hasInvalidEntry')) , "hasInvalidEntry function not defined"
        assert isinstance(cyc.hasInvalidEntry(self.unit), bool) , "should return True or False"
        assert cyc.hasInvalidEntry([-1]) , "-1 is invalid"
        assert cyc.hasInvalidEntry([1]) , "1 is invalid when the length is 1"
        assert cyc.hasInvalidEntry([0,1,2,3,4,6]) , "6 is invalid when the length is 6"
        assert not cyc.hasInvalidEntry(self.unit) , "[0] doesn't have an invalid entry"
        assert not cyc.hasInvalidEntry(self.path) , "[1,2,3,0] doesn't have an invalid entry"
        assert self.path == [1,2,3,0] , "path list was changed"
        assert cyc.hasInvalidEntry([]) , "empty path list is invalid"

    def test_numbers(self):
        """
        Test if the path has every number
        """
        assert callable(getattr(cyc,'hasEveryNumber')) , "hasInvalidEntry function not defined"
        assert isinstance(cyc.hasEveryNumber(self.unit), bool) , "should return True or False"
        assert cyc.hasEveryNumber(self.unit) , "[0] contains every possible number"
        assert cyc.hasEveryNumber([1,0]) , "[1,0] contains every possible number"
        assert cyc.hasEveryNumber([1,2,0]) , "[1,2,0] contains every possible number"
        assert cyc.hasEveryNumber(self.path) , "[1,2,3,0] has every entry"
        assert self.path == [1,2,3,0] , "path list was changed"
        assert not cyc.hasEveryNumber([1,2,3,4,5,1]) , "missing entry zero"
        assert not cyc.hasEveryNumber([0,1,2,3,4,5,6,6]) , "should include 7"
        assert not cyc.hasEveryNumber([]) , "empty path list [] has no numbers"
    
    def test_cycle_length(self):
        """
        Test computing the length of any given cycle
        """
        assert callable(getattr(cyc,'cycleLength')) , "hasInvalidEntry function not defined"
        assert isinstance(cyc.cycleLength(self.unit), int) , "should return an integer"
        assert cyc.cycleLength([-1]) == 0, "[-1] has an invalid length should return 0"
        assert cyc.cycleLength(self.unit) == 1, "[0] has one element in its path"
        assert cyc.cycleLength(self.path) == 4, "[1,2,3,0] has 4 elements in its path"
        assert self.path == [1,2,3,0] , "path list was changed"
        assert cyc.cycleLength([]) == 0, "empty list has a path length of zero"