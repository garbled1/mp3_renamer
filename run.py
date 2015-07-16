from optparse import OptionParser
import eyed3
import os

if __name__ == '__main__':
    oparser = OptionParser()
    oparser.add_option("--dir", dest="dir", help="Directory to search for files to rename")
    (options, args) = oparser.parse_args()

    for f in os.listdir(options.dir):
        if f.endswith('.mp3'):
            path = os.path.abspath(os.path.join(options.dir, f))
            mp3_file = eyed3.load(path)
            if mp3_file.tag.artist is not None and mp3_file.tag.title is not None:
                try:
                    os.rename(path, "{0}/{1} - {2}.mp3".format(options.dir, mp3_file.tag.artist, mp3_file.tag.title))
                    print "{0} was successfully renamed using ID3 tags.".format(path)
                except Exception as e:
                    "{0} could not be renamed.  Exception: {1}".format(path, e)