import unittest
from volume import calculer_volume_sphere


class TestVolumeSphere(unittest.TestCase):
    def test_calculer_volume_sphere_positif(self):
        self.assertAlmostEqual(calculer_volume_sphere(2), 33.51032, places=5)

    def test_calculer_volume_sphere_nuls(self):
        self.assertEqual(calculer_volume_sphere(0), 0)

    def test_calculer_volume_sphere_négatif(self):
        self.assertAlmostEqual(calculer_volume_sphere(-3), -113.09734, places=5)

    def test_calculer_volume_sphere_float(self):
        self.assertAlmostEqual(calculer_volume_sphere(2.5), 65.44985, places=5)


if __name__ == "__main__":
    unittest.main()
