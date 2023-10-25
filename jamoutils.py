자음수=19
모음수=21
받침수=28
자음첫코드=0x1100
모음첫코드=0x1161
받침첫코드=0x11a7
자음채움=chr(0x115f)
모음채움=chr(0x1160)
완성형첫코드=0xac00
완성형수 = 자음수*모음수*받침수

def is_korean_syallable(string:str) -> bool:
    for char in string:
        if ord(char)<완성형첫코드 or ord(char)>=완성형첫코드+완성형수:
            return False
    return True

class 자음(int):
    def __new__(cls, 번호:int):
        if 번호>=자음수:
            raise ValueError('자음번호는 0~18 사이이여야 합니다.')
        self = super().__new__(cls, 번호)
        return self
    _호환 = [
        'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ',
        'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
        'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ',
        'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
    ]
    def __str__(self):
        return self.char
    @property
    def char(self):
        return self._호환[self]
    @property
    def type(self):
        return 0
    @property
    def jamo(self):#ᄀ
        return chr(자음첫코드+self)

class 모음(int):
    def __new__(cls, 번호:int):
        if 번호>=모음수:
            raise ValueError('모음번호는 0~20 사이이여야 합니다.')
        self = super().__new__(cls, 번호)
        return self
    _호환 = [
        'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ',
        'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
        'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ',
        'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
        'ㅣ'
    ]
    def __str__(self):
        return self.char
    @property
    def char(self):
        return self._호환[self]
    @property
    def type(self):
        return 1
    @property
    def jamo(self):#ᅡ
        return chr(모음첫코드+self)

class 받침(int):
    def __new__(cls, 번호:int):
        if 번호>=받침수:
            raise ValueError('받침번호는 0~27 사이이여야 합니다.')
        self = super().__new__(cls, 번호)
        return self
    _호환 = [
        '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ',
        'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ',
        'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ',
        'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
        'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ',
        'ㅌ', 'ㅍ', 'ㅎ'
    ]
    def __str__(self):
        return self.char
    @property
    def char(self):
        return self._호환[self]
    @property
    def type(self):
        return 2
    @property
    def jamo(self):#ᆨ
        return chr(받침첫코드+self)

class 조선글자(tuple):
    def __new__(cls, 자음:자음, 모음:모음, 받침:받침):
        if 자음.type!=0:
            raise ValueError('자음은 자음이여야 합니다.')
        if 모음.type!=1:
            raise ValueError('모음은 모음이여야 합니다.')
        if 받침.type!=2:
            raise ValueError('받침은 받침이여야 합니다.')
        self = super().__new__(cls, (자음, 모음, 받침))
        return self
    def __str__(self):
        return self.char
    @property
    def 조선글자인가(self):
        return True
    @property
    def 자음(self):
        return self[0]
    @property
    def 모음(self):
        return self[1]
    @property
    def 받침(self):
        return self[2]
    @property
    def char(self):
        return chr(
            완성형첫코드+
            self.자음*모음수*받침수+
            self.모음*받침수+
            self.받침
        )

class 글자(str):
    def __new__(cls, char:str):
        if len(char)!=1:
            raise ValueError('char must be a single character')
        if is_korean_syallable(char):
            raise ValueError('char must not be a korean syllable character')
        self = super().__new__(cls, char)
        return self
    def __str__(self):
        return self.char
    @property
    def 조선글자인가(self):
        return False
    @property
    def char(self):
        return self