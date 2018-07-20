# coding: utf-8

import lyricwikia

lSongNames = ["10 Ribs & All/Carrot Pod Pod","Achilles Last Stand",
"All My Love",
"Babe I'm Gonna Leave You",
"Baby Come On Home" ,
"Bathroom Sound",
"The Battle of Evermore",
"Black Country Woman",
"Black Dog",
"Black Mountain Side",
"Blot",
"Bonzo's Montreux",
"Boogie with Stu",
"Brandy & Coke",
"Bring It On Home",
"Bron-Y-Aur Stomp",
"Bron-Yr-Aur",
"Candy Store Rock",
"Carouselambra",
"Celebration Day",
"Communication Breakdown",
"The Crunge",
"Custard Pie",
"C'mon Everybody",
"Dancing Days",
"Darlene",
"Dazed and Confused",
"Desire",
"Down by the Seaside",
"Driving Through Kashmir",
"D'yer Mak'er",
"The Epic",
"Everybody Makes It Through",
"Fool in the Rain",
"For Your Life",
"Four Sticks",
"Four Hands",
"Friends",
"Gallows Pole",
"The Girl I Love She Got Long Black Wavy Hair",
"Going to California",
"Good Times Bad Times",
"Hats Off to (Roy) Harper",
"Heartbreaker",
"Hey, Hey, What Can I Do",
"The Hook",
"Hot Dog",
"Hots On for Nowhere",
"Houses of the Holy",
"How Many More Times",
"I Can't Quit You Baby",
"If It Keeps On Raining",
"I'm Gonna Crawl",
"Immigrant Song",
"In My Time of Dying",
"In the Evening",
"In the Light",
"Jennings Farm Blues",
"Kashmir",
"Key to the Highway/Trouble in Mind",
"LA Drone",
"La La",
"The Lemon Song",
"Living Loving Maid (She's Just a Woman)",
"Misty Mountain Hop",
"Moby Dick",
"Night Flight",
"Nobody's Fault but Mine",
"No Quarter",
"The Ocean",
"Out on the Tiles",
"Over the Hills and Far Away",
"Ozone Baby",
"Poor Tom",
"The Rain Song",
"Ramble On",
"Rock and Roll",
"The Rover",
"Royal Orleans",
"Sick Again",
"Since I've Been Loving You",
"Somethin' Else",
"The Song Remains the Same",
"South Bound Saurez",
"Southbound Piano",
"St. Tristan's Sword",
"Stairway to Heaven",
"Sugar Mama",
"Sunshine Woman",
"Tangerine",
"Tea for One",
"Ten Years Gone",
"Thank You",
"That's the Way",
"Trampled Under Foot",
"Travelling Riverside Blues",
"Two Ones Are Won",
"Walter's Walk",
"The Wanton Song",
"Wearing and Tearing",
"We're Gonna Groove",
"What Is and What Should Never Be",
"When the Levee Breaks",
"White Summer/Black Mountain Side",
"Whole Lotta Love",
"You Shook Me",
"Your Time Is Gonna Come"]

sLyricsGlobal = "" # initialize global string
for sSongName in lSongNames:
    try:
        sLyrics = lyricwikia.get_lyrics('Led Zeppelin', sSongName)
    except:
        print "Lyrics not found for " + sSongName
    else:
        if sLyrics != "Instrumental":
            sFileName = sSongName.replace("'", "") # will cause weird file names
            sFileName = "-".join(sFileName.split()) # dashes where each space is
            sLyricsGlobal = sLyricsGlobal + " " + sLyrics # concatenate this song's lyrics to the global lyric object
            with open("lyrics/" + sFileName + ".txt", "w") as f: 
                f.write(sLyrics)
                f.close()
                print "Lyrics saved for " + sSongName
        else:
            print "Song was instrumental; not saving file or adding to global corpus"

with open("lyrics/input.txt", "w") as f:  # we use 'input.txt' as the global file name because thats what the word RNN uses
    f.write(sLyricsGlobal)
    f.close()
    print "Lyrics saved globally in input.txt"
            
            
            
            