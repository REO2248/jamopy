import jamoutils

class _존함:
    def __init__(self):
        self.김일성_김 = chr(0xF113)
        self.김일성_일 = chr(0xF114)
        self.김일성_성 = chr(0xF115)
        self.김일성 = self.김일성_김+self.김일성_일+self.김일성_성#
        self.KIS = self.김일성
        self.김정일_김 = chr(0xF116)
        self.김정일_정 = chr(0xF117)
        self.김정일_일 = chr(0xF118)
        self.김정일 = self.김정일_김+self.김정일_정+self.김정일_일#
        self.KJI = self.김정일
        self.김정은_김 = chr(0xF120)
        self.김정은_정 = chr(0xF121)
        self.김정은_은 = chr(0xF122)
        self.김정은 = self.김정은_김+self.김정은_정+self.김정은_은#
        self.KJU = self.김정은

존함 = _존함()
honorable = 존함

def 존함글자분리(string:str) -> jamoutils.조선글자:
    if len(string)!=1:
        raise ValueError('string must be a single character')
    if string==존함.김일성_김:
        return jamoutils.조선글자(자모.자음.ㄱ, 자모.모음.ㅣ, 자모.받침.ㅁ)
    elif string==존함.김일성_일:
        return jamoutils.조선글자(자모.자음.ㅇ, 자모.모음.ㅣ, 자모.받침.ㄹ)
    elif string==존함.김일성_성:
        return jamoutils.조선글자(자모.자음.ㅅ, 자모.모음.ㅓ, 자모.받침.ㅇ)
    elif string==존함.김정일_김:
        return jamoutils.조선글자(자모.자음.ㄱ, 자모.모음.ㅣ, 자모.받침.ㅁ)
    elif string==존함.김정일_정:
        return jamoutils.조선글자(자모.자음.ㅈ, 자모.모음.ㅓ, 자모.받침.ㅇ)
    elif string==존함.김정일_일:
        return jamoutils.조선글자(자모.자음.ㅇ, 자모.모음.ㅣ, 자모.받침.ㄹ)
    elif string==존함.김정은_김:
        return jamoutils.조선글자(자모.자음.ㄱ, 자모.모음.ㅣ, 자모.받침.ㅁ)
    elif string==존함.김정은_정:
        return jamoutils.조선글자(자모.자음.ㅈ, 자모.모음.ㅓ, 자모.받침.ㅇ)
    elif string==존함.김정은_은:
        return jamoutils.조선글자(자모.자음.ㅇ, 자모.모음.ㅡ, 자모.받침.ㄴ)
    else:
        raise ValueError('string must be a honorific character')



완성형수 = jamoutils.자음수*jamoutils.모음수*jamoutils.받침수

class _자모목록:
    def __init__(self):
        self.자음 = self._자음목록()
        self.모음 = self._모음목록()
        self.받침 = self._받침목록()
        self.j = self.자음
        self.m = self.모음
        self.p = self.받침
        self.jaum = self.자음
        self.moum = self.모음
        self.patcim = self.받침
        self.initial = self.자음
        self.medial = self.모음
        self.final = self.받침
        self.초성 = self.자음
        self.중성 = self.모음
        self.종성 = self.받침
        self.consonant = self.자음
        self.vowel = self.모음
        self.finalconsonant = self.받침
    class _자음목록:
        def __init__(self):
            self.ㄱ = jamoutils.자음(0)
            self.ㄲ = jamoutils.자음(1)
            self.ㄴ = jamoutils.자음(2)
            self.ㄷ = jamoutils.자음(3)
            self.ㄸ = jamoutils.자음(4)
            self.ㄹ = jamoutils.자음(5)
            self.ㅁ = jamoutils.자음(6)
            self.ㅂ = jamoutils.자음(7)
            self.ㅃ = jamoutils.자음(8)
            self.ㅅ = jamoutils.자음(9)
            self.ㅆ = jamoutils.자음(10)
            self.ㅇ = jamoutils.자음(11)
            self.ㅈ = jamoutils.자음(12)
            self.ㅉ = jamoutils.자음(13)
            self.ㅊ = jamoutils.자음(14)
            self.ㅋ = jamoutils.자음(15)
            self.ㅌ = jamoutils.자음(16)
            self.ㅍ = jamoutils.자음(17)
            self.ㅎ = jamoutils.자음(18)
            self.ㄱㄱ = self.ㄲ
            self.ㄷㄷ = self.ㄸ
            self.ㅂㅂ = self.ㅃ
            self.ㅅㅅ = self.ㅆ
            self.ㅈㅈ = self.ㅉ
    class _모음목록:
        def __init__(self):
            self.ㅏ = jamoutils.모음(0)
            self.ㅐ = jamoutils.모음(1)
            self.ㅑ = jamoutils.모음(2)
            self.ㅒ = jamoutils.모음(3)
            self.ㅓ = jamoutils.모음(4)
            self.ㅔ = jamoutils.모음(5)
            self.ㅕ = jamoutils.모음(6)
            self.ㅖ = jamoutils.모음(7)
            self.ㅗ = jamoutils.모음(8)
            self.ㅘ = jamoutils.모음(9)
            self.ㅙ = jamoutils.모음(10)
            self.ㅚ = jamoutils.모음(11)
            self.ㅛ = jamoutils.모음(12)
            self.ㅜ = jamoutils.모음(13)
            self.ㅝ = jamoutils.모음(14)
            self.ㅞ = jamoutils.모음(15)
            self.ㅟ = jamoutils.모음(16)
            self.ㅠ = jamoutils.모음(17)
            self.ㅡ = jamoutils.모음(18)
            self.ㅢ = jamoutils.모음(19)
            self.ㅣ = jamoutils.모음(20)
            self.ㅏㅣ = self.ㅐ
            self.ㅑㅣ = self.ㅒ
            self.ㅓㅣ = self.ㅔ
            self.ㅕㅣ = self.ㅖ
            self.ㅗㅏ = self.ㅘ
            self.ㅗㅐ = self.ㅙ
            self.ㅗㅣ = self.ㅚ
            self.ㅜㅓ = self.ㅝ
            self.ㅜㅔ = self.ㅞ
            self.ㅜㅣ = self.ㅟ
            self.ㅡㅣ = self.ㅢ
            self.ㅗㅏㅣ = self.ㅙ
            self.ㅜㅓㅣ = self.ㅞ
    class _받침목록:
        def __init__(self):
            self._ = jamoutils.받침(0)
            self.ㄱ = jamoutils.받침(1)
            self.ㄲ = jamoutils.받침(2)
            self.ㄳ = jamoutils.받침(3)
            self.ㄴ = jamoutils.받침(4)
            self.ㄵ = jamoutils.받침(5)
            self.ㄶ = jamoutils.받침(6)
            self.ㄷ = jamoutils.받침(7)
            self.ㄹ = jamoutils.받침(8)
            self.ㄺ = jamoutils.받침(9)
            self.ㄻ = jamoutils.받침(10)
            self.ㄼ = jamoutils.받침(11)
            self.ㄽ = jamoutils.받침(12)
            self.ㄾ = jamoutils.받침(13)
            self.ㄿ = jamoutils.받침(14)
            self.ㅀ = jamoutils.받침(15)
            self.ㅁ = jamoutils.받침(16)
            self.ㅂ = jamoutils.받침(17)
            self.ㅄ = jamoutils.받침(18)
            self.ㅅ = jamoutils.받침(19)
            self.ㅆ = jamoutils.받침(20)
            self.ㅇ = jamoutils.받침(21)
            self.ㅈ = jamoutils.받침(22)
            self.ㅊ = jamoutils.받침(23)
            self.ㅋ = jamoutils.받침(24)
            self.ㅌ = jamoutils.받침(25)
            self.ㅍ = jamoutils.받침(26)
            self.ㅎ = jamoutils.받침(27)
            self.ㄱㄱ = self.ㄲ
            self.ㄱㅅ = self.ㄳ
            self.ㄴㅈ = self.ㄵ
            self.ㄴㅎ = self.ㄶ
            self.ㄹㄱ = self.ㄺ
            self.ㄹㅁ = self.ㄻ
            self.ㄹㅂ = self.ㄼ
            self.ㄹㅅ = self.ㄽ
            self.ㄹㅌ = self.ㄾ
            self.ㄹㅍ = self.ㄿ
            self.ㄹㅎ = self.ㅀ
            self.ㅂㅅ = self.ㅄ
            self.ㅅㅅ = self.ㅆ

자모 = _자모목록()
jamo = 자모

자음목록 = []
for i in range(jamoutils.자음수):
    자음목록.append(jamoutils.자음(i).char)
모음목록 = []
for i in range(jamoutils.모음수):
    모음목록.append(jamoutils.모음(i).char)
받침목록 = []
for i in range(jamoutils.받침수):
    받침목록.append(jamoutils.받침(i).char)

def decompose_char(char:str) -> jamoutils.조선글자:
    """완성형 조선글자를 자음, 모음, 받침으로 분리합니다.

    Args:
        char (str): 분리할 글자 (한글자)

    Raises:
        ValueError: char이 한글자가 아닐 경우
        ValueError: char이 조선글자가 아닐 경우

    Returns:
        jamoutils.조선글자: 분리된 조선글자
    """
    if len(char)!=1:
        raise ValueError('char must be a single character')
    if not jamoutils.is_korean_syallable(char):
        raise ValueError('char must be a korean syllable character')
    code = ord(char)-jamoutils.완성형첫코드
    result = jamoutils.조선글자(
        jamoutils.자음(code//jamoutils.모음수//jamoutils.받침수),
        jamoutils.모음((code//jamoutils.받침수)%jamoutils.모음수),
        jamoutils.받침(code%jamoutils.받침수)
    )
    return result
def decompose(string:str) -> list: #jamoutils.조선글자 or str
    """완성형 조선글자문자렬을 자음, 모음, 받침으로 분리된 .
    Args:
        string (str): 분리할 문자렬
    Returns:
        list: 분리된 문자 목록
    """
    result = []
    for char in string:
        try:
            result.append(존함글자분리(char))
        except ValueError:
            if jamoutils.is_korean_syallable(char):
                result.append(decompose_char(char))
            else:
                result.append(jamoutils.글자(char))
    return result
분리 = decompose
자모분리 = decompose

def compose(*args:list[jamoutils.조선글자]) -> str:
    result = ''
    for 글자 in args[0]:
        if isinstance(글자, jamoutils.조선글자):
            result += str(글자.char)
        else:
            result += str(글자)
    return result
결합 = compose
자모결합 = compose

