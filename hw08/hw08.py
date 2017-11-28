passphrase = '23c1c1'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '2caf3fec71b31be27f69dd8d7b86efa50ba8cf50bdf9511fdae5a7f2'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()