import hw4_nasa as nasa
class TestSample:
    """
    Autograder - *DO NOT* alter this file
    It tests if your functions are working as expected.
    """
    def test_reading(self):
        """
        Test reading from a file converting to list
        """
        assert callable(getattr(nasa,'fileToList')) , "fileToList function not defined"
        result = nasa.fileToList("test_data.txt")
        assert isinstance(result, list) , "should return a list of strings"
        assert result == ["1","2","3"] , "Double check you're reading the file correctly, creating a new list, and stripping the new line chracter"
    
    def test_converstion(self):
        """
        Test the conversion from list of strings to list of floats
        """
        assert callable(getattr(nasa,'strListToFloatList')) , "strListToFloatList function not defined"
        assert isinstance(nasa.strListToFloatList([]), list) , "should return a list"
        assert nasa.strListToFloatList([]) == [] , "Parameter was empty list should return empty list"
        data = ["1.1","2","3"]
        result = nasa.strListToFloatList(data)
        assert result == [1.1,2.0,3.0] , "Double check you are using floats when returning the new list"
        assert data == ["1.1","2","3"] , "Do not change the inputed list, create a new one and return that"
        

    def test_mini(self):
        """
        The index of the smallest element
        """
        assert callable(getattr(nasa,'minIndex')) , "minIndex function not defined"
        assert isinstance(nasa.minIndex([1,2,3]),int) , "minIndex should return an integer"
        assert nasa.minIndex([1,2,3]) == 0 , "Index 0 was the smallest"
        assert nasa.minIndex([3,2,1]) == 2 , "Index 2 was the smallest"
        assert nasa.minIndex([]) == -1 , "Should return -1 for empty list"

    def test_maxi(self):
        """
        The index of the largest element
        """
        assert callable(getattr(nasa,'maxIndex')) , "maxIndex function not defined"
        assert isinstance(nasa.maxIndex([1,2,3]),int) , "maxIndex should return an integer"
        assert nasa.maxIndex([1,2,3]) == 2 , "Index 2 was the largest"
        assert nasa.maxIndex([3,2,1]) == 0 , "Index 0 was the largest"
        assert nasa.maxIndex([]) == -1 , "Should return -1 for empty list"        
    