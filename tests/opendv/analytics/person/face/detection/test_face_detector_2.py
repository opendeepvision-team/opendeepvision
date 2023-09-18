import unittest

from opendv.analytics.person.face.detection import FaceDetector2

class TestFaceDetector2(unittest.TestCase):

    def test_get_property(self):
        face_detector = FaceDetector2()
        self.assertEqual(face_detector.name, 'RetinaFace')
        self.assertEqual(face_detector.alias, 'retinaface')

if __name__ == '__main__':
    unittest.main()