from subprocess import Popen, PIPE, STDOUT

p = Popen(['doxygen', '-'], stdout=PIPE, stdin=PIPE, stderr=PIPE)

input = '\x1fINPUT = files/src\x1fOUTPUT_DIRECTORY = files/doxy2\x1fDOXYFILE_ENCODING = UTF-8\x1fGENERATE_XML = YES\x1fRECURSIVE = YES\x1fEXAMPLE_PATH = examples\x1fSHOW_NAMESPACES = YES\x1fGENERATE_HTML = NO\x1fGENERATE_LATEX = NO\x1f'


stdout_data = p.communicate(input.encode('utf-8'))[0].decode().strip()
print(stdout_data)