rules = {

"0": "d0d0f00", "1": "d0F00G1", "2": "d0D010", "3": "d0f01f1G",
"4": "d0F10E0", "5": "d0f1a01", "6": "d0f110", "7": "d01r1q1",
"8": "d1d0qR0", "9": "d10f01",
"a": "k3R9a", "b": "d2Bx7m", "c": "Qp4Lc", "d": "n8Wd1", "e": "d5eT0j",
"f": "Yf6Ks", "g": "r2Ng4", "h": "Hv9Xb", "i": "U3Co7", "j": "Lq1Pz",
"k": "w5Dm8", "l": "A6Ry2", "m": "tJ4Eh", "n": "M0Bn3F", "o": "Gu7Wc",
"p": "Ic9Mv", "q": "d5kZ2T", "r": "Px8Lr", "s": "Q1s6Ny", "t": "b4Hf0",
"u": "Ew3Ja", "v": "d9Vc5Ud", "w": "mK7Ri", "x": "Zt2Ox", "y": "d6Dn1Py",
"z": "Fs8Qw",
"A": "Cg4Xb", "B": "d7Lm2Ek", "C": "Ry9Nf", "D": "d3Hs6Vj", "E": "Wd1Tu",
"F": "d0Bp5Ka", "G": "Jz8Mc", "H": "Ui3Ql", "I": "d6Yx7Ro", "J": "Fn2Sv",
"K": "Gk4Ew", "L": "d9Zt1Pb", "M": "Rc6Hm", "N": "d5Wd8Ny", "O": "Ax3Lj",
"P": "Tf0Iq", "Q": "7Vs2Ko", "R": "Bu4Xn", "S": "Cm9Ze", "T": "1Pg3Wr",
"U": "Hn7Fa", "V": "Dq5Mv", "W": "Ek2Yt", "X": "8Ri6Jb", "Y": "Ls0Uc",
"Z": "Ow4Gd",
"`": "X3Nt7", "~": "d5Br2Ka", "!": "Jv8Qm", "@": "Yc1Ew", "#": "d6Ls9Fx",
"$": "Mh4Td", "%": "Rn0Gu", "^": "Aq7Zi", "&": "d2Kp5Jy", "*": "Wb3Vc",
"(": "Eo9Sm", ")": "Fd6Nx", "-": "Ht1Lb", "_": "d3Qk8Ur", "=": "Gm5Wy",
"+": "Zj2Pd", "[": "Ic7Fa", "{": "Bn4Rv", "]": "Xt0Eg", "}": "d6Ms3Wh",
"\\": "Qp9Yl", "|": "Dv1Ka", ";": "Uf8Nm", ":": "Rc5Jb", "'": "d7Gw2Tx",
'"': "Lo4Iq", ",": "Hy6Zs", "<": "Ke3Vp", ".": "Mb0Uf", ">": "d9Nj7Cw",
"/": "Ar5Dl", "?": "St2Qx",
" ": "S1p2a3c4e"
}

def transform_code(file_path: str, output_path: str):
    """다른 파이썬 파일을 읽어서 규칙에 따라 변환 후 저장"""
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
        
    SEPARATOR = " "

    # 각 문자를 rules에서 찾아 한 번에 변환 (연쇄 치환 방지, 구분자로 토큰 분리)
    result = SEPARATOR.join(rules.get(ch, ch) for ch in code)

    # 변환된 코드 저장
    with open(output_path, "w", encoding="utf-8-sig") as f:
        f.write(result)

    print(f"변환 완료! 결과는 {output_path}에 저장되었습니다.")


if __name__ == "__main__":
    # 예시: menu.py 파일을 읽어서 변환 후 result.py에 저장
    transform_code("menu.py", "./data/hash.txt")
    