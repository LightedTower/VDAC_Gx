#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Wed Nov  9 16:24:37 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'AttRewPy1'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Volumes/GoogleDrive-110921232830228762532/My Drive/LAVA Lab Resources/Experiments/VDAC_Gx Team/AttRewPy1/AttRewPy1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "trial" ---
fixation_small = visual.ImageStim(
    win=win,
    name='fixation_small', 
    image='images/Fix_Dot.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.005, 0.005),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fixation_large = visual.ImageStim(
    win=win,
    name='fixation_large', 
    image='images/Fix_Dot.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.01, 0.01),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
targ = visual.ImageStim(
    win=win,
    name='targ', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
dist1 = visual.ImageStim(
    win=win,
    name='dist1', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
dist2 = visual.ImageStim(
    win=win,
    name='dist2', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
dist3 = visual.ImageStim(
    win=win,
    name='dist3', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
dist4 = visual.ImageStim(
    win=win,
    name='dist4', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
dist5 = visual.ImageStim(
    win=win,
    name='dist5', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('AttRewPy1_Conditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    targ.setPos((targ_x, targ_y))
    targ.setImage(targ_img)
    dist1.setPos((dist1_x, dist1_y))
    dist1.setImage(dist1_img)
    dist2.setPos((dist2_x, dist2_y))
    dist2.setImage(dist2_img)
    dist3.setPos((dist3_x, dist3_y))
    dist3.setImage(dist3_img)
    dist4.setPos((dist4_x, dist4_y))
    dist4.setImage(dist4_img)
    dist5.setPos((dist5_x, dist5_y))
    dist5.setImage(dist5_img)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [fixation_small, fixation_large, targ, dist1, dist2, dist3, dist4, dist5, key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_small* updates
        if fixation_small.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            fixation_small.frameNStart = frameN  # exact frame index
            fixation_small.tStart = t  # local t and not account for scr refresh
            fixation_small.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_small, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_small.started')
            fixation_small.setAutoDraw(True)
        if fixation_small.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_small.tStartRefresh + .266-frameTolerance:
                # keep track of stop time/frame for later
                fixation_small.tStop = t  # not accounting for scr refresh
                fixation_small.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_small.stopped')
                fixation_small.setAutoDraw(False)
        
        # *fixation_large* updates
        if fixation_large.status == NOT_STARTED and tThisFlip >= 0.766-frameTolerance:
            # keep track of start time/frame for later
            fixation_large.frameNStart = frameN  # exact frame index
            fixation_large.tStart = t  # local t and not account for scr refresh
            fixation_large.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_large, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_large.started')
            fixation_large.setAutoDraw(True)
        
        # *targ* updates
        if targ.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            targ.frameNStart = frameN  # exact frame index
            targ.tStart = t  # local t and not account for scr refresh
            targ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(targ, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'targ.started')
            targ.setAutoDraw(True)
        if targ.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > targ.tStartRefresh + .660-frameTolerance:
                # keep track of stop time/frame for later
                targ.tStop = t  # not accounting for scr refresh
                targ.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'targ.stopped')
                targ.setAutoDraw(False)
        
        # *dist1* updates
        if dist1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            dist1.frameNStart = frameN  # exact frame index
            dist1.tStart = t  # local t and not account for scr refresh
            dist1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dist1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dist1.started')
            dist1.setAutoDraw(True)
        if dist1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dist1.tStartRefresh + .660-frameTolerance:
                # keep track of stop time/frame for later
                dist1.tStop = t  # not accounting for scr refresh
                dist1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dist1.stopped')
                dist1.setAutoDraw(False)
        
        # *dist2* updates
        if dist2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            dist2.frameNStart = frameN  # exact frame index
            dist2.tStart = t  # local t and not account for scr refresh
            dist2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dist2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dist2.started')
            dist2.setAutoDraw(True)
        if dist2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dist2.tStartRefresh + .660-frameTolerance:
                # keep track of stop time/frame for later
                dist2.tStop = t  # not accounting for scr refresh
                dist2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dist2.stopped')
                dist2.setAutoDraw(False)
        
        # *dist3* updates
        if dist3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            dist3.frameNStart = frameN  # exact frame index
            dist3.tStart = t  # local t and not account for scr refresh
            dist3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dist3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dist3.started')
            dist3.setAutoDraw(True)
        if dist3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dist3.tStartRefresh + 0.660-frameTolerance:
                # keep track of stop time/frame for later
                dist3.tStop = t  # not accounting for scr refresh
                dist3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dist3.stopped')
                dist3.setAutoDraw(False)
        
        # *dist4* updates
        if dist4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            dist4.frameNStart = frameN  # exact frame index
            dist4.tStart = t  # local t and not account for scr refresh
            dist4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dist4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dist4.started')
            dist4.setAutoDraw(True)
        if dist4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dist4.tStartRefresh + 0.660-frameTolerance:
                # keep track of stop time/frame for later
                dist4.tStop = t  # not accounting for scr refresh
                dist4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dist4.stopped')
                dist4.setAutoDraw(False)
        
        # *dist5* updates
        if dist5.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            dist5.frameNStart = frameN  # exact frame index
            dist5.tStart = t  # local t and not account for scr refresh
            dist5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dist5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dist5.started')
            dist5.setAutoDraw(True)
        if dist5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dist5.tStartRefresh + .660-frameTolerance:
                # keep track of stop time/frame for later
                dist5.tStop = t  # not accounting for scr refresh
                dist5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dist5.stopped')
                dist5.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['y','n','left','right','space','a','l'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(corr_ans)) or (key_resp.keys == corr_ans):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corr_ans).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
