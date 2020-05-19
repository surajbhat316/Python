text = "X-DSPAM-Confidence:    0.8475";

pos = text.find(':')

pat=print(text[pos+1:].strip())


#z=pat.strip()
#print(z)
