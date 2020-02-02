from unittest import TestCase
import area

class TestShapeAreas(TestCase):
    def test_triangle_area(self):
        # A trinagle with height4 and base 5 should have area 10

        #arrange
        base = 4
        height = 5
        expected_area = 10

        #action
        action_area = area.triangle_area(base, height)

        #assert
        self.assertEqual(expected_area, action_area)

    def test_triangle_area_floating_point(self):
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25, 4.91))

    def test_triangle_negative_height_base_raises_value_exception(self):

        with self.assertRaises(ValueError):
            area.triangle_area(9,-10)
        with self.assertRaises(ValueError):
            area.triangle_area(-9, 10)
        with self.assertRaises(ValueError):
            area.triangle_area(-9,-10)

    def test_triangle_base_height_zero(self):
        self.assertEqual(0, area.triangle_area(0,1))
        self.assertEqual(0, area.triangle_area(1,0))
        self.assertEqual(0, area.triangle_area(0,0))