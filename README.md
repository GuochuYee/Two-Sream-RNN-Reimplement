# Two-Sream-RNN-Reimplement(PyTorch framework)
In this project, I reimplemented the method reported in the paper "Modeling Temporal Dynamics and Spatial Configurations of Actions Using Two-Stream Recurrent Neural Networks"(which can be found here: https://openaccess.thecvf.com/content_cvpr_2017/papers/Wang_Modeling_Temporal_Dynamics_CVPR_2017_paper.pdf) on NTU RGB+D Dataset.
## 1 NTU RGB+D Dataset: 
- Download the dataset

a) project page：http://rose1.ntu.edu.sg/Datasets/actionRecognition.asp
b) github reference: https://github.com/shahroudy/NTURGB-D
c) github reference: https://github.com/kdkalvik/skeleton-action-recognition  
- Execute 'ntu_dataset_main.py' to generate 'all_train_sample.pkl' and 'all_test_sample.pkl' files.
```python
python ntu_dataset_main.py
```
## 3 Results:
<img width="316" alt="image" src="https://user-images.githubusercontent.com/94251855/153308995-46a15750-40cb-4b43-b888-b1302a913021.png">

<img width="387" alt="image" src="https://user-images.githubusercontent.com/94251855/153309106-19813887-f33e-4203-a27c-cb9aa6d76070.png">
