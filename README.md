# ezMP3

A library for getting info from MP3s

# Functions

`version()`\
Returns the current version of ezMP3.\
\
`super(path,tag)`\
Takes the path of an MP3 and a metadata tag(ex. album), then returns the\
value of the tag.\
\
`getTitle(path)`\
Returns the title of a specified MP3 file.\
\
`getAuthor(path)`\
Returns the artist of a specified MP3 file.\
\
`getAlbum(path)`\
Returns the album that a specified MP3 file corresponds to.\
\
`getLength(path)`
Returns the length of a song in milliseconds.\
\
`getYear(path)`\
Returns the year of a specified MP3 file.\
\
`getCover(path)`\
Returns the raw binary data from an extracted cover. To write this data you'll\
need to open a file in `"wb"` mode.\
\
*NOTE: getLength() and getCover are the only functions that don't use super()\
as their backend*\
\
*NOTE: getCover returns the cover in the `.png` format*\
