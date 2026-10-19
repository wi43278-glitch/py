'''

* 기본환경 : 모든 개발환경에 공통적으로 설치가됨
*  가상환경 : 해당 프로젝트에서만 사용하는 패키지 설치

* 가상환경 만들기
    터미널에서 
     (py)pythone -m venv 이름
    
 * 가상환경 활성화(cmd) (파워셀은 권한 부여해야 됨)


    가상환경이름\Scripts\activate


* 가상환경 종료

    deactivate


> 외부 라이브러리 중에서 requset를 함 
: requests 는 외부 웹페이지에 접근 응답을 받아오는 http 통신라이브러리


'''
import requests

def get_ex():
    resopnse = requests.get('https://google.com')
    print(f'Status Code : {resopnse.status_code}')

if __name__ == '__main__':
    get_ex()
