import unittest

from opendv.analytics.person.face.detection import FaceDetector

class TestFaceDetector(unittest.TestCase):

    def test_get_property(self):
        face_detector = FaceDetector()
        self.assertEqual(face_detector.name, 'MTCNN')
        self.assertEqual(face_detector.alias, 'mtcnn')
        self.assertEqual(face_detector.min_face_size, 20)
        self.assertEqual(face_detector.scale_factor, 0.709)

if __name__ == '__main__':
    unittest.main()