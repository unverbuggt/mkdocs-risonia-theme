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
    download_and_check('theme_override/assets/javascripts/cryptojs/core.js',
        'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/core.js',
        'b55ae8027253d4d54c4f1ef3b6254646')
    download_and_check('theme_override/assets/javascripts/cryptojs/enc-base64.js',
        'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/enc-base64.js',
        'f551ce1340a86e5edbfef4a6aefa798f')
    download_and_check('theme_override/assets/javascripts/cryptojs/cipher-core.js',
        'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/cipher-core.js',
        'dfddc0e33faf7a794e0c3c140544490e')
    download_and_check('theme_override/assets/javascripts/cryptojs/pad-nopadding.js',
        'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/pad-nopadding.js',
        'e288e14e2cd299c3247120114e1178e6')
    download_and_check('theme_override/assets/javascripts/cryptojs/md5.js',
        'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/md5.js',
        '349498f298a6e6e6a85789d637e89109')
    download_and_check('theme_override/assets/javascripts/cryptojs/aes.js',
        'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/aes.js',
        'da81b91b1b57c279c29b3469649d9b86')
    download_and_check('theme_override/assets/javascripts/tablesort.js',
        'https://unpkg.com/tablesort@5.3.0/src/tablesort.js',
        '65eb57eaabaf9e968b8beee16a77072c')
    download_and_check('theme_override/assets/javascripts/tablesort.number.js',
        'https://unpkg.com/tablesort@5.3.0/src/sorts/tablesort.number.js',
        '377b82a88aeda884475d40fa1051c70a')
    download_and_check('theme_override/assets/javascripts/highlight.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js',
        '2a66af0aa884e09f41086cf620b4186f')
