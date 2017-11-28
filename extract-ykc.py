import sys, os
from ykc import Ykc

EXTRACT_PATH = "extracted"

for i in [elem for elem in sys.argv if elem.endswith(".ykc")]:
	ykc = Ykc.from_file(i)
	
	for f in ykc.header.entries:
		fname = f.filename.strip().replace("\\", "/")
		dname = os.path.dirname(fname)
		
		os.makedirs(''.join([EXTRACT_PATH, '/', dname]), exist_ok=True)
		with open(''.join([EXTRACT_PATH, '/', fname]), mode="xb") as writer:
			print(''.join([EXTRACT_PATH, '/', fname]))
			writer.write(f.body)

