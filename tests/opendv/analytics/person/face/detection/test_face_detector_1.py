import unittest

from opendv.analytics.person.face.detection import FaceDetector1

class TestFaceDetector1(unittest.TestCase):

    def test_get_property(self):
        face_detector = FaceDetector1()
        name = "MTCNN"
        description = "Joint face detection and alignment using multitask cascaded convolutional networks"
        alias = "mtcnn"
        paper_url = "https://ieeexplore.ieee.org/document/7553523"
        arxiv_url = "https://arxiv.org/abs/1604.02878"
        code_url = "https://github.com/ipazc/mtcnn"
        bibtex = [
				"@article{Zhang_2016, doi = {10.1109/lsp.2016.2603342}, url = {https://doi.org/10.1109%2Flsp.2016.2603342}, year = 2016, month = {oct}, publisher = {Institute of Electrical and Electronics Engineers ({IEEE})}, volume = {23}, number = {10}, pages = {1499--1503}, author = {Kaipeng Zhang and Zhanpeng Zhang and Zhifeng Li and Yu Qiao}, title = {Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks}, journal = {{IEEE} Signal Processing Letters} }"
		]
        class_name = "FaceDetector1"
        self.assertEqual(face_detector.name, name)
        self.assertEqual(face_detector.description, description)
        self.assertEqual(face_detector.alias, alias)
        self.assertEqual(face_detector.paper_url, paper_url)
        self.assertEqual(face_detector.arxiv_url, arxiv_url)
        self.assertEqual(face_detector.code_url, code_url)
        self.assertListEqual(face_detector.bibtex, bibtex)
        self.assertEqual(face_detector.class_name, class_name)
        self.assertEqual(face_detector.min_face_size, 20)
        self.assertEqual(face_detector.scale_factor, 0.709)
        self.assertIsNone(face_detector.steps_threshold)
        

if __name__ == '__main__':
    unittest.main()