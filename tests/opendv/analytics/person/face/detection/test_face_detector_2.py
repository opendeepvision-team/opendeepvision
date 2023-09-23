import unittest

from opendv.analytics.person.face.detection import FaceDetector2

class TestFaceDetector2(unittest.TestCase):

    def test_get_property(self):
        face_detector = FaceDetector2()
        name = "RetinaFace"
        description = "Single-shot multi-level face localisation in the wild"
        alias = "retinaface"
        paper_url = "https://ieeexplore.ieee.org/document/9157330"
        arxiv_url = "https://arxiv.org/abs/1905.00641"
        code_url = "https://github.com/serengil/retinaface"
        bibtex = [
				"@InProceedings{Deng_2020_CVPR, author = {Deng, Jiankang and Guo, Jia and Ververas, Evangelos and Kotsia, Irene and Zafeiriou, Stefanos}, title = {RetinaFace: Single-Shot Multi-Level Face Localisation in the Wild}, booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}, month = {June}, year = {2020} }",
				"@inproceedings{serengil2020lightface, title = {LightFace: A Hybrid Deep Face Recognition Framework}, author = {Serengil, Sefik Ilkin and Ozpinar, Alper}, booktitle = {2020 Innovations in Intelligent Systems and Applications Conference (ASYU)}, pages = {23-27}, year = {2020}, doi = {10.1109/ASYU50717.2020.9259802}, url = {https://doi.org/10.1109/ASYU50717.2020.9259802}, organization = {IEEE} }"
		]
        class_name = "FaceDetector2"
        self.assertEqual(face_detector.name, name)
        self.assertEqual(face_detector.description, description)
        self.assertEqual(face_detector.alias, alias)
        self.assertEqual(face_detector.paper_url, paper_url)
        self.assertEqual(face_detector.arxiv_url, arxiv_url)
        self.assertEqual(face_detector.code_url, code_url)
        self.assertListEqual(face_detector.bibtex, bibtex)
        self.assertEqual(face_detector.class_name, class_name)

if __name__ == '__main__':
    unittest.main()