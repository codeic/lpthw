indata = open("test.txt").read()

out_file = open("test.txt").read()

"new_file.txt", "w")
out_file.write(indata)

out_file.close()


# Mistakes:
    # 1.
    # Traceback (most recent call last):
    #   File "ex17v2.py", line 5, in <module>
    #   out_file = open("new_file.txt").write(indata)
    # IOError: File not open for writing
        # Added back "w" to open().
        
    # 2.
    # Traceback (most recent call last):
    #   File "ex17v2.py", line 7, in <module>
    #     out_file.close()
    # AttributeError: 'NoneType' object has no attribute 'close'
        # Defaulted. 
        
        
        
        
        Wrote comments about what of remaing lines does,
        # to make it easier to understand steps.

