#!/usr/bin/python3
from optparse import OptionParser
import eyed3
import os
from pathlib import Path

if __name__ == '__main__':
    oparser = OptionParser()
    oparser.add_option("--dir", dest="dir",
                       help="Directory to search for files to rename")
    oparser.add_option("--dest", dest="dest", default=".",
                       help="Directory to send files to")
    oparser.add_option("--overwrite", dest="overwrite", default=False,
                       action="store_true",
                       help="Overwrite target if exists.")
    (options, args) = oparser.parse_args()

    for f in os.listdir(options.dir):
        if f.endswith('.mp3'):
            path = os.path.abspath(os.path.join(options.dir, f))
            mp3_file = eyed3.load(path)
            if (mp3_file is not None
                and mp3_file.tag is not None
                and mp3_file.tag.artist is not None
                and mp3_file.tag.title is not None
                and mp3_file.tag.album is not None):
                target_dir = options.dest + '/' + mp3_file.tag.artist + '/' + mp3_file.tag.album
                target_file = target_dir + '/{0} - {1}.mp3'.format(mp3_file.tag.track_num[0], mp3_file.tag.title)
                if not os.path.isdir(target_dir):
                    Path(target_dir).mkdir(parents=True, exist_ok=True)
                if not os.path.exists(target_file) or options.overwrite:
                    try:
                        os.rename(path, target_file)
                        try:
                            print("{0} was successfully renamed using ID3 tags.".format(path.encode("utf-8")))
                        except:
                            print("Moved file")
                            pass
                    except OSError as ose:
                        "{0} could not be renamed.  Exception message: {1}".format(path, ose)
                else:
                    print("Target exists:{0}".format(target_file))    
