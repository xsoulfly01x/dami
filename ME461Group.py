import numpy as np
import time
class ME461Group:
    '''
    This is the random player used in the colab example.
    Edit this file properly to turn it into your submission or generate a similar file that has the same minimal class structure.
    You have to replace the name of the class (ME461Group) with one of the following (exactly as given below) to match your group name
        atlas
        backspacex
        ducati
        hepsi1
        mechrix
        meturoam
        nebula
        ohmygroup
        tulumba
    After you edit this class, save it as groupname.py where groupname again is exactly one of the above
    '''
    def __init__(self, userName, clrDictionary, maxStepSize, maxTime):
        self.name = userName # your object will be given a user name, i.e. your group name
        self.maxStep = maxStepSize # maximum length of the returned path from run()
        self.maxTime = maxTime # run() is supposed to return before maxTime

  
    def run(self, img, info):
        myinfo = info[self.name]
        imS = img.shape[0] # assume square image and get size
        # get current location 
        loc, game_point = info[self.name]
        y,x = loc # get current y,x coordinates
        # a very simple randomizer
        maxL = self.maxStep # total travel
        dx = int(np.random.randint(1, int(maxL/2)) * np.sign(np.random.randn()))
        if x + dx < imS and x + dx > 0:
            nx = x + dx
        else:
            nx = x - dx
        maxL = maxL -abs(dx) # remaining travel
        dy = int(np.random.randint(1, maxL - 5) * np.sign(np.random.randn()))
        if y + dy < imS and y + dy > 0:
            ny = y + dy
        else:
            ny= y - dy        
        maxL = maxL - abs(dy)
        dx2 = int(maxL * np.sign(np.random.randn()))
        if nx + dx2 < imS and nx + dx2 > 0:
            nx2 = nx + dx2
        else:
            nx2 = nx - dx2       
        # right before return wait a certain amount of time
        time.sleep(self.maxTime * np.random.rand())
        return [[25, 175], [26, 175], [27, 175], [28, 175], [29, 175], [30, 175], [31, 175], [32, 175], [33, 175], [34, 175], [35, 175], [36, 175], [37, 175], [38, 175], [39, 175], [40, 175], [41, 175], [42, 175], [43, 175], [44, 175], [45, 175], [46, 175], [47, 175], [48, 175], [49, 175], [50, 175], [51, 175], [52, 175], [53, 175], [54, 175], [55, 175], [56, 175], [57, 175], [58, 175], [59, 175], [60, 175]]
