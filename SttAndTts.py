from time import sleep
import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
# 에러 시, pip install playsound==1.2.2 실행해볼 것 (윈도우 기준)

dir_audio = "C:\\Users\\jweun\\PycharmProjects\\swContest2023\\audio" #audio directory location (SocketServer.py에서 참조 중)
# dir_audio = "C:\\Users\\joyew\\Project\\sw23\\tmp"  # BY YEWON
filename = dir_audio + "\\voice.mp3"
inform_msg = "안녕하세요. 검색할 상품의 이름을 말씀해주세요."
effect_msg = "띵동"
loading_msg = "상품을 검색 중입니다. 잠시만 기다려주세요."
error_msg = "다시 말씀해주세요."

def make_audio(product_rank,text):
    #오디오파일 만들기
    tts = gTTS(text=text, lang='ko')
    tts.save(f'{dir_audio}/{product_rank}.mp3')

def speak(text):
    os.remove(filename)     # 이 부분 없으면 퍼미션 에러 발생 (파일을 연 상태에서의 추가 파일 생성 부분에서 에러가 발생하는 것으로 보임)
    tts = gTTS(text=text, lang='ko')
    tts.save(filename)      # 파일을 만들고,
    playsound(filename)     # 해당 음성 파일을 실행 (즉, 음성을 말함)

def get_key():

 #   speak(inform_msg) # 안내 방송(음성)

    while True:
        speak(effect_msg)
        
        try:
            # 사용자 음성 듣기
            r = sr.Recognizer()
            mic = sr.Microphone(device_index = 1)

            with mic as source:
                audio = r.listen(source, timeout = 3)

            query_txt = r.recognize_google(audio, language="ko-KR")
            print(query_txt)
        
            speak(loading_msg) # 로딩 메시지 방송(음성)
            return (query_txt)
        except sr.UnknownValueError:
            print("음성 인식 실패")
        except sr.RequestError:
            print("HTTP Request Error 발생")
        except sr.WaitTimeoutError:
            print("WaitTimeout Error 발생 ㅠㅠ")
            
        speak(error_msg)
        sleep(1)

    return -1