# Pedestrian Attribute Recognition and Attributed-based Person Retrieval Challenge at WACV 2023 (UPAR@WACV2023)

The UPAR@WACV2023 challenge includes separate tracks for Pedestrian Attribute Recognition and Attribute-based Person
Retrieval.
This challenge aims to spotlight the problem of domain gap in a real-world surveillance context and highlight the
challenges and limitations of existing methods to provide a direction of research for the future.
It will be based on an extenstion of the UPAR Dataset [1] composed of annotations for 40 binary attributes.

## Information
Challenge website: [UPAR Challenge](https://chalearnlap.cvc.uab.cat/challenge/52/description/)

Associated workshop: [Real-World Surveillance: Applications and Challenges Workshop](https://vap.aau.dk/rws-wacv2023/)

Challenge dataset: [UPAR dataset](https://arxiv.org/abs/2209.02522)

## Challenge Dataset
We will build on an extension of the UPAR dataset.
The challenge dataset consists of the harmonization of three public datasets (PA100K, PETA, and Market1501-Attributes) and a private test set.
40 binary attributes have been unified between those for which we provide additional annotations.
This dataset enables the investigation of Pedestrian Attribute Recognition (PAR) methods' generalization ability under different attribute distributions, viewpoints, varying illumination, and low resolutions.
The UPAR annotations and this repository are published under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/de/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License</a>.
If you use the UPAR dataset, please cite our paper as well as the papers of the sub-datasets (see [Dataset information](#Datasetinformation))
```
@article{specker2022upar,
  title={UPAR: Unified Pedestrian Attribute Recognition and Person Retrieval},
  author={Specker, Andreas and Cormier, Mickael and Beyerer, J{\"u}rgen},
  journal={arXiv preprint arXiv:2209.02522},
  year={2022}
}
```

## Starter Kit Usage
1. Install the python requirements.
```
conda env create -f environment.yml
conda activate rws-upar-challenge
```
2. Download the images, annotations, and templates for the development phase.
```
python download_datasets.py
```
3. The structure should now look as follows:
```
.
│── data/                               
│   ├── phase1/                         -> annotations for the development phase
│   │   │── train/                      -> train images with attribute labels for the three splits             
│   │   │   ├── train_0.csv
│   │   │   ├── train_1.csv
│   │   │   └── train_2.csv
│   │   ├── val_task1/                  -> information required for task 1 submissions to the evaluation server
│   │   │   └── val_all.csv             -> list of images for which predictions have to be submitted (Task 1 PAR)
│   │   └── val_task2/                  -> information required for task 2 submissions to the evaluation server
│   │       ├── val_imgs_0.csv          -> list of gallery images for split 0
│   │       ├── ...
│   │       ├── val_queries_0.csv       -> attribute queries for split 0
│   │       └── ...
│   ├── Market1501/                     -> Market1501 dataset
│   │   ├── bounding_box_test/
│   │   ├── bounding_box_train/
│   │   ├── query/
│   │   └── ...
│   ├── PA100k/                         -> PA100k dataset
│   │   └── release_data/
│   │       └── release_data/
│   └── PETA/                           -> PETA dataset
│       └── images/
└── submission_templates/
    ├── task1/                          -> submission template for task1
    └── task2/                          -> submission template for task2
```

## Dataset information
### PA-100K Dataset
Liu, Xihui, et al. "Hydraplus-net: Attentive deep features for pedestrian analysis." Proceedings of the IEEE international conference on computer vision. 2017.

https://github.com/xh-liu/HydraPlus-Net

License: [CC-BY 4.0 license "Creative Commons — Attribution 4.0 International — CC BY 4.0"](https://creativecommons.org/licenses/by/4.0/).

## PETA Dataset
Y. Deng, P. Luo, C. C. Loy, X. Tang, "Pedestrian attribute recognition at far distance," in Proceedings of ACM Multimedia (ACM MM), 2014

http://mmlab.ie.cuhk.edu.hk/projects/PETA.html

License: "This dataset is intended for research purposes only and as such cannot be used commercially. In addition, reference must be made to the aforementioned publications when this dataset is used in any academic and research reports."

## Market
Zheng, Liang, et al. "Scalable person re-identification: A benchmark." Proceedings of the IEEE international conference on computer vision. 2015.

https://drive.google.com/file/d/0B8-rUzbwVRk0c054eEozWG9COHM/view?resourcekey=0-8nyl7K9_x37HlQm34MmrYQ

License: No license available.


## License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/de/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License</a>.
