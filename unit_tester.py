import sys

def test(did_pass):
    """   Print the result of a test.  
    pre:  boolean
    post: print the caller's line number and the status of the test, ok (1) or failed (0)
    """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
