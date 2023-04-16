import os
import logging
import hashlib
from urllib.request import urlopen
from os.path import exists
from pathlib import Path

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def download_and_check(filename, url, hash):
    hash_md5 = hashlib.md5()
    logger = logging.getLogger("mkdocs.download_and_check")
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    if not exists(filename):
        Path(cur_dir + '/' + filename.rsplit('/',1)[0]).mkdir(parents=True, exist_ok=True)
        with urlopen(url) as response:
            filecontent = response.read()
            hash_md5.update(filecontent)
            hash_check = hash_md5.hexdigest()
            if hash == hash_check:
                with open(Path(cur_dir + '/' + filename), 'wb') as file:
                    file.write(filecontent)
                    logger.info('downloaded external asset "' + filename + '"')
            else:
                logger.error('error downloading asset "' + filename + '" hash mismatch!')
                os._exit(1)

def on_files(files, config, **kwargs):
    for file in files:
        ext = file.src_path.rsplit('.',1)[1].lower()
        if ext == "png" or ext == "jpg" or ext == "jpeg" or ext == "svg":
            hash = md5(file.abs_src_path)
            filename, ext =  file.abs_dest_path.rsplit('.',1)
            filename = filename + "_" + hash
            file.abs_dest_path = filename + "." + ext
            filename, ext =  file.url.rsplit('.',1)
            filename = filename + "_" + hash
            file.url = filename + "." + ext
            #file.name = file.name + "_test_url"

def get_external_assets(config, **kwargs):
    download_and_check('theme_override/assets/fonts/lobster-v28-latin-regular.woff',
        'https://fonts.gstatic.com/s/lobster/v28/neILzCirqoswsqX9zoKmNQ.woff',
        '1575124e09b3ac03144d0de24e1ad5c9')
    download_and_check('theme_override/assets/fonts/lobster-v28-latin-regular.woff2',
        'https://fonts.gstatic.com/s/lobster/v28/neILzCirqoswsqX9zoKmMw.woff2',
        'b9b4c932ef89c39525bfe1b604cda3a1')
    download_and_check('theme_override/assets/javascripts/tablesort.js',
        'https://unpkg.com/tablesort@5.3.0/src/tablesort.js',
        '65eb57eaabaf9e968b8beee16a77072c')
    download_and_check('theme_override/assets/javascripts/tablesort.number.js',
        'https://unpkg.com/tablesort@5.3.0/src/sorts/tablesort.number.js',
        '377b82a88aeda884475d40fa1051c70a')
    download_and_check('theme_override/assets/javascripts/highlight.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js',
        '2a66af0aa884e09f41086cf620b4186f')
