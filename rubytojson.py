import os
import subprocess
import time


def ruby_to_json(code, prefix='', cache_timeout=-1):
    # cache_timeout is in seconds.
    # default -1 indicates no cache.

    cache_file = "/tmp/ruby_to_json_%s_%s.json" % (prefix, str(hash(code)))
    try:
        age = time.time() - os.stat(cache_file).st_mtime
        if age > cache_timeout:
            raise
        with open(cache_file, 'r') as f:
            out = f.read()
    except:
        p = subprocess.Popen([os.path.dirname(os.path.abspath(__file__)) + '/ruby_to_json.rb', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, _ = p.communicate()
        if cache_timeout != -1:
            with open(cache_file, 'w') as f:
                f.write(out)
    return out
