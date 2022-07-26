import sys

intext = sys.stdin.read()
if len(intext) == 0:
    exit('Pipe some text into stdin') 
primemap = { 3: ' ', 5: '.', 7: '!', 11: '?'}
uwumap = { 0: 'u', 1: 'w', 2: 'U', 3: 'W' }

def flipdict(d):
    # thanks stack overflowz
    return {value: key for key, value in d.items()}

def uwuify(instr):
    print('~ uwuifying.......')
    ostr = ''
    for b in instr:
        tb = ord(b)
        ctext = ''
        for prime in primemap:
            cchar = primemap[prime]
            while tb % prime == 0:
                ctext += cchar
                tb //= prime
        while tb // 4 > 0:
            ctext += uwumap[tb % 4]
            tb //= 4
        ctext += uwumap[tb % 4]
        ostr += ctext[::-1] + ','
    return(ostr)

def deuwu(instr):
    print('~ deuwuifying.......')
    ostr = ''
    deuwumap = flipdict(uwumap)
    deprimemap = flipdict(primemap)
    for b in [k for k in instr.split(',') if k != '']:
        val = 0
        for letter in b:
            if letter not in primemap.values():
                val = val * 4 + deuwumap[letter]
            else:
                val *= deprimemap[letter]
        ostr += chr(val)
    return(ostr)

print(uwuify(intext.strip()))
print()
try:
    print(deuwu(intext.strip()))
except Exception as e:
    exit("Unable to de-uwu input text")
