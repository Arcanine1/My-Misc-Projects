from Board import Board
from Tile import Tile
import numpy as np
import neat
import os
import copy
import visualize


p =neat.Checkpointer.restore_checkpoint("neat-checkpoint-296")