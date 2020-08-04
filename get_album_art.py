import eyed3
import time, musicbrainzngs as mus
import os, glob,pathlib, os.path, sys

mus.set_useragent("Private app", "0.1")

# ************************
# *** Set music folder ***
# ************************
dirname ="/home/username/music/"

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

def album_list(files):
    albumlist = []
    for j in files:
        a = j.split(".", 1)[1]
        if a == "mp3":
            try:
                audiofile = eyed3.load(j)    
                artist = audiofile.tag.artist
                album = audiofile.tag.album
                albumlist.append((artist, album))
            except:
                next
    albumlist = list(dict.fromkeys(albumlist))
    return(albumlist)

def get_cover(artist, album, size=500, retry_delay=5, retries=5):
    try:
        data = mus.search_releases(artist=artist,
                                   release=album,
                                   limit=1)
        #release_id = data["release-list"][0]["id"]
        release_id = data["release-list"][0]["release-group"]["id"]
        print(f"album: Using release-id: {data['release-list'][0]['id']}")

        return mus.get_release_group_image_front(release_id,None )

    except mus.NetworkError:
        if retries == 0:
            raise mus.NetworkError("Failure connecting to MusicBrainz.org")
        print(f"warning: Retrying download. {retries} retries left!")
        time.sleep(retry_delay)
        get_cover(song, size, retries=retries - 1)

    except mus.ResponseError:
        print("error: Couldn't find album art for")
    except:
        next

liste = getListOfFiles(dirname)
albumlist = album_list(liste)
#print(albumlist)
print(len(albumlist))
input()
for j in albumlist:
    print(j)
    artist, album = j
    print(artist +" "+album)
    album_art = get_cover(artist, album)
    if album_art!= None: 
        filename = "images/" + artist + "-" + album + ".jpg"
        try:
            with open(filename, "wb") as file:
                file.write(album_art)
        except:
            next
