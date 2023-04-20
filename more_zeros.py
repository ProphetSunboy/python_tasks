def more_zeros(s):
    """
    Receive a string for input, and return an array, containing only the
    characters from that string whose binary representation of its ASCII value
    consists of more zeros than ones. 
    """    
    res = []
    for ch in s:
        byte_ch = format(ord(ch), 'b')
        if byte_ch.count('0') > byte_ch.count('1') and ch not in res:
            res.append(ch)
            
    return res