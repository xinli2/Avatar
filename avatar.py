###
### Author: Xin Li
### Description:  In this assignment, you will
### be writing a console-based avatar creation
### tool. The program that you build will allow
### the user to build a custom avatar, or select
### from 3 pre-designed ones. The avatars that
### this program will create will not be of just
### a face, but rather, an avatar body. All of
### the interaction for this program will happen
### on the command-line.
### Name of this program is: avatar.py
###
print('----- AVATAR -----')
select = input('Select an Avatar or create your own:\n')
while select !='custom'and select !='exit' and select !='Jeff' and select != 'Adam' and select != 'Chris':
    select = input('Select an Avatar or create your own:\n')
def main ():
    if select != 'exit':
        if select == 'custom':
            print('Answer the following questions to create a custom avatar')
            creation ()
        elif select == 'Jeff':
            Jeff ()
        elif select == 'Adam':
            Adam ()
        elif select == 'Chris':
            Chris()
def creation ():
    cap = input('Hat style ?\n')
    eye = input('Character for eyes ?\n')
    hair = input('Shaggy hair (True/False) ?\n')
    arm = input('Arm style ?\n')
    torso = int(input('Torso length ?\n'))
    leg = int(input('Leg length (1-4) ?\n'))
    shose = input('Shoe look ?\n')
    print()
    cap_style(cap)
    hair_style(hair)
    face(eye)
    Arm_Style(arm)
    Torso_Length(torso)
    Leg_length(leg)
    shose_style(shose)
def Jeff():
    print()
    cap_style('both')
    hair_style('True')
    face('0')
    Arm_Style('=')
    Torso_Length(2)
    Leg_length(2)
    shose_style('#HHH#')
def Adam():
    print()
    cap_style('right')
    hair_style('False')
    face('*')
    Torso_Length(1)
    Arm_Style('T')
    Torso_Length(3)
    Leg_length(3)
    shose_style('<|||>')
def Chris():
    print()
    cap_style('front')
    hair_style('True')
    face('U')
    Torso_Length(1)
    Arm_Style('W')
    Torso_Length(1)
    Leg_length(4)
    shose_style('<>-<>')
def cap_style (cap):
    if cap == 'right' :
        print(' '*7,'~-~            ',sep='')
        print(' '*5,'/-~-~-\        ',sep='')
        print(' '*4,'/_______\___     ',sep='')
    elif cap == 'left' :
        print(' '*7,'~-~            ',sep='')
        print(' '*5,'/-~-~-\        ',sep='')
        print(' ','___/_______\   ',sep='')
    elif cap == 'both' :
        print(' '*7,'~-~            ',sep='')
        print(' '*5,'/-~-~-\        ',sep='')
        print(' ','___/_______\___',sep='')
    elif cap == 'front':
        print(' '*7,'~-~       ',sep='')
        print(' '*5,'/-~-~-\   ',sep='')
        print(' '*4,'/_______\   ',sep='')
def face (eye):
    print(' '*4,'|',' ',eye,'   ',eye,' ','|',sep='')
    print(' '*4,'|   V   |    ',sep='')
    print(' '*4,'|  ~~~  |    ',sep='')
    print(' '*5,'\_____/     ',sep='')
def hair_style (hair):
    if hair == 'True':
        print(' '*4,'|"""""""|',sep='')
    elif hair == 'False':
        print(" "*4,"|'''''''|",sep='')
def Arm_Style (arm):
        print(' ','0',arm*4,'|---|',arm*4,'0',sep='')
def Torso_Length(torso):
    i = 0
    while i < torso:
        print(' '*6,'|-X-|',sep='')
        i += 1
def Leg_length(leg):
    print(' '*6,'HHHHH',sep='')
    i = 0
    while i < leg :
        print(' '*(5-i),'///', ' '*(2*i+1), '\\\\\\',sep='')
        i += 1
def shose_style (shose):
    print(shose,' '*7,shose,sep='')
main()
