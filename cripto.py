from cryptography.fernet import Fernet
from os.path import exists
import csv

if not(exists('chave.key')):
    chave = Fernet.generate_key()
    with open('chave.key', 'wb') as filekey: 
        filekey.write(chave)

with open('chave.key', 'rb') as filekey:
    chave = filekey.read()

fernet = Fernet(chave)

arquivo = csv.reader(open('SpotifyTracks.csv'), delimiter=',')

encriptado = open('SpotifyTracksCripto.csv', 'w', newline='', encoding='utf-8')

write = csv.writer(encriptado, delimiter=',')
header = ['_id', 'artist_name', 'danceability', 'duration_ms', 'genre', 'loudness', 'popularity', 'track_name']
write.writerow(header)

for [_id, artist_name, danceability, duration_ms, genre, loudness, popularity, track_name] in arquivo:
    track_name = fernet.encrypt(track_name.encode())
    write.writerow([_id, artist_name, danceability, duration_ms, genre, loudness, popularity, track_name])