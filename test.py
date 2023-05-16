import os
import requests

from pathlib import Path

from settings import ENCODING_KEY,DECODING_KEY

# API 엔드포인트 URL
url = Path("http://ws.bus.go.kr/api/rest/arrive/")

# GET 요청 보내기
response = requests.get(url)

# # 응답 코드 확인
# if response.status_code == 200:
#     # 요청이 성공한 경우 응답 데이터 가져오기
#     data = response.json()
#     # 데이터 처리
#     print(data)
# else:
#     # 요청이 실패한 경우 에러 메시지 출력
#     print("Error:", response.status_code)