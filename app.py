import pandas as pd

# Top 50 Spotify Songs of 2019
data = [
    ["Blinding Lights", "The Weeknd", 4922606449],
    ["Dance Monkey", "Tones and I", 3287800985],
    ["Señorita", "Shawn Mendes & Camila Cabello", 3052894588],
    ["Watermelon Sugar", "Harry Styles", 3052405517],
    ["Don't Start Now", "Dua Lipa", 2976230197],
    ["Cruel Summer", "Taylor Swift", 2972355747],
    ["Circles", "Post Malone", 2883347756],
    ["bad guy", "Billie Eilish", 2760083427],
    ["7 rings", "Ariana Grande", 2571640384],
    ["Memories", "Maroon 5", 2299382057],
    ["Before You Go", "Lewis Capaldi", 2234410822],
    ["The Box", "Roddy Ricch", 2192038746],
    ["La Canción", "J Balvin & Bad Bunny", 2132894110],
    ["Roses", "SAINt JHN", 2080013549],
    ["HIGHEST IN THE ROOM", "Travis Scott", 2064103543],
    ["I Don’t Care", "Ed Sheeran & Justin Bieber", 2024540000],
    ["everything i wanted", "Billie Eilish", 1911235412],
    ["Adore You", "Harry Styles", 1894112385],
    ["Lover", "Taylor Swift", 1803247623],
    ["Ransom", "Lil Tecca", 1770543125],
    ["Callaita", "Bad Bunny", 1642503188],
    ["Tusa", "Karol G & Nicki Minaj", 1634441350],
    ["Under the Influence", "Chris Brown", 1631098834],
    ["No Me Conoce", "Jhay Cortez, J Balvin, Bad Bunny", 1601058321],
    ["ROXANNE", "Arizona Zervas", 1563241009],
    ["Sucker", "Jonas Brothers", 1553182440],
    ["Ride It", "Regard", 1543495812],
    ["Dancing With A Stranger", "Sam Smith & Normani", 1521834444],
    ["Con Calma", "Daddy Yankee ft. Snow", 1519388822],
    ["Beautiful People", "Ed Sheeran ft. Khalid", 1492088412],
    ["MIDDLE CHILD", "J. Cole", 1442183321],
    ["Falling", "Harry Styles", 1420341890],
    ["Arcade", "Duncan Laurence", 1400321401],
    ["Goodbyes", "Post Malone ft. Young Thug", 1383345100],
    ["Lose You To Love Me", "Selena Gomez", 1374400811],
    ["hot girl bummer", "blackbear", 1361231999],
    ["Astronaut In The Ocean", "Masked Wolf", 1351173000],
    ["Streets", "Doja Cat", 1341228000],
    ["If the World Was Ending", "JP Saxe ft. Julia Michaels", 1300984321],
    ["Say So", "Doja Cat", 1300119900],
    ["China", "Anuel AA, Daddy Yankee, Karol G, Ozuna, J Balvin", 1290887234],
    ["Boy With Luv", "BTS ft. Halsey", 1280345678],
    ["Truth Hurts", "Lizzo", 1272244567],
    ["You Need To Calm Down", "Taylor Swift", 1261343421],
    ["Panini", "Lil Nas X", 1250194455],
    ["Graveyard", "Halsey", 1239887221],
    ["Bop", "DaBaby", 1234012298],
    ["Someone You Loved", "Lewis Capaldi", 1220134459],
    ["Walk Me Home", "P!nk", 1200988000],
    ["Wow.", "Post Malone", 1199990000]
]
# Create DataFrame
df = pd.DataFrame(data, columns=["Track Name", "Artist", "Streams (2019)"])

# Save to CSV
df.to_csv("top_50_spotify_2019.csv", index=False)
print("CSV file 'top_50_spotify_2019.csv' created successfully.")