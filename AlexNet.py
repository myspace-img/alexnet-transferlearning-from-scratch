# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:57:40 2021

@author: cgnya
"""

import torch
from torch import nn
class AlexNet(nn.Module):

    def __init__(self, num_classes = 10):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(64, 192, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
        )
        self.avgpool = nn.AdaptiveAvgPool2d((6, 6))
        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(4096, 1024), # (4096, 4096) --> (4096, 1024) to avoid overfitting and heavy losses during training
            nn.ReLU(inplace=True),
            nn.Linear(1024, num_classes),
        )
    

    def forward(self, x):
        '''
        Parameters
        ----------
        x : Input Image 
            An Input image of size 256x256x3.

        Returns
        -------
        x : Output Tensor
            Flattened 1-Dimensional Tensor providing scores for 10 classes.

        '''
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x
    
    
