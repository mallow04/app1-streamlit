import streamlit as st

st.title(':cat:펫 가이드:dog:')
st.info('반려동물 보호자분들께 필요한 정보를 보기 쉽게 정리해서 제공해드려요 :)')
#st.caption('d') 

st.subheader('**수원 근처 동물병원**') # 제목

with st.expander('**:violet[<정직한 동물 의료센터>]**'): # 서브제목
    st.write('전화번호) 0507-1303-7617')
    st.write('주소) 경기도 수원시 권선구 경수대로 411 1층')
    st.write('영업시간) 매일 09:00 – 22:00')
    st.write('특징) 석박사 의료진이 강아지와 고양이만 전문적으로 진료하며 대기실, 진료실, 입원실이 분리되어 있음')

with st.expander('**:violet[<아이러브 동물병원>]**'): # 서브제목
    st.write('전화번호) 0507-1387-7551')
    st.write('주소) 경기 수원시 장안구 송원로 69 4층')
    st.write('영업시간) 평일 11:00 – 19:00 / 토요일 11:00 – 17:00 / 일요일 11:00 – 16:00 / 휴게시간 14:00 – 15:00')
    st.write('특징) 슬개골수술 , 십자인대파열, 슬개골탈구수술, 관절고정술 등 슬개골특화 진료 병원임')

with st.expander('**:violet[<본동물의료센터>]**'): # 서브제목
    st.write('전화번호) 031-248-8275')
    st.write('주소) 경기 수원시 장안구 송정로 114 본동물의료센터')
    st.write('영업시간) 매일 00:00 – 24:00 연중무휴')
    st.write('특징) 지역병원에서 치료하기 어려운 반려동물들을 의뢰 받아 치료하는 경기도 지역 거점 2차 동물병원으로 소화기내과, 피부과, 심장내과, 종양내과, 내분비내과, 정형신경외과, 일반외과, 안과, 치과, 영상진단의학과 등 각 과별 전공의를 포함한 80여명의 의료진들로 구성되어 있음')

with st.expander('**:violet[<수원 종합 동물병원>]**'): # 서브제목
    st.write('전화번호) 031-214-5527')
    st.write('주소) 경기 수원시 영통구 중부대로 263')
    st.write('영업시간) 평일&토요일 09:00 – 20:00 / 일요일 10:00 – 20:00')

with st.expander('**:violet[<돌봄 동물병원>]**'): # 서브제목
    st.write('전화번호) 031-217-7570')
    st.write('주소) 경기 수원시 팔달구 중부대로 251 2층')
    st.write('영업시간) 매일 10:00 – 20:00 / 휴게시간 12:00 - 13:00')
    st.write('특징) 수원 최대 규모의 오픈 수술실을 운영하며 외과, 치과, 내과, 안과로 분과하여 진단 및 수술, 치료를 진행함 ')

with st.expander('**:violet[<라온 동물병원>]**'): # 서브제목
    st.write('전화번호) 031-215-8588')
    st.write('주소) 경기 수원시 영통구 동탄원천로1109번길 100')
    st.write('영업시간) 금요일 10:00 – 19:30 / 토요일 10:00 – 18:00 / 일요일 휴무 / 휴게시간 12:00 - 13:30 ')

with st.expander('**:violet[<24시 마음반려 동물 의료원>]**'): # 서브제목
    st.write('전화번호) 031-211-0975')
    st.write('주소) 경기 수원시 팔달구 경수대로 461')
    st.write('영업시간) 매일 00:00 – 24:00 연중무휴 / 휴게시간 12:00 - 13:00')
    st.write('특징) 전문 영상장비(16채널 CT, 초음파, X-ray, C-arm 등)를 기반으로 내과, 외과, 영상의학과 등 각 전공의 의료진들이 분과 진료를 실시함 / 일반외과 수술부터 고난이도 외과수술까지 가능하며 보호자님들이 처치과정을 보실 수 있도록 오픈 처치실을 운영함') 

st.subheader('**흔한 질병 증상**') # 제목

with st.expander('**:violet[<열사병>]**'): # 서브제목
    st.write('원인) 강아지 체온이 40도 이상으로 올라갈 때 발생')
    st.write('증상) 과도한 헐떡거림, 침 흘림, 무기력증, 쓰러짐 ')

with st.expander('**:violet[<탈수증>]**'): # 서브제목
    st.write('원인) 더운 날씨에 야외에서 많은 수분을 잃을 때 발생')
    st.write('증상) 잇몸 건조, 눈의 함몰, 무기력증')

with st.expander('**:violet[<일광 화상>]**'): # 서브제목
    st.write('원인) 털이 짧거나 밝을수록 걸리기 쉬우며 강한 햇볕에 장시간 노출되었을 경우 발생')
    st.write('증상) 붉은 반점, 피부 벗겨짐, 피부암 ')

with st.expander('**:violet[<알레르기>]**'): # 서브제목
    st.write('원인) 봄, 여름철 꽃가루, 풀, 곰팡이에 의해 발생')
    st.write('증상) 가려움증, 긁기, 눈 충혈, 귀 감염')

with st.expander('**:violet[<외이염, 중이염, 청각 장애>]**'): # 서브제목
    st.write('원인) 귀가 덮여있거나 귀에 털이 많은 강아지에게 자주 발생하며 박테리아, 진드기, 이물질 등에 의해 유발')
    st.write('증상) 귀를 자주 긁음, 머리를 양옆으로 흔듦')

with st.expander('**:violet[<슬개골 탈구>]**'): # 서브제목
    st.write('원인) 소형견에게 흔히 발생하며, 유전적 혹은 외상성 부상으로 인해 발생')
    st.write('증상) 다리를 절거나 깽깽이 걸음을 함')

with st.expander('**:violet[<감기>]**'): # 서브제목
    st.write('원인) 기온이 낮은 곳에 장시간 머물거나 다른 강아지에게 전염되어 발생')
    st.write('증상) 기침, 구토, 무기력증')

with st.expander('**:violet[<암>]**'): # 서브제목
    st.write('원인) 장기에서 종양으로 발생하며 노견일 경우 면역이 저하되면서 발생하는 경우가 빈번함')
    st.write('증상) 활력 저하, 식욕 부진, 구토, 설사, 악취, 체중 저하')

st.subheader('**주의해야 할 음식**') # 제목

with st.expander('**:violet[<초콜릿>]**'): # 서브제목
    st.write('카페인과 테오브린을 함유하고 있어 강아지에게 중독을 유발할 수 있으며, 소화되지 않고 신장에서 분해되어 나오기 때문에 소화기관의 문제를 일으킬 수 있음')

with st.expander('**:violet[<양파, 파, 마늘>]**'): # 서브제목
    st.write('소화기관을 자극해 위장장애를 유발할 수 있으며 일부 성분은 강아지의 적혈구 파괴를 유발하여 빈혈을 일으킬 수 있음')

with st.expander('**:violet[<계란 흰자>]**'): # 서브제목
    st.write('살모넬라균과 같은 세균이 흰자에 존재할 가능성이 높으며 특정 단백질이 비타민의 흡수를 방해하여 노화 및 영양분 문제를 일으킬 수 있음')

with st.expander('**:violet[<아보카도>]**'): # 서브제목
    st.write('살균독소가 함유되어 있어 소량만 섭취해도 구토와 설사의 증상을 유발함')

with st.expander('**:violet[<생땅콩>]**'): # 서브제목
    st.write('장내 가스를 발생시켜 복통을 일으킬 수 있음')

with st.expander('**:violet[<포도>]**'): # 서브제목
    st.write('반려동물의 콩팥을 훼손하는 독소가 들어있어 급성 신부전의 원인이 될 수 있음')

with st.expander('**:violet[<자몽>]**'): # 서브제목
    st.write('자몽의 산 성분으로 인해 위장기관에 자극이 되어 구토, 속쓰림, 설사 등을 유발함')

st.subheader('**강아지 기본케어**') # 제목

with st.expander('**:violet[<발톱 자르기>]**'): # 서브제목
    st.write('발톱이 너무 길 경우 휘거나 부러져 발톱 속 혈관이 다칠 위험이 있으므로 2~3주 주기로 잘라주어야하며, 발톱 속 정맥을 자르지 않도록 주의해야함 https://youtu.be/xFh2k0cay1g?si=ibk1PZAzHEfkH5Db')

with st.expander('**:violet[<눈물 닦기>]**'): # 서브제목
    st.write('눈물과 눈꼽은 방치하면 염증이 생겨 눈 건강에도 악영향을 미칠 수 있으므로 하루에 최소 한번 닦아 관리해줘야함')
    st.write('https://youtu.be/q8ocAw3WtGw?si=ar8_mVBGxWgWgLoW')
 
with st.expander('**:violet[<이빨 닦기>]**'): # 서브제목
    st.write('강아지 침에는 기본적으로 살균 성분이 포함되어 있지만 이빨을 닦아주지 않으면 치석이 점층적으로 쌓여 치아 부식, 구강염, 악취 등을 발생시킬 수 있음 https://youtu.be/UvWL0wviLlo?si=J8BXSUldpHYUpPw5')

with st.expander('**:violet[<산책 후 발 닦기>]**'): # 서브제목
    st.write('https://youtu.be/mXliGLg6On8?si=ZFjnaX3YphmSrjXW')

with st.expander('**:violet[<목욕하기>]**'): # 서브제목
    st.write('위생, 피부관리, 털 관리 등을 위해 필요하며 먼지와 냄새의 원인이 되는 박테리아를 제거할 수 있어 피부병, 해충을 예방하는 데에 필수적임')
    st.write('https://youtu.be/zFNF-D_gEbA?si=GU31_0nx_9Adq2RN')

with st.expander('**:violet[<항문낭 짜기>]**'): # 서브제목
    st.write('항문낭 분비물이 제대로 비워지지 않을경우 통증, 염증을 유발하고 항문이 빨갛게 붓거나 항문을 지속적으로 핥는 증상을 보일 수 있음')
    st.write('https://youtube.com/shorts/DUGK0WBI4h4?si=zozBZ_dIS8PXlDxK')

st.subheader('**강아지 훈련법**') # 제목 

with st.expander('**:violet[<배변훈련>]**'): # 서브제목
    st.write('https://youtu.be/mnPlK6NR92U?si=10QJmmR1UIjChbKa')

with st.expander('**:violet[<기다려>]**'): # 서브제목
    st.write('https://youtu.be/aFojR9xDl30?si=Zy4otmf9sZ3VcPUD')

with st.expander('**:violet[<손>]**'): # 서브제목
    st.write('https://youtu.be/1s-V_JMmfhk?si=eEWIn-xMgTdFE7Mr')

with st.expander('**:violet[<앉아>]**'): # 서브제목
    st.write('https://youtu.be/qG3cZgje2CE?si=fN9YjsyZr5YuCAhk')

st.subheader('**강아지들의 언어-카밍시그널**') # 제목 

with st.expander('**:violet[<낯선 사람과 시선 마주치기>]**'): # 서브제목
    st.write('강한 경계와 도전을 의미')

with st.expander('**:violet[<앞다리 들기>]**'): # 서브제목
    st.write('놀라서 긴장했거나 불편함을 느끼고 있는 상태')

with st.expander('**:violet[<코 핥기>>]**'): # 서브제목
    st.write('불편, 불안, 긴장을 표현')

with st.expander('**:violet[<꼬리를 세우고 기지개를 필 때>]**'): # 서브제목
    st.write('놀이를 시작하자고 하는 것으로 같이 놀아달라는 뜻')

with st.expander('**:violet[<하품>]**'): # 서브제목
    st.write('긴장했거나 스트레스를 받았을 때 스트레스를 완화시키려고 하는 행동 또는 보호자를 진정시키기 위함')

with st.expander('**:violet[<꼬리 흔들기>]**'): # 서브제목
    st.write('반가운 상황일 때-기분이 좋고 반갑다는 의미')
    st.write('긴장되는 상황일 때-경계심과 우월감을 드러내려는 의도')

with st.expander('**:violet[<몸 터는 행동>]**'): # 서브제목
    st.write('스트레스를 완화시키거나 어떤 행동을 하다 한숨을 돌릴 때 보이는 행동')

with st.expander('**:violet[<한숨>]**'): # 서브제목
    st.write('눈을 반쯤 감고 쉴 때-편안한 상태')
    st.write('눈을 완전히 뜨고 쉴 때-실망한 상태')

with st.expander('**:violet[<덥지 않은 상태에서 헥헥거림>]**'): # 서브제목
    st.write('불안함을 느낄 때')

    st.write('눈을 완전히 뜨고 쉴 때-실망한 상태')

with st.expander('**:violet[<덥지 않은 상태에서 헥헥거림>]**'): # 서브제목
    st.write('불안함을 느낄 때')
