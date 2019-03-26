def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    # One slick way to do the swap is x[0], x[-1] = x[-1], x[0]
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    r1 = racers[0]
    r2 = racers[-1]
    
    racers[0] = r2
    racers[-1] = r1
