
import random
from midi2audio import FluidSynth
import numpy as np
from midiutil.MidiFile import MIDIFile
import math
exportfile=""
notespeed=0
scale=0
octave=0
majormin=0
totallength=0
gchannels=0
mjminscale=[[0,2,4,5,7,9,11,12],[0,2,3,4,6,7,9,11]]

#cords=[[1,6,8,3,5,10],[2,7,9,4,6,11],[3,8,10,5,7,12],[4,9,11,1,6,8],[5,10,12,2,7,9]\
#,[1,6,11,3,8,10],[2,7,12,4,9,11],[1,3,8,5,10,12],[2,4,9,1,6,11],[3,5,10,2,7,12]\
#,[4,6,11,1,3,8],[5,7,12,2,4,9]]
    
cords=[[ 0,  5,  7,  2,  4,  9],\
       [ 1,  6,  8,  3,  5, 10],\
       [ 2,  7,  9,  4,  6, 11],\
       [ 3,  8, 10,  0,  5,  7],\
       [ 4,  9, 11,  1,  6,  8],\
       [ 0,  5, 10,  2,  7,  9],\
       [ 1,  6, 11,  3,  8, 10],\
       [ 0,  2,  7,  4,  9, 11],\
       [ 1,  3,  8,  0,  5, 10],\
       [ 2,  4,  9,  1,  6, 11],\
       [ 3,  5, 10,  0,  2,  7],\
       [ 4,  6, 11,  1,  3,  8],\
        [ 4,  9, 11,  1,  6,  8],\
        [ 0,  5, 10,  2,  7,  9],\
        [ 1,  6, 11,  3,  8, 10],\
        [ 0,  2,  7,  4,  9, 11],\
        [ 1,  3,  8,  0,  5, 10],\
        [ 2,  4,  9,  1,  6, 11],\
        [ 3,  5, 10,  0,  2,  7],\
        [ 4,  6, 11,  1,  3,  8],\
        [ 0,  5,  7,  2,  4,  9],\
        [ 1,  6,  8,  3,  5, 10],\
        [ 2,  7,  9,  4,  6, 11],\
        [ 3,  8, 10,  0,  5,  7]]

mjmincords=[[0,4,7],[0,3,7]]

def rando(index):
    rnd=random.randint(0, index-1)
    return rnd


def askscale():
    global scale
    scaleinput = input("What scale do you wnat to work with: ")
    if scaleinput=="A":
        scale=0
    elif scaleinput=="A#":
        scale=1
    elif scaleinput=="B":
        scale=2
    elif scaleinput=="C":
        scale=3
    elif scaleinput=="C#":
        scale=4
    elif scaleinput=="D":
        scale=5
    elif scaleinput=="D#":
        scale=6
    elif scaleinput=="E":
        scale=7
    elif scaleinput=="F":
        scale=8
    elif scaleinput=="F#":
        scale=9
    elif scaleinput=="G":
        scale=10
    elif scaleinput=="G#":
        scale=11
    else:
        print ("Invalid answer C sacle chosen") 
        scale=3

def majororminor():
    global majormin
    mjomi = input("Major (0) or Minor (1) scale: ")
    if mjomi=="0":
        majormin=0
    elif mjomi=="1":
        majormin=1
    else:
        print ("Invalid answer Major sacle chosen") 
        majormin=0
        
def octaveselect():
    global octave
    octavesel = input("What will be the main octave? (1-9): ")
    if octavesel=="1":
        octave=0
    elif octavesel=="2":
        octave=1
    elif octavesel=="3":
        octave=2
    elif octavesel=="4":
        octave=3
    elif octavesel=="5":
        octave=4
    elif octavesel=="6":
        octave=5
    elif octavesel=="7":
        octave=6
    elif octavesel=="8":
        octave=7
    elif octavesel=="9":
        octave=8
    else:
        print ("Invalid answer octave 4 chosen") 
        octave=3
        

        


def length():
    global totallength    
    length = int(input("How long in seconds should the comasotion be: "))
    if length>0:
        totallength = int(length)
    elif length<1:
        print ("Invalid answer length of 5 sec cosen") 
        totallength=5
    else:
        print ("Invalid answer length of 5 sec cosen") 
        totallength=5

def compose(MyMIDI,index):
    global scale
    global octave
    global majormin
    global totallength
    global mjminscale
    global cords
    global mjmincords
    global exportfile
    global notespeed
    global gchannels
    ind=0
    totaltime=totallength
    duration=0
    randcunt=0
    play=0
    time = 0   # In beats
    track = 0    
    tempo = 60     # In BPM
    melodynum=0
    melodykey=0
    melodyoct=0
    melcunt=0
    meltime=0
    degrees=[]
    melduration=0
    pmel=[]
    volume   = 100
     # One track, defaults to format 1 (tempo track
                     # automatically created)
    MyMIDI.addTrackName(track, time, "Sample Track")
    MyMIDI.addTempo(track, time, tempo)
    
    while ind < totaltime:
        init=rando(6)
        mainscale= np.add(mjminscale[majormin],21+12*octave).tolist()
        
        if majormin==0:
            play=cords[scale][init]
        elif majormin==1:
            play=cords[scale+12][init]
        else:
            print ("Cord Error")  
        if init>2:
            pcord=np.add(mjmincords[1],21+12*octave+play).tolist()

        elif init<3:
            pcord=np.add(mjmincords[0],21+12*octave+play).tolist()
        else:
            print ("Rand Error")  
        # melodynum=rando(4)
        # for mnum in range(melodynum):
        #     melodykey=rando(7)
        #     melodyoct=rando(3)
        #     pmel=(mjminscale[majormin][melodykey]+21+12*(octave+melodyoct-1))
        #     melduration=(rando(18)+1)/18
        #     meltime=ind
        #     degrees  = pmel
        #     channel  = index
        #     pitch = degrees
        #     MyMIDI.addNote(track, channel, pitch, meltime, melduration, volume)
        #     pmel=[]


        degrees  = pcord # MIDI note number
        channel  = index
        time     = ind
        
        if notespeed ==0:
            duration=1
        elif notespeed ==1:
           duration=0.5
           time = ind/2
           totaltime=totallength*2
        elif notespeed ==2:
              duration=0.25
              time = ind/4
              totaltime=totallength*4
        elif notespeed ==3:
            randcunt=randcunt+duration
            ind=math.floor(time)            
            time=randcunt+(rando(5)/2)
            duration=(rando(18)+1)/18
            # In beats
 # 0-127, as per the MIDI standard

        for pitch in degrees:
            MyMIDI.addNote(track, channel, pitch, time, duration, volume)
        ind=ind+1


# write it to disk
    return MyMIDI

    
    
#    fs = FluidSynth(sound_font='font.sf2')
        #   midi   
#    fs.midi_to_audio(exportfile, exportfile.replace(".mid",".mp3")) #  output.wav
    
def filename():
    global exportfile
    export = input("Export file name or file name and location:")
    exportfile=export+".mid"
    
def notespeedf():
    global notespeed
    speed= int(input("What do you wnat the speed of the notes to be 1 sec (0) , 0.5 sec (1), 0.25 sec (2) random (3): "))
    if speed==0:
        notespeed=0
    elif speed==1:
        notespeed=1
    elif speed==2:        
        notespeed=2
    elif speed==3:        
        notespeed=3
    else:      
        print ("Invalid answer random time is chosen") 
        notespeed=2

        

def start():
    global gchannels
    gchannels= int(input("How many channels do you want to write: "))
    MyMIDI = MIDIFile(gchannels)
    length()   
    filename()   
    for index in range(gchannels):
        askscale()
        majororminor()
        octaveselect()
        notespeedf()
        MIDI=compose(MyMIDI,index)
        
    with open(exportfile, "wb+") as output_file:
        MIDI.writeFile(output_file)
start()    