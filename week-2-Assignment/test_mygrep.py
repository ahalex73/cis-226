# Alexander Holmes
# 9/9/22
# CRN: 10235
# CIS 226: Advanced Python Programming
# TOTAL TIME TO COMPLETE: --- 5 hours ---

from mygrep import text_in_file

def test_text_in_file(capsys):
    ''' Tests if the lines given to us by our mygrep tool returns what we
        expected

    The readouterr method returns a tuple of the output and or a thrown error
    the .out specifies that we want the output from capsys.
    Then mark our test as true if it has the expected output. '''
    
    text_in_file("jacob", "students.txt")
    assert capsys.readouterr().out == "jacob has english with james\n"





