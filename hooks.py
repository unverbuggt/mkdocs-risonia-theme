import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

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
