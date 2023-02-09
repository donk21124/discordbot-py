import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '/엄':
        return '해당 발언은 팀 선셋과 아무런 연관이 없는 발언입니다'

    if message == '/symbols ;':
        return str(random.randint(1,4))

    if message == '/symbols；':
        return '2'

    if message == '/numbers ;':
        return str(random.randint(1, 13))

    if message == '/numbers；':
        return '8'

    if p_message == '/도움!':
        return '`"//동키"와 같이 팀원 이름을 적으면 해당 팀원에 대한 정보가 나옵니당! (주의: 디스코드에 명시된 풀 네임으로 적어야 작동됩니다!)`'

    if p_message == '/동키':
        return '`동키: 디렉터, 디자이너, 번역가 (영어), 영상 편집자, 마케터 (비주류), 경영자 (비주류), 보컬/성우 디렉터 (비주류)`'

    if p_message == '/브루스':
        return '`브루스: 서브 디렉터, 경영자, 사운드 디렉터 (비주류), 보컬/성우 디렉터 (비주류)`'

    if p_message == '/앤쵸비_스낵':
        return '`앤쵸비: 서브 디렉터, 사운드 디렉터, 경영자 (비주류), 마케터 (비주류)`'

    if p_message == '/롤라드':
        return '`롤라드: BGM/Instument 사운드 엔지니어`'

    if p_message == '/이누테루':
        return '`이누테루: 보컬/Instument 사운드 엔지니어`'

    if p_message == '/초아':
        return '`초아: UI/UX 및 GIF 일러스트레이터`'

    if p_message == '/주변인':
        return '`주변인: 스토리 작가, 보컬 디렉터, 성우 디렉터`'

    if p_message == '/스탕달':
        return '`스탕달: 프로그래머`'

    if p_message == '/도아케일':
        return '`도아케일: 마케터`'

    if p_message == '/루카스 챠게스':
        return '`루카스: 번역가 (포르투갈어)`'

    if p_message == '/동키 여친':
        return '`소개시켜줘요`'

    if p_message == '/엄준식 화이팅':
        return 'https://cdn.discordapp.com/attachments/1073333282063798432/1073344146925944932/EC9784ECA480EC8B9D-ED9994EC9DB4ED8C85.png'

    if p_message == '/이스터에그':
        return '`84 121 112 101 32 34 47 47 105 116 97 117 34`'

    if p_message == '/이스터에그 힌트':
        return '`영어 아스키코드 변환기`'

    if p_message == '/itau':
        return 'https://cdn.discordapp.com/attachments/1073333282063798432/1073351605434470510/qrcode.png'

    if p_message == '/ㄹㄱㄴ':
        return '`ㄹㄱㄴ`'

    return '슬래시 / 를 총 두개 붙여쓰세요!'