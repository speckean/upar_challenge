# Pedestrian Attribute Recognition and Attributed-based Person Retrieval Challenge at WACV 2024 (UPAR@WACV2024)

The UPAR@WACV2024 challenge includes separate tracks for Pedestrian Attribute Recognition and Attribute-based Person
Retrieval.
This challenge aims to spotlight the problem of domain gap in a real-world surveillance context and highlight the
challenges and limitations of existing methods to provide a direction of research for the future.
It will be based on an extenstion of the UPAR Dataset [1] composed of annotations for 40 binary attributes.

## News
- 2024-01-07 Challenge paper is published [here](https://openaccess.thecvf.com/content/WACV2024W/RWS/html/Cormier_UPAR_Challenge_2024_Pedestrian_Attribute_Recognition_and_Attribute-Based_Person_Retrieval_WACVW_2024_paper.html)
- 2023-10-16 Decryption key: UVk4yayzy38zEMKH
- 2023-10-13 Encrypted test data is now available [here](https://drive.google.com/file/d/1eJKKvWenl6aQE76D0j0asf3YVthVvqpq/view?usp=sharing). Decryption key will be released on Oct 16th.

## Information
Challenge website: [UPAR Challenge](https://chalearnlap.cvc.uab.cat/challenge/52/description/)

Associated workshop: [Real-World Surveillance: Applications and Challenges Workshop](https://vap.aau.dk/rws-wacv2024/)

Challenge dataset: [UPAR dataset](https://openaccess.thecvf.com/content/WACV2023/papers/Specker_UPAR_Unified_Pedestrian_Attribute_Recognition_and_Person_Retrieval_WACV_2023_paper.pdf)

Challenge results 2023: [UPAR@WACV2023](https://openaccess.thecvf.com/content/WACV2023W/RWS/papers/Cormier_UPAR_Challenge_Pedestrian_Attribute_Recognition_and_Attribute-Based_Person_Retrieval_--_WACVW_2023_paper.pdf)

Original UPAR dataset: [Github](https://github.com/speckean/upar_dataset)

## Challenge Dataset
We will build on an extension of the UPAR dataset.
The challenge dataset consists of the harmonization of three public datasets (PA100K, PETA, and Market1501-Attributes) and a private test set.
40 binary attributes have been unified between those for which we provide additional annotations.
This dataset enables the investigation of Pedestrian Attribute Recognition (PAR) methods' generalization ability under different attribute distributions, viewpoints, varying illumination, and low resolutions.
The UPAR annotations and this repository are published under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/de/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License</a>.
If you use the UPAR dataset, please cite our paper as well as the papers of the sub-datasets (see [Dataset information](#Datasetinformation))
```
@inproceedings{specker2023upar,
  title={UPAR: Unified pedestrian attribute recognition and person retrieval},
  author={Specker, Andreas and Cormier, Mickael and Beyerer, J{\"u}rgen},
  booktitle={Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision},
  pages={981--990},
  year={2023}
}

@inproceedings{cormier2023upar,
  title={UPAR Challenge: Pedestrian Attribute Recognition and Attribute-Based Person Retrieval--Dataset, Design, and Results},
  author={Cormier, Mickael and Specker, Andreas and Junior, Julio and Jacques, CS and Florin, Lucas and Metzler, J{\"u}rgen and Moeslund, Thomas B and Nasrollahi, Kamal and Escalera, Sergio and Beyerer, J{\"u}rgen},
  booktitle={Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision},
  pages={166--175},
  year={2023}
}

@InProceedings{Cormier_2024_WACV,
    author    = {Cormier, Mickael and Specker, Andreas and Junior, Julio C. S. Jacques and Moritz, Lennart and Metzler, J\"urgen and Moeslund, Thomas B. and Nasrollahi, Kamal and Escalera, Sergio and Beyerer, J\"urgen},
    title     = {UPAR Challenge 2024: Pedestrian Attribute Recognition and Attribute-Based Person Retrieval - Dataset, Design, and Results},
    booktitle = {Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) Workshops},
    month     = {January},
    year      = {2024},
    pages     = {359-367}
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
│   │   │   └── train.csv
│   │   ├── val_task1/                  -> information required for task 1 submissions to the evaluation server
│   │   │   └── val.csv                 -> list of images for which predictions have to be submitted (Task 1 PAR)
│   │   └── val_task2/                  -> information required for task 2 submissions to the evaluation server
│   │       ├── val_imgs.csv            -> list of gallery images
│   │       └── val_queries.csv         -> attribute queries
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
