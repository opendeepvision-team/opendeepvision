import unittest

from opendv.analytics.person.face.detection import FaceDetector

class TestFaceDetector(unittest.TestCase):

    def test_get_property(self):
        # Test for FaceDetector1
        face_detector = FaceDetector()
        config = self.get_face_detector_config()
        id = config['default']
        algorithm = config['algorithms'][id]
        self.assertEqual(face_detector.name, algorithm['name'])
        self.assertEqual(face_detector.description, algorithm['description'])
        self.assertEqual(face_detector.alias, algorithm['alias'])
        self.assertEqual(face_detector.paper_url, algorithm['paper_url'])
        self.assertEqual(face_detector.arxiv_url, algorithm['arxiv_url'])
        self.assertEqual(face_detector.code_url, algorithm['code_url'])
        self.assertListEqual(face_detector.bibtex, algorithm['bibtex'])
        self.assertEqual(face_detector.class_name, algorithm['class_name'])
        self.assertEqual(face_detector.min_face_size, 20)
        self.assertEqual(face_detector.scale_factor, 0.709)
        self.assertIsNone(face_detector.steps_threshold)
        # Test for FaceDetector1
        face_detector = FaceDetector(id=1)
        config = self.get_face_detector_config()
        id = '1'
        algorithm = config['algorithms'][id]
        self.assertEqual(face_detector.name, algorithm['name'])
        self.assertEqual(face_detector.description, algorithm['description'])
        self.assertEqual(face_detector.alias, algorithm['alias'])
        self.assertEqual(face_detector.paper_url, algorithm['paper_url'])
        self.assertEqual(face_detector.arxiv_url, algorithm['arxiv_url'])
        self.assertEqual(face_detector.code_url, algorithm['code_url'])
        self.assertListEqual(face_detector.bibtex, algorithm['bibtex'])
        self.assertEqual(face_detector.class_name, algorithm['class_name'])
        self.assertEqual(face_detector.min_face_size, 20)
        self.assertEqual(face_detector.scale_factor, 0.709)
        self.assertIsNone(face_detector.steps_threshold)
        # Test for FaceDetector1
        face_detector = FaceDetector(alias='mtcnn')
        config = self.get_face_detector_config()
        id = '1'
        algorithm = config['algorithms'][id]
        self.assertEqual(face_detector.name, algorithm['name'])
        self.assertEqual(face_detector.description, algorithm['description'])
        self.assertEqual(face_detector.alias, algorithm['alias'])
        self.assertEqual(face_detector.paper_url, algorithm['paper_url'])
        self.assertEqual(face_detector.arxiv_url, algorithm['arxiv_url'])
        self.assertEqual(face_detector.code_url, algorithm['code_url'])
        self.assertListEqual(face_detector.bibtex, algorithm['bibtex'])
        self.assertEqual(face_detector.class_name, algorithm['class_name'])
        self.assertEqual(face_detector.min_face_size, 20)
        self.assertEqual(face_detector.scale_factor, 0.709)
        self.assertIsNone(face_detector.steps_threshold)
        # Test for FaceDetector2
        face_detector = FaceDetector(id=2)
        config = self.get_face_detector_config()
        id = '2'
        algorithm = config['algorithms'][id]
        self.assertEqual(face_detector.name, algorithm['name'])
        self.assertEqual(face_detector.description, algorithm['description'])
        self.assertEqual(face_detector.alias, algorithm['alias'])
        self.assertEqual(face_detector.paper_url, algorithm['paper_url'])
        self.assertEqual(face_detector.arxiv_url, algorithm['arxiv_url'])
        self.assertEqual(face_detector.code_url, algorithm['code_url'])
        self.assertListEqual(face_detector.bibtex, algorithm['bibtex'])
        self.assertEqual(face_detector.class_name, algorithm['class_name'])
        # Test for FaceDetector2
        face_detector = FaceDetector(alias='retinaface')
        config = self.get_face_detector_config()
        id = '2'
        algorithm = config['algorithms'][id]
        self.assertEqual(face_detector.name, algorithm['name'])
        self.assertEqual(face_detector.description, algorithm['description'])
        self.assertEqual(face_detector.alias, algorithm['alias'])
        self.assertEqual(face_detector.paper_url, algorithm['paper_url'])
        self.assertEqual(face_detector.arxiv_url, algorithm['arxiv_url'])
        self.assertEqual(face_detector.code_url, algorithm['code_url'])
        self.assertListEqual(face_detector.bibtex, algorithm['bibtex'])
        self.assertEqual(face_detector.class_name, algorithm['class_name'])
    
    def test_set_property(self):
        # Test for FaceDetector1
        face_detector = FaceDetector()
        face_detector.min_face_size = 30
        self.assertEqual(face_detector.min_face_size, 30)
        # Test for FaceDetector1
        face_detector = FaceDetector(id=1)
        face_detector.min_face_size = 40
        self.assertEqual(face_detector.min_face_size, 40)
        # Test for FaceDetector1
        face_detector = FaceDetector(alias='mtcnn')
        face_detector.min_face_size = 50
        self.assertEqual(face_detector.min_face_size, 50)
    
    def test_create_instance(self):
        # Test for FaceDetector1
        min_face_size = 30
        scale_factor = 0.7
        steps_threshold = [0.1, 0.2, 0.3]
        face_detector = FaceDetector(min_face_size=min_face_size,
                                      scale_factor=scale_factor,
                                      steps_threshold=steps_threshold)
        self.assertEqual(face_detector.min_face_size, min_face_size)
        self.assertEqual(face_detector.scale_factor, scale_factor)
        self.assertListEqual(face_detector.steps_threshold, steps_threshold)
        # Test for FaceDetector1
        min_face_size = 40
        scale_factor = 0.8
        steps_threshold = [0.4, 0.5, 0.6]
        face_detector = FaceDetector(id=1, 
                                     min_face_size=min_face_size,
                                      scale_factor=scale_factor,
                                      steps_threshold=steps_threshold)
        self.assertEqual(face_detector.min_face_size, min_face_size)
        self.assertEqual(face_detector.scale_factor, scale_factor)
        self.assertListEqual(face_detector.steps_threshold, steps_threshold)
        # Test for FaceDetector1
        min_face_size = 50
        scale_factor = 0.9
        steps_threshold = [0.6, 0.7, 0.7]
        face_detector = FaceDetector(alias='mtcnn', 
                                     min_face_size=min_face_size,
                                      scale_factor=scale_factor,
                                      steps_threshold=steps_threshold)
        self.assertEqual(face_detector.min_face_size, min_face_size)
        self.assertEqual(face_detector.scale_factor, scale_factor)
        self.assertListEqual(face_detector.steps_threshold, steps_threshold)
    
    def get_face_detector_config(self):
        config = {
            'default': '1',
            'algorithms': {
                '1': {
                    'name': 'MTCNN', 
                    'description': 'Joint face detection and alignment using multitask cascaded convolutional networks', 
                    'alias': 'mtcnn', 
                    'paper_url': 'https://ieeexplore.ieee.org/document/7553523', 
                    'arxiv_url': 'https://arxiv.org/abs/1604.02878', 
                    'code_url': 'https://github.com/ipazc/mtcnn', 
                    'bibtex': [
                        '@article{Zhang_2016, doi = {10.1109/lsp.2016.2603342}, url = {https://doi.org/10.1109%2Flsp.2016.2603342}, year = 2016, month = {oct}, publisher = {Institute of Electrical and Electronics Engineers ({IEEE})}, volume = {23}, number = {10}, pages = {1499--1503}, author = {Kaipeng Zhang and Zhanpeng Zhang and Zhifeng Li and Yu Qiao}, title = {Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks}, journal = {{IEEE} Signal Processing Letters} }'
                    ], 
                    'class_name': 'FaceDetector1'
                }, 
                '2': {
                    'name': 'RetinaFace', 
                    'description': 'Single-shot multi-level face localisation in the wild', 
                    'alias': 'retinaface', 
                    'paper_url': 'https://ieeexplore.ieee.org/document/9157330', 
                    'arxiv_url': 'https://arxiv.org/abs/1905.00641', 
                    'code_url': 'https://github.com/serengil/retinaface', 
                    'bibtex': [
                        '@InProceedings{Deng_2020_CVPR, author = {Deng, Jiankang and Guo, Jia and Ververas, Evangelos and Kotsia, Irene and Zafeiriou, Stefanos}, title = {RetinaFace: Single-Shot Multi-Level Face Localisation in the Wild}, booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}, month = {June}, year = {2020} }', 
                        '@inproceedings{serengil2020lightface, title = {LightFace: A Hybrid Deep Face Recognition Framework}, author = {Serengil, Sefik Ilkin and Ozpinar, Alper}, booktitle = {2020 Innovations in Intelligent Systems and Applications Conference (ASYU)}, pages = {23-27}, year = {2020}, doi = {10.1109/ASYU50717.2020.9259802}, url = {https://doi.org/10.1109/ASYU50717.2020.9259802}, organization = {IEEE} }'
                    ], 
                    'class_name': 'FaceDetector2'
                }
            }
        }
        return config

if __name__ == '__main__':
    unittest.main()