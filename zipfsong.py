__author__ = 'brett'

import sys

def compute_zipf(track_number):
    return 1/track_number

def compute_quality(play_count, zipf_score):
    return play_count / zipf_score

line = sys.stdin.readline()
(m, n) = line.split(' ')
n = int(n.rstrip('\n'))
songs = {}
for track_number in range(int(m)):
    song_line = sys.stdin.readline()
    (play_count, track_name) = song_line.split()
    song_quality = compute_quality(float(play_count), compute_zipf(float(track_number) + 1))
    if song_quality in songs:
        same_quality_list = songs[song_quality]
        same_quality_list.append(track_name)
    else:
        songs[song_quality] = [track_name]

printed = 0
for song in reversed(sorted(songs.iterkeys())):
    for curr_song in songs[song]:
        print curr_song
        printed += 1
        if printed == n:
            exit()