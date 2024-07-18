#Mutagen user guide
#https://mutagen.readthedocs.io/en/latest/user/index.html

from mutagen.easyid3 import EasyID3
import glob
import PySimpleGUI as sg

###Global Variables
ArtistUpdate = False
AlbumUpdate = False
# AlbumArtistUpdate = False
# ContributingArtistsUpdate = False
# TrackUpdate = False
Artist = "Radiohead"
Album = "Radiohead: Greatest Hits Disk 1"
# AlbumArtist = ""
# ContributingArtists = []
# Track = ""
AlbumPath = 'C:\\Users\\slane\\Music\\Radiohead\\Radiohead - Greatest Hits Vol 1\\*'
###Global Variables

###Main
def main():
    print('Running quickedit.py')
    # print(EasyID3.valid_keys.keys())
    run_GUI()
    modify() 
###Main

###Run GUI
def run_GUI():
    # global AlbumPath
    global ArtistUpdate
    global AlbumUpdate
    global Artist
    global Album
    
    print('run GUI')
    layout = [
        [sg.Button('Select Folder', disabled=True)],
        [sg.Checkbox('Artist', default=False, k='k_ArU'), sg.Input(key='k_Ar')],
        [sg.Checkbox('Album', default=False, k='k_AlU'), sg.Input(key='k_Al')],
        # [sg.Checkbox('Album Artist', default=False, k='k_AlArU'), sg.Input(key='k_AlAr')],
        [sg.Button('OK')]]
    window = sg.Window('Hello World', layout)
    while True:
        event, values = window.read()
        #End program if user closes window or
        #presses the OK button
        if event == 'OK':
            # print('GUI closing')
            ArtistUpdate = True if values['k_ArU'] == True else False
            AlbumUpdate = True if values['k_AlU'] == True else False
            # AlbumArtistUpdate = True if values['k_AlArU'] == True else False
            Artist = values['k_Ar']
            Album = values['k_Al']
            # AlbumArtist = values['k_AlAr']
            break
        elif event == sg.WIN_CLOSED:
            quit()
        if event == 'Select Folder':
            AlbumPath = sg.popup_get_folder('Choose your folder', keep_on_top=True)
            print('Folder Selected: ' + AlbumPath)
    window.close()
    print('GUI closed')
    print('ArtistUpdate: ' + str(ArtistUpdate) + ' to ' + Artist)
    print('AlbumUpdate: ' + str(AlbumUpdate) + ' to ' + Album)
    # print('AlbumUpdate: ' + str(AlbumArtistUpdate) + ' to ' + AlbumArtist)
###Run GUI

###Modify Album Info
def modify():
    # global AlbumPath
    global ArtistUpdate
    global AlbumUpdate
    global Artist
    global Album
    
    print('run modify')
    print(AlbumPath)
    print('Update Artist ' + str(ArtistUpdate) + ', to: ' + Artist)
    print('Update Album ' + str(AlbumUpdate) + ', to: ' + Album)

    audiofiles = []
    
    for file in glob.glob(AlbumPath):
        audiofiles.append(file)
        
    if ArtistUpdate:
        print('Updating Artist to: ' + Artist)
        for file in audiofiles:
            audio = EasyID3(file)
            audio['artist'] = Artist
            audio.save()
        
    if AlbumUpdate:
        print('Updating Album to: ' + Album)
        for file in audiofiles:
            audio = EasyID3(file)
            audio['album'] = Album
            audio.save()
            
    # if AlbumArtistUpdate:
        # for file in audiofiles:
            # audio = EasyID3(file)
            # audio['albumartist'] = AlbumArtist
            # audio.save()
            
    print('Artist, Album, Track')
            
    for file in audiofiles:
        audio = EasyID3(file)
        # print(audio['artist'] + audio['albumartist'] + audio['album'] + audio['title'])
        print(audio['artist'] + audio['album'] + audio['title'])
###Modify Album Info
    
if __name__ == '__main__':
    main()