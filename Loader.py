# 역변환 규칙
reverse_rules = {
"d0d0f00": "0", "d0F00G1": "1", "d0D010": "2", "d0f01f1G": "3",
"d0F10E0": "4", "d0f1a01": "5", "d0f110": "6", "d01r1q1": "7",
"d1d0qR0": "8", "d10f01": "9",
"k3R9a": "a", "d2Bx7m": "b", "Qp4Lc": "c", "n8Wd1": "d", "d5eT0j": "e",
"Yf6Ks": "f", "r2Ng4": "g", "Hv9Xb": "h", "U3Co7": "i", "Lq1Pz": "j",
"w5Dm8": "k", "A6Ry2": "l", "tJ4Eh": "m", "M0Bn3F": "n", "Gu7Wc": "o",
"Ic9Mv": "p", "d5kZ2T": "q", "Px8Lr": "r", "Q1s6Ny": "s", "b4Hf0": "t",
"Ew3Ja": "u", "d9Vc5Ud": "v", "mK7Ri": "w", "Zt2Ox": "x", "d6Dn1Py": "y",
"Fs8Qw": "z",
"Cg4Xb": "A", "d7Lm2Ek": "B", "Ry9Nf": "C", "d3Hs6Vj": "D", "Wd1Tu": "E",
"d0Bp5Ka": "F", "Jz8Mc": "G", "Ui3Ql": "H", "d6Yx7Ro": "I", "Fn2Sv": "J",
"Gk4Ew": "K", "d9Zt1Pb": "L", "Rc6Hm": "M", "d5Wd8Ny": "N", "Ax3Lj": "O",
"Tf0Iq": "P", "d7Vs2Ko": "Q", "Bu4Xn": "R", "Cm9Ze": "S", "1Pg3Wr": "T",
"Hn7Fa": "U", "Dq5Mv": "V", "Ek2Yt": "W", "8Ri6Jb": "X", "Ls0Uc": "Y",
"Ow4Gd": "Z",
"X3Nt7": "`", "d5Br2Ka": "~", "Jv8Qm": "!", "Yc1Ew": "@", "d6Ls9Fx": "#",
"Mh4Td": "$", "Rn0Gu": "%", "Aq7Zi": "^", "d2Kp5Jy": "&", "Wb3Vc": "*",
"Eo9Sm": "(", "Fd6Nx": ")", "Ht1Lb": "-", "d3Qk8Ur": "_", "Gm5Wy": "=",
"Zj2Pd": "+", "Ic7Fa": "[", "Bn4Rv": "{", "Xt0Eg": "]", "d6Ms3Wh": "}",
"Qp9Yl": "\\", "Dv1Ka": "|", "Uf8Nm": ";", "Rc5Jb": ":", "d7Gw2Tx": "'",
"Lo4Iq": '"', "Hy6Zs": ",", "Ke3Vp": "<", "Mb0Uf": ".", "d9Nj7Cw": ">",
"Ar5Dl": "/", "St2Qx": "?",
"S1p2a3c4e": " "

}

# 디코딩할 파일 지정
file_path = "./data/hash.txt"  # 인코딩된 파일명

# 방법 A: utf-8-sig + BOM 강제 제거 (가장 안전)
with open(file_path, "r", encoding="utf-8-sig") as f:
    content = f.read()

# BOM 강제 제거 (이 한 줄 추가!)
if content.startswith("\ufeff"):
    content = content[1:]          # 또는 content = content.lstrip("\ufeff")

# 나머지 코드는 그대로
tokens = content.split(" ")
decoded = ""
for token in tokens:
    if token in reverse_rules:
        decoded += reverse_rules[token]
    else:
        decoded += token

# 디버그용 (필수로 한 번 확인해보세요)
print("Decoded first 300 characters:")
print(repr(decoded))   # BOM이 남아있는지 확인
print("-" * 50)

exec(decoded, globals())