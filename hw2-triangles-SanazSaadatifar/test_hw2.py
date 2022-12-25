import hw2_triangles as tri
class TestSample:
    """
    Autograder - *DO NOT* alter this file
    It tests if your functions are working as expected.
    """
    def test_real(self):
        """
        Tests the inequality sumations and valid lengths
        """
        assert callable(getattr(tri,'isReal')) , "isReal function not defined"
        assert isinstance(tri.isReal(0,0,0), bool) , "should return True or False"
        assert tri.isReal(1,1,1) , "basic triangle"
        assert not tri.isReal(1,2,3) , "1+2 is the same length as 3"
        assert not tri.isReal(3,2,1) , "1+2 is the same length as 3"
        assert not tri.isReal(-3,-4,-5) , "sides can't have negative length"
    
    def test_equilateral(self):
        """
        All sides are equal
        """
        assert callable(getattr(tri,'isEquilateral')) , "isEquilateral function not defined"
        assert isinstance(tri.isEquilateral(0,0,0), bool) , "should return True or False"
        assert tri.isEquilateral(1,1,1) , "basic Equilateral"
        assert not tri.isEquilateral(2,2,3) , "Isoscelese isn't Equilateral"
        assert not tri.isEquilateral(3,4,5) , "Scalene isn't Equilateral"
        assert not tri.isEquilateral(0,0,0) , "triangle should be real"
        assert not tri.isEquilateral(-1,-1,-1) , "triangle should be real"

    def test_isoscelese(self):
        """
        Two (and only two) sides match
        """
        assert callable(getattr(tri,'isIsosceles')) , "isIsosceles function not defined"
        assert isinstance(tri.isIsosceles(0,0,0), bool) , "should return True or False"
        assert tri.isIsosceles(3,2,2) , "basic Isoscelese 3-2-2"
        assert not tri.isIsosceles(3,3,3) , "Equilateral isn't Isoscelese"
        assert not tri.isIsosceles(3,4,5) , "Scalene isn't Isoscelese"
        assert not tri.isIsosceles(1,1,0) , "triangle should be real"
        assert not tri.isIsosceles(0,-1,-1) , "triangle should be real"
    
    def test_scalene(self):
        """
        All three sides are different lengths
        """
        assert callable(getattr(tri,'isScalene')) , "isScalene function not defined"
        assert isinstance(tri.isScalene(0,0,0), bool) , "should return True or False"
        assert tri.isScalene(3,4,5) , "classic Scalene 3-4-5"
        assert not tri.isScalene(3,3,3) , "Equilateral isn't Scalene"
        assert not tri.isScalene(3,2,3) , "Isoscelese isn't Scalene"
        assert not tri.isScalene(-3,-4,-5) , "triangle should be real"
    
    def test_pythagorean(self):
        """
        a*a + b*b = c*c including re-order
        """
        assert callable(getattr(tri,'isPythagorean')) , "isPythagorean function not defined"
        assert isinstance(tri.isPythagorean(0,0,0), bool) , "should return True or False"
        assert tri.isPythagorean(3,4,5) , "classic Pythagorean 3-4-5"
        assert tri.isPythagorean(13,12,5) , "classic Pythagorean 5-12-13 (check re-order)"
        assert not tri.isPythagorean(2,3,10) , "not Pythagorean"
        assert not tri.isPythagorean(-3,-4,-5) , "triangle should be real"
