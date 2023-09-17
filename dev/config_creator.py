import os
import json
import argparse

# analytics.person.face.detection
def create_analytics_person_face_detection(module):
    # create config path
    config_path = module.split('.')
    config_path.insert(0, '..')
    config_path.append('config.json')
    config_path = os.sep.join(config_path)
    # create config content
    bibtex = ''
    config_content = {
        'default': '1',
        'algorithms': {
            '1': {
                'name': 'MTCNN', 
                'description': 'Joint face detection and alignment using multitask cascaded convolutional networks', 
                'alias': 'mtcnn', 
                'paper_url': 'https://ieeexplore.ieee.org/document/7553523', 
                'arxiv_url': 'https://arxiv.org/abs/1604.02878', 
                'code_url': 'https://github.com/ipazc/mtcnn', 
                'bibtex': '@article{Zhang_2016, doi = {10.1109/lsp.2016.2603342}, url = {https://doi.org/10.1109%2Flsp.2016.2603342}, year = 2016, month = {oct}, publisher = {Institute of Electrical and Electronics Engineers ({IEEE})}, volume = {23}, number = {10}, pages = {1499--1503}, author = {Kaipeng Zhang and Zhanpeng Zhang and Zhifeng Li and Yu Qiao}, title = {Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks}, journal = {{IEEE} Signal Processing Letters} }', 
                'class_name': 'FaceDetector1'
            }
        }
    }
    # write config content into config path
    with open(config_path, 'w') as f:
        json.dump(config_content, f, indent='\t')

def main():
    parser = argparse.ArgumentParser(description='Config Creator Tool')
    parser.add_argument('--module', type=str)
    args = parser.parse_args()

    if args.module == 'analytics.person.face.detection':
        create_analytics_person_face_detection(args.module)

if __name__ == '__main__':
    main()