import pygame
from utils.board import Board
from utils.constants import WIDTH, HEIGHT, FPS
from utils.real_time_emotion_detector import *
import numpy as np
import subprocess
import random


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mainline.digital')

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()


    while run:
        clock.tick(FPS)
        
        run_real_time_emotion_detector(
            classifier_algorithm='RandomForest',  # Alternatively 'SVM'.
            predictor_path='utils/shape_predictor_68_face_landmarks.dat',
            dataset_csv='utils/data/csv/dataset.csv',
            dataset_images_dir='utils/data/raw'
        )
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        board.draw_cubes(WIN)
        pygame.display.update()

    pygame.quit()

main()